# Sistema de Gestión para Cmas GYM

Este proyecto es una página web desarrollada en Django que busca promover el gimnasio Cmas GYM, mostrando sus promociones y ofreciendo una plataforma de gestión de suscripciones. Los usuarios pueden crear una cuenta y acceder a planes de suscripción para aprovechar las instalaciones del gimnasio.

## Descripción

La plataforma permite:
- **Explorar el gimnasio**: Página principal con información del gimnasio y promociones.
- **Registro y autenticación**: Los usuarios pueden crear cuentas, iniciar sesión y acceder a opciones de suscripción.
- **Gestión de suscripciones**: Los usuarios registrados pueden suscribirse a los distintos planes ofrecidos por el gimnasio.

## Requisitos

- **Python 3.12** (junto con el framework Django)
- **Django**: Puedes instalarlo con `pip install django`.
- **Base de datos**: Supabase (PostgreSQL) para entornos en la nube, o MariaDB (XAMPP) para desarrollo local.

## Instalación

### Paso 1: Clonar el repositorio

```bash
git clone <url_del_repositorio>
cd <nombre_del_directorio>
```

### Paso 2: Crear un entorno virtual (opcional, pero recomendado)

```bash
python -m venv env
source env/bin/activate  # En Windows, usa `env\Scripts\activate`
```

### Paso 3: Instalar dependencias

```bash
pip install django psycopg2
```

### Paso 4: Configurar la Base de Datos

#### Para desarrollo local con XAMPP y MariaDB:

1. Asegúrate de que MariaDB esté activo en XAMPP.
2. Crea una base de datos para el sistema.
3. Configura las credenciales en el archivo `settings.py` de Django en la sección `DATABASES`:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'gimnasio',
           'USER': 'root',
           'PASSWORD': '',  # Añade tu contraseña si tienes una configurada en XAMPP
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
   ```

#### Para despliegue en la nube con Supabase:

1. Crea un proyecto en Supabase y configura la base de datos PostgreSQL.
2. Obtén las credenciales de acceso (nombre de la base de datos, usuario, contraseña, host y puerto).
3. Configura las credenciales en `settings.py` de Django:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': '<nombre_de_la_base>',
           'USER': '<usuario>',
           'PASSWORD': '<contraseña>',
           'HOST': '<host_de_supabase>',
           'PORT': '5432',
       }
   }
   ```

### Paso 5: Ejecutar migraciones para crear las tablas necesarias

```bash
python manage.py makemigrations
python manage.py migrate
```

### Paso 6: Iniciar el servidor de desarrollo

```bash
python manage.py runserver
```

Accede a la aplicación en [http://localhost:8000](http://localhost:8000).

## Comandos Principales

- `python manage.py runserver`: Inicia el servidor de desarrollo.
- `python manage.py makemigrations`: Detecta cambios en el modelo de datos.
- `python manage.py migrate`: Aplica migraciones a la base de datos.

## Autores

- Sebastián Vargas
- Ángel Rodríguez
- Vicente Cumillaf
- Matías Díaz