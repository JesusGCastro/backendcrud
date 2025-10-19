#!/usr/bin/env bash
# build.sh

# Instalar dependencias
pip install -r requirements.txt

# Aplicar migraciones
python manage.py migrate

# Crear superusuario automáticamente (solo si no existe)
echo "from django.contrib.auth import get_user_model; \
User = get_user_model(); \
import os; \
username = os.environ.get('DJANGO_SUPERUSER_USERNAME'); \
email = os.environ.get('DJANGO_SUPERUSER_EMAIL'); \
password = os.environ.get('DJANGO_SUPERUSER_PASSWORD'); \
if username and not User.objects.filter(username=username).exists(): \
    User.objects.create_superuser(username=username, email=email, password=password)" | python manage.py shell

# Recoger archivos estáticos
python manage.py collectstatic --noinput
