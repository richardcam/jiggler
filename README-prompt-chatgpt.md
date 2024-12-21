> Quiero crear un proyecto Python llamado Jiggler que simule el movimiento del ratón cada minuto para evitar que el sistema entre en modo de suspensión. Deseo que el proyecto cumpla las siguientes especificaciones:

**Funcionalidades**:

- **Contador de inactividad**: Implementar un contador que registre el tiempo transcurrido desde el último movimiento del ratón.
- **Movimiento del ratón**: Si transcurre un minuto sin detectar movimiento, el ratón se desplazará 25 píxeles hacia la derecha desde su posición actual.
- **Ambiente virtual**: Crear un ambiente virtual (venv o virtualenv) para aislar las dependencias del proyecto.
- **Gestión de paquetes**: Utilizar `pip freeze` para generar un archivo `requirements.txt` y `pip install -r requirements.txt` para instalar las dependencias.

**Estructura del proyecto:**

- **Carpeta**: Crear una carpeta principal llamada `jiggler-py`.
- **Archivo principal**: Dentro de la carpeta, crear un archivo Python llamado `py-jiggler.py` que contenga la lógica principal del programa.
- **Requisitos**: Especificar las librerías necesarias (por ejemplo, `pyautogui` para controlar el ratón) en el archivo `requirements.txt`.

**Comandos de creación**:

Proporciona los comandos de terminal para:

- Crear el ambiente virtual.
- Activar el ambiente virtual.
- Crear la estructura de carpetas y archivos.
- Instalar las dependencias.

**Consideraciones**:

- Plataforma: El proyecto se ejecutará en Linux Mint 22.
- Errores: Considerar posibles errores como:
    - El módulo `pyautogui` no está instalado.
    - El ratón no se mueve como se espera.
    - El contador de tiempo no funciona correctamente.
    - El ambiente virtual no se activa correctamente.

Código:

Proporciona un ejemplo de código en Python para el archivo py-jiggler.py, incluyendo:

- La importación de las librerías necesarias.
- La función principal que se encargue de controlar el movimiento del ratón.
- El bucle principal que monitoree la actividad del ratón y ejecute la función de movimiento.

Explicación:

Explica brevemente cada sección del código y las decisiones de diseño tomadas.