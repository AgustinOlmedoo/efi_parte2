# Sistema de Gestión para una Concesionaria de Autos

Este documento incluye los pasos y comandos necesarios para configurar, instalar y ejecutar el sistema de gestión de una concesionaria de autos en Django. A continuación, encontrarás las instrucciones para clonar el repositorio, configurar el entorno, instalar las dependencias y realizar otras tareas esenciales.

### Comandos de Instalación y Configuración

1. **Clona el repositorio en la ubicación que desees:**
    ```bash
    git clone git@github.com:AgustinOlmedoo/efi_parte2.git
    ```

2. **Accede a la carpeta del proyecto:**
    ```bash
    cd concesionaria
    ```

3. **Crea un entorno virtual:**
    ```bash
    python3 -m venv env
    ```

4. **Activa el entorno virtual:**
    ```bash
    source env/bin/activate
    ```

5. **Navega a la carpeta principal del proyecto:**
    ```bash
    cd concesionaria
    ```

6. **Instala las dependencias necesarias:**
    ```bash
    pip install -r requirements.txt
    ```

7. **Ejecuta las migraciones para crear las tablas en la base de datos:**
    ```bash
    python3 manage.py migrate
    ```

8. **Carga los datos iniciales en la base de datos:**
    ```bash
    python3 manage.py load_data
    ```

9. **Crea un superusuario para acceder al panel de administración:**
    ```bash
    python3 manage.py createsuperuser --username <nombre de tu usuario>
    ```

10. **Inicia el servidor de desarrollo:**
    ```bash
    python3 manage.py runserver
    ```

11. **Compila los archivos de idioma:**
    ```bash
    django-admin compilemessages
    ```

### Documentación de la API

- **Para consultar la información retornada por cada endpoint, visita:**
    ```plaintext
    http://127.0.0.1:8000/swagger/
    ```

