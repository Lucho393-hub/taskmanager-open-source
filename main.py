# ==========================================
# TaskManager Open Source - Versión Avanzada
# Sistema avanzado de gestión de tareas
# Licencia: MIT
# ==========================================

# Importamos las librerías necesarias
import json  # Para trabajar con archivos JSON (guardar/cargar datos)
import os  # Para verificar si existen archivos en el sistema
from datetime import datetime  # Para manejar fechas y horas

# Lista global que almacenará todas las tareas en memoria durante la ejecución
tareas = []

def cargar_tareas():
    """
    Carga las tareas desde archivo JSON al iniciar el programa.
    Si no existe el archivo, intenta migrar desde el formato antiguo .txt
    """
    try:
        # Verificamos si existe el archivo tareas.json
        if os.path.exists("tareas.json"):
            # Abrimos el archivo en modo lectura con codificación UTF-8
            with open("tareas.json", "r", encoding="utf-8") as archivo:
                global tareas  # Usamos la variable global 'tareas'
                tareas = json.load(archivo)  # Cargamos el JSON a la lista
                print(f"✅ Se cargaron {len(tareas)} tareas.")
        else:
            # Si no existe el archivo JSON, intentamos migrar desde .txt
            migrar_desde_txt()
    except Exception as e:
        # Capturamos cualquier error y lo mostramos
        print(f"⚠️ Error al cargar tareas: {e}")

def migrar_desde_txt():
    """
    Migra tareas desde el formato .txt antiguo al nuevo formato JSON.
    Esto permite mantener compatibilidad con versiones anteriores.
    """
    try:
        # Verificamos si existe el archivo antiguo
        if os.path.exists("tareas.txt"):
            with open("tareas.txt", "r", encoding="utf-8") as archivo:
                # Leemos cada línea del archivo
                for linea in archivo:
                    # Separamos los datos usando el delimitador "|"
                    datos = linea.strip().split("|")
                    # Verificamos que la línea tenga al menos 4 campos
                    if len(datos) >= 4:
                        # Creamos un diccionario con la estructura nueva
                        tarea = {
                            "id": len(tareas) + 1,  # Generamos ID único
                            "nombre": datos[0],  # Nombre de la tarea
                            "descripcion": "",  # Campo nuevo, lo dejamos vacío
                            "prioridad": datos[1],  # Alta, Media o Baja
                            "estado": datos[2],  # Pendiente o Completada
                            "categoria": "General",  # Categoría por defecto
                            "fecha_creacion": datos[3],  # Fecha original
                            "fecha_vencimiento": "",  # Campo nuevo
                            "etiquetas": []  # Campo nuevo para etiquetas
                        }
                        tareas.append(tarea)  # Añadimos a la lista
            guardar_tareas()  # Guardamos en el nuevo formato
            print("✅ Tareas migradas al nuevo formato.")
    except FileNotFoundError:
        # Si no existe el archivo .txt, no hacemos nada
        pass

def guardar_tareas():
    """
    Guarda todas las tareas en formato JSON.
    Se ejecuta automáticamente al salir del programa.
    """
    try:
        # Abrimos el archivo en modo escritura
        with open("tareas.json", "w", encoding="utf-8") as archivo:
            # Guardamos la lista como JSON con formato legible
            # indent=2: sangría de 2 espacios
            # ensure_ascii=False: permite caracteres especiales (ñ, acentos)
            json.dump(tareas, archivo, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"⚠️ Error al guardar: {e}")

def mostrar_tareas(filtro=None):
    """
    Muestra las tareas en formato tabla.
    
    Parámetros:
        filtro (str): Puede ser None, "pendientes", "completadas" o un término de búsqueda
    """
    # Verificamos si hay tareas
    if not tareas:
        print("\n📋 No hay tareas registradas.")
        return

    # Por defecto mostramos todas las tareas
    tareas_filtradas = tareas
    
    # Aplicamos filtros según el parámetro recibido
    if filtro == "pendientes":
        # Filtramos solo las tareas pendientes usando list comprehension
        tareas_filtradas = [t for t in tareas if t["estado"] == "Pendiente"]
    elif filtro == "completadas":
        # Filtramos solo las tareas completadas
        tareas_filtradas = [t for t in tareas if t["estado"] == "Completada"]
    elif filtro:
        # Si hay un filtro de texto, buscamos en el nombre de la tarea
        tareas_filtradas = [t for t in tareas if filtro.lower() in t["nombre"].lower()]

    # Verificamos si el filtro encontró resultados
    if not tareas_filtradas:
        print(f"\n📋 No hay tareas que coincidan con el filtro.")
        return

    # Imprimimos el encabezado de la tabla
    print("\n" + "="*80)
    # Usamos format strings para alinear columnas:
    # <5 significa alinear a la izquierda con ancho de 5 caracteres
    print(f"{'ID':<5} {'NOMBRE':<25} {'PRIORIDAD':<10} {'ESTADO':<12} {'CATEGORÍA':<15}")
    print("="*80)
    
    # Iteramos sobre cada tarea filtrada
    for t in tareas_filtradas:
        # Asignamos emojis según la prioridad usando un diccionario
        icono_prioridad = {"Alta": "🔴", "Media": "🟡", "Baja": "🟢"}.get(t["prioridad"], "⚪")
        # Emoji para el estado (completada o pendiente)
        icono_estado = "✅" if t["estado"] == "Completada" else "⏳"
        
        # Imprimimos la fila de la tarea
        # [:24] limita el nombre a 24 caracteres para evitar desbordar la columna
        print(f"{t['id']:<5} {t['nombre'][:24]:<25} {icono_prioridad} {t['prioridad']:<8} {icono_estado} {t['estado']:<10} {t['categoria'][:14]:<15}")
        
        # Mostramos la descripción si existe (usando .get para evitar errores)
        if t.get("descripcion"):
            print(f"      Descripción: {t['descripcion'][:60]}")
        
        # Mostramos las etiquetas si existen
        if t.get("etiquetas"):
            # Convertimos la lista de etiquetas en un string separado por comas
            # Agregamos el símbolo # a cada etiqueta
            etiquetas_str = ", ".join([f"#{tag}" for tag in t["etiquetas"]])
            print(f"      Etiquetas: {etiquetas_str}")
        
        # Mostramos la fecha de vencimiento si existe
        if t.get("fecha_vencimiento"):
            print(f"      📅 Vence: {t['fecha_vencimiento']}")
        
        # Línea separadora entre tareas
        print("-"*80)

def agregar_tarea():
    """
    Permite al usuario agregar una nueva tarea con todos sus detalles.
    Solicita: nombre, descripción, prioridad, categoría, etiquetas y fecha de vencimiento.
    """
    print("\n--- AGREGAR NUEVA TAREA ---")
    
    # Solicitamos el nombre y eliminamos espacios al inicio/final con .strip()
    nombre = input("📝 Nombre de la tarea: ").strip()
    # Validamos que el nombre no esté vacío
    if not nombre:
        print("❌ El nombre no puede estar vacío.")
        return  # Salimos de la función

    # Descripción opcional
    descripcion = input("📄 Descripción (opcional): ").strip()

    # Menú de prioridades
    print("\n🎯 Prioridad:")
    print("1. Alta")
    print("2. Media")
    print("3. Baja")
    p = input("Elige prioridad (1-3): ").strip()

    # Usamos un diccionario para mapear la opción a la prioridad
    # Si no es válida, usamos "Media" como valor por defecto
    prioridad = {"1": "Alta", "2": "Media", "3": "Baja"}.get(p, "Media")

    # Categoría con valor por defecto "General"
    categoria = input("📂 Categoría (ej: Trabajo, Personal, Estudios): ").strip() or "General"

    # Etiquetas: pedimos que las separen por comas
    print("\n🏷️ Etiquetas (separadas por comas, ej: urgente,importante):")
    etiquetas_input = input("Etiquetas: ").strip()
    # Dividimos el string por comas, eliminamos espacios y filtramos vacíos
    etiquetas = [e.strip() for e in etiquetas_input.split(",") if e.strip()]

    # Fecha de vencimiento opcional
    print("\n📅 Fecha de vencimiento (DD/MM/YYYY, opcional):")
    fecha_venc = input("Fecha: ").strip()

    # Obtenemos la fecha/hora actual y la formateamos
    fecha_creacion = datetime.now().strftime("%d/%m/%Y %H:%M")

    # Creamos el diccionario de la nueva tarea
    tarea = {
        # Generamos ID único: buscamos el ID máximo y le sumamos 1
        # Si no hay tareas, usamos 0 como default
        "id": max([t["id"] for t in tareas], default=0) + 1,
        "nombre": nombre,
        "descripcion": descripcion,
        "prioridad": prioridad,
        "estado": "Pendiente",  # Por defecto las tareas se crean como pendientes
        "categoria": categoria,
        "fecha_creacion": fecha_creacion,
        "fecha_vencimiento": fecha_venc,
        "etiquetas": etiquetas
    }

    # Añadimos la tarea a la lista
    tareas.append(tarea)
    print(f"\n✅ Tarea agregada con ID {tarea['id']}.")

def editar_tarea():
    """
    Permite editar una tarea existente.
    El usuario puede modificar: nombre, descripción, estado y prioridad.
    """
    # Verificamos si hay tareas
    if not tareas:
        print("\n📋 No hay tareas para editar.")
        return

    # Mostramos todas las tareas primero
    mostrar_tareas()
    
    try:
        # Solicitamos el ID de la tarea a editar
        tarea_id = int(input("\n🔢 ID de la tarea a editar: "))
        
        # Buscamos la tarea con ese ID usando next()
        # next() devuelve el primer elemento que coincida o None si no encuentra
        tarea = next((t for t in tareas if t["id"] == tarea_id), None)
        
        # Verificamos si se encontró la tarea
        if not tarea:
            print("❌ Tarea no encontrada.")
            return

        # Mostramos qué tarea estamos editando
        print(f"\n--- EDITANDO: {tarea['nombre']} ---")
        
        # Para cada campo, mostramos el valor actual y permitimos cambiarlo
        # Si el usuario presiona Enter sin escribir nada, mantenemos el valor actual
        
        print(f"\nNombre actual: {tarea['nombre']}")
        nuevo_nombre = input("Nuevo nombre (Enter para mantener): ").strip()
        if nuevo_nombre:  # Solo actualizamos si ingresó algo
            tarea["nombre"] = nuevo_nombre

        print(f"\nDescripción actual: {tarea.get('descripcion', '')}")
        nueva_desc = input("Nueva descripción (Enter para mantener): ").strip()
        if nueva_desc:
            tarea["descripcion"] = nueva_desc

        # Menú para cambiar el estado
        print("\n🔄 Cambiar estado:")
        print("1. Pendiente")
        print("2. En progreso")
        print("3. Completada")
        print("4. Cancelada")
        e = input("Elige (Enter para mantener): ").strip()
        
        # Diccionario para mapear opciones a estados
        estados = {"1": "Pendiente", "2": "En progreso", "3": "Completada", "4": "Cancelada"}
        if e in estados:  # Solo actualizamos si eligió una opción válida
            tarea["estado"] = estados[e]

        # Menú para cambiar la prioridad
        print("\n🎯 Cambiar prioridad:")
        print("1. Alta")
        print("2. Media")
        print("3. Baja")
        p = input("Elige (Enter para mantener): ").strip()
        
        prioridades = {"1": "Alta", "2": "Media", "3": "Baja"}
        if p in prioridades:
            tarea["prioridad"] = prioridades[p]

        print("\n✅ Tarea actualizada correctamente.")

    except ValueError:
        # Error si el usuario no ingresó un número válido
        print("❌ ID inválido.")
    except Exception as e:
        # Capturamos cualquier otro error
        print(f"❌ Error al editar: {e}")

def eliminar_tarea():
    """
    Elimina una tarea de la lista.
    Pide confirmación antes de eliminar para evitar borrados accidentales.
    """
    # Verificamos si hay tareas
    if not tareas:
        print("\n📋 No hay tareas para eliminar.")
        return

    # Mostramos todas las tareas
    mostrar_tareas()
    
    try:
        # Solicitamos el ID de la tarea a eliminar
        tarea_id = int(input("\n🔢 ID de la tarea a eliminar: "))
        
        # Buscamos la tarea
        tarea = next((t for t in tareas if t["id"] == tarea_id), None)
        
        if not tarea:
            print("❌ Tarea no encontrada.")
            return

        # Pedimos confirmación mostrando el nombre de la tarea
        confirmar = input(f"⚠️ ¿Eliminar '{tarea['nombre']}'? (s/n): ").lower()
        if confirmar == 's':
            # Eliminamos la tarea de la lista
            tareas.remove(tarea)
            print("✅ Tarea eliminada.")
        else:
            print("❌ Operación cancelada.")

    except ValueError:
        print("❌ ID inválido.")

def buscar_tareas():
    """
    Busca tareas que contengan un término específico en su nombre.
    La búsqueda no distingue entre mayúsculas y minúsculas.
    """
    termino = input("\n🔍 Buscar tarea: ").strip()
    if termino:
        # Reutilizamos la función mostrar_tareas pasando el término como filtro
        mostrar_tareas(filtro=termino)

def estadisticas():
    """
    Muestra estadísticas generales sobre las tareas:
    - Total de tareas
    - Distribución por estado (pendientes, en progreso, completadas)
    - Distribución por prioridad (alta, media, baja)
    """
    # Verificamos si hay tareas
    if not tareas:
        print("\n📋 No hay tareas para mostrar estadísticas.")
        return

    # Calculamos el total de tareas
    total = len(tareas)
    
    # Contamos tareas por estado usando list comprehension
    pendientes = len([t for t in tareas if t["estado"] == "Pendiente"])
    completadas = len([t for t in tareas if t["estado"] == "Completada"])
    en_progreso = len([t for t in tareas if t["estado"] == "En progreso"])
    
    # Contamos tareas por prioridad
    alta = len([t for t in tareas if t["prioridad"] == "Alta"])
    media = len([t for t in tareas if t["prioridad"] == "Media"])
    baja = len([t for t in tareas if t["prioridad"] == "Baja"])

    # Mostramos las estadísticas en formato de reporte
    print("\n" + "="*50)
    print("📊 ESTADÍSTICAS DE TAREAS")
    print("="*50)
    print(f"Total de tareas: {total}")
    
    print(f"\n📈 Por estado:")
    # Calculamos porcentajes dividiendo entre el total
    print(f"  ⏳ Pendientes: {pendientes} ({pendientes/total*100:.1f}%)")
    print(f"  🔄 En progreso: {en_progreso} ({en_progreso/total*100:.1f}%)")
    print(f"  ✅ Completadas: {completadas} ({completadas/total*100:.1f}%)")
    
    print(f"\n🎯 Por prioridad:")
    print(f"  🔴 Alta: {alta}")
    print(f"  🟡 Media: {media}")
    print(f"  🟢 Baja: {baja}")
    print("="*50)

def menu():
    """
    Muestra el menú principal con todas las opciones disponibles.
    """
    print("\n" + "="*50)
    print("  📋 TASK MANAGER OPEN SOURCE - VERSIÓN AVANZADA")
    print("="*50)
    print("1.  Ver todas las tareas")
    print("2.  Ver tareas pendientes")
    print("3.  Ver tareas completadas")
    print("4.  Agregar tarea")
    print("5.  Editar tarea")
    print("6.  Eliminar tarea")
    print("7.  Buscar tareas")
    print("8.  Estadísticas")
    print("9.  Guardar y salir")
    print("="*50)

def main():
    """
    Función principal que ejecuta el programa.
    Contiene el bucle principal que mantiene el programa funcionando
    hasta que el usuario decida salir.
    """
    print("🚀 Iniciando Task Manager...")
    
    # Cargamos las tareas al inicio
    cargar_tareas()
    
    # Bucle infinito - solo se rompe cuando el usuario elige salir
    while True:
        # Mostramos el menú
        menu()
        
        # Leemos la opción del usuario
        opcion = input("\n🎯 Elige una opción (1-9): ").strip()

        # Ejecutamos la función correspondiente según la opción elegida
        if opcion == "1":
            mostrar_tareas()  # Muestra todas las tareas
        elif opcion == "2":
            mostrar_tareas(filtro="pendientes")  # Solo pendientes
        elif opcion == "3":
            mostrar_tareas(filtro="completadas")  # Solo completadas
        elif opcion == "4":
            agregar_tarea()  # Agrega nueva tarea
        elif opcion == "5":
            editar_tarea()  # Edita tarea existente
        elif opcion == "6":
            eliminar_tarea()  # Elimina tarea
        elif opcion == "7":
            buscar_tareas()  # Busca tareas por término
        elif opcion == "8":
            estadisticas()  # Muestra estadísticas
        elif opcion == "9":
            # Guardamos las tareas antes de salir
            guardar_tareas()
            print("\n💾 Datos guardados. ¡Hasta luego! 👋")
            break  # Rompemos el bucle para salir del programa
        else:
            # Opción no válida
            print("❌ Opción no válida. Intenta de nuevo.")

# Punto de entrada del programa
# Este bloque solo se ejecuta si el archivo se ejecuta directamente
# (no si se importa como módulo)
if __name__ == "__main__":
    main()