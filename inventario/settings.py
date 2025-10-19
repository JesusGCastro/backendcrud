"""
Django settings for inventario project.
"""

from dotenv import load_dotenv
import os
from pathlib import Path
import dj_database_url  # ✅ nuevo: para leer la base de datos desde DATABASE_URL

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv()

# ⚠️ En producción, Render usa su propia URL y no deberías dejar DEBUG en True
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# Render asigna automáticamente el dominio de tu app, puedes permitirlo con:
ALLOWED_HOSTS = ['*']

# 🔐 En producción, deberías usar una variable de entorno
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-9gm@ifwl#cn7!n5slp=s)l!_j9e(*8e6q1c!6x$m%ndwptyo&2')

# ---------------------------------------------------------------------
# Apps
# ---------------------------------------------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'producto',
    'corsheaders',  # ✅ asegúrate de tener instalado django-cors-headers
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'inventario.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'inventario.wsgi.application'

# ---------------------------------------------------------------------
# Base de datos
# ---------------------------------------------------------------------
# ✅ Render crea una variable DATABASE_URL automáticamente
#    Ejemplo: postgres://usuario:contraseña@host:puerto/dbname

DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL'),
        conn_max_age=600,  # mantiene conexiones abiertas (optimiza performance)
        ssl_require=True   # Render requiere SSL
    )
}

# ---------------------------------------------------------------------
# Archivos estáticos (necesario para producción)
# ---------------------------------------------------------------------
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# ---------------------------------------------------------------------
# Otros ajustes
# ---------------------------------------------------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
]

# Permitir todo temporalmente (opcional para probar desde el front)
CORS_ALLOW_ALL_ORIGINS = True
