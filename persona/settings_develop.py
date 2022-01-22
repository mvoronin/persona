from pathlib import Path

from . import settings_generic

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-pehts3pz(002y%62^puolfalr6zsarv*&wwltzhi!r&=artrs0'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = settings_generic.INSTALLED_APPS

MIDDLEWARE = settings_generic.MIDDLEWARE

ROOT_URLCONF = settings_generic.ROOT_URLCONF

TEMPLATES = settings_generic.TEMPLATES

WSGI_APPLICATION = settings_generic.WSGI_APPLICATION

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_USER_MODEL = settings_generic.AUTH_USER_MODEL

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.ScryptPasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
]

AUTH_PASSWORD_VALIDATORS = settings_generic.AUTH_PASSWORD_VALIDATORS

LANGUAGE_CODE = settings_generic.LANGUAGE_CODE
TIME_ZONE = settings_generic.TIME_ZONE
USE_I18N = settings_generic.USE_I18N
USE_L10N = settings_generic.USE_L10N
USE_TZ = settings_generic.USE_TZ

STATIC_URL = settings_generic.STATIC_URL
STATICFILES_DIRS = [
    ("css", BASE_DIR / "static/css"),
    ("css", BASE_DIR / "static/css3p"),
    ("js", BASE_DIR / "static/js"),
    ("fonts", BASE_DIR / "static/fonts"),
    ("img", BASE_DIR / "static/img"),
]
STATIC_ROOT = BASE_DIR / "static/production"

DEFAULT_AUTO_FIELD = settings_generic.DEFAULT_AUTO_FIELD
