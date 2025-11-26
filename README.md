# taskmanager-open-source
Sistema avanzado de gestión de tareas desarrollado en Python con interfaz de línea de comandos.

Descripción:
TaskManager es un sistema completo de gestión de tareas diseñado para ayudar a usuarios a organizar, priorizar y dar seguimiento a sus tareas diarias. Desarrollado en Python puro sin dependencias externas, ofrece una interfaz de línea de comandos intuitiva y potente con funcionalidades avanzadas como categorización, etiquetado, búsqueda y estadísticas de productividad.
El proyecto surge como una solución práctica para la gestión personal y profesional de tareas, implementando conceptos de programación orientada a funciones, manejo de archivos JSON y diseño de interfaces de usuario en consola.

Características:

Gestión completa de tareas: Crear, editar, eliminar y listar tareas
Sistema de prioridades: Alta, Media y Baja con indicadores visuales
Categorización: Organiza tus tareas por categorías (Trabajo, Personal, Estudios, etc.)
Etiquetas: Añade múltiples etiquetas a cada tarea para mejor organización
Fechas de vencimiento: Establece fechas límite para tus tareas
Búsqueda avanzada: Encuentra tareas rápidamente por nombre
Estadísticas: Visualiza tu productividad con reportes detallados
Persistencia de datos: Todas tus tareas se guardan automáticamente en formato JSON
Estados múltiples: Pendiente, En progreso, Completada, Cancelada
Soporte UTF-8: Acentos y caracteres especiales sin problemas

Requisitos del Sistema:

Python 3.7 o superior
Sistema operativo: Windows, macOS o Linux
Espacio en disco: ~1 MB
No requiere instalación de librerías externas (solo módulos estándar de Python)

Instalación:

1.-Descarga el archivo ZIP desde GitHub
2.-Descomprime el archivo en tu computadora
3.-Abre una terminal en la carpeta descomprimida
4.-Ejecuta: python main.py

Verificación de instalación
Para verificar que Python está instalado correctamente:
python --version
Deberías ver algo como: Python 3.7.x o superior.


Inicio rápido

Ejecuta el programa:

bash   python main.py

Verás el menú principal:

   ==================================================
     📋 TASK MANAGER OPEN SOURCE
   ==================================================
   1.  Ver todas las tareas
   2.  Ver tareas pendientes
   3.  Ver tareas completadas
   4.  Agregar tarea
   5.  Editar tarea
   6.  Eliminar tarea
   7.  Buscar tareas
   8.  Estadísticas
   9.  Guardar y salir
   ==================================================

Selecciona una opción escribiendo el número y presionando Enter

Guía de uso detallada
📝 Agregar una tarea

Selecciona opción 4 en el menú
Ingresa los datos solicitados:

   📝 Nombre de la tarea: Completar informe mensual
   📄 Descripción: Preparar informe de ventas de noviembre
   🎯 Prioridad: 1 (Alta)
   📂 Categoría: Trabajo
   🏷️ Etiquetas: urgente, informe
   📅 Fecha de vencimiento: 30/11/2025
📋 Ver tareas

Opción 1: Ver todas las tareas con todos sus detalles
Opción 2: Ver solo tareas pendientes (filtrado automático)
Opción 3: Ver solo tareas completadas

Las tareas se muestran con indicadores visuales:

🔴 Prioridad Alta
🟡 Prioridad Media
🟢 Prioridad Baja
✅ Completada
⏳ Pendiente

✏️ Editar una tarea

Selecciona opción 5
Se mostrarán todas las tareas con sus IDs
Ingresa el ID de la tarea que deseas editar
Modifica los campos que necesites (presiona Enter para mantener el valor actual)

🗑️ Eliminar una tarea

Selecciona opción 6
Ingresa el ID de la tarea
Confirma la eliminación escribiendo s

🔍 Buscar tareas

Selecciona opción 7
Ingresa el término de búsqueda
Se mostrarán todas las tareas que contengan ese término en su nombre

📊 Ver estadísticas
Selecciona opción 8 para ver:

Total de tareas
Distribución por estado (con porcentajes)
Distribución por prioridad

📄 Licencia
Este proyecto está licenciado bajo la MIT License - una de las licencias open source más permisivas.
¿Qué significa esto?
✅ Puedes:

Usar el código comercialmente
Modificar el código como desees
Distribuir el código original o modificado
Usar el código de forma privada
Sublicenciar bajo otros términos

📋 Solo debes:

Incluir el aviso de copyright y la licencia en todas las copias

⚠️ Ten en cuenta:

El software se proporciona "tal cual", sin garantías
Los autores no son responsables por daños derivados del uso

Ver el archivo LICENSE para el texto completo de la licencia.
¿Por qué elegí MIT?
Elegí la licencia MIT porque:

Máxima libertad: Permite que cualquiera use, modifique y aprenda del código
Simplicidad: Fácil de entender, sin términos legales complicados
Educación: Ideal para proyectos académicos y de aprendizaje
Compatibilidad: Compatible con casi todas las demás licencias
Fomenta colaboración: Sin barreras para contribuciones
