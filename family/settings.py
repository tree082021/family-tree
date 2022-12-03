"""
Django settings for family project.

Generated by 'django-admin startproject' using Django 3.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

from django.conf import settings 
from django.urls import path, include 
from django.conf.urls.static import static

import os
import dj_database_url
db_from_env = dj_database_url.config()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-^@chv85^xzzvi+2x3k-hwzu9*zch5t%$4uxb$b_*fm31vb79mu'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'family-tree.onrender.com',]

# Application definition (Зарегистрированные приложегия)

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tree',
    'crispy_forms',
    'widget_tweaks',
    'django_cleanup',
    'cloudinary_storage',
    'cloudinary',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',    
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

ROOT_URLCONF = 'family.urls'

# Создать в корневой папке проекта новый каталог templates.
# Указать, что этот каталог будет использоваться в качестве хранилища шаблонов в переменной TEMPLATES
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR,],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'family.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    #'default': {
    #    'ENGINE': 'django.db.backends.sqlite3',
    #    'NAME': BASE_DIR / 'db.sqlite3',
    #}
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'family',
        'USER' : 'customer',
        'PASSWORD' : 'customer',
        'HOST' : '127.0.0.1',
        'PORT' : '5432',
    }
    #'default': {
    #    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #    'NAME': 'd6so58ed0ubvft',
    #    'USER' : 'vcdnszipvdpfnz',
    #    'PASSWORD' : 'c3f7bd848b7ab7daf5e1f5be522d4cf72f16f12f83b0b15bf2b55b54b8ed1c00',
    #    'HOST' : 'ec2-44-196-170-156.compute-1.amazonaws.com',
    #    'PORT' : '5432',
    #}
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'ru-Ru'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale')]

LANGUAGES = (
    ('kk', 'Kazakh'),
    ('ru', 'Russian'),    
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

#DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


#STATICFILES_DIRS = [
#    os.path.join(BASE_DIR, "static"),
#]

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/ static /'
#STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# MEDIA_ROOT - это абсолютный путь файловой системы к каталогу для загруженных пользователем файлов.
# MEDIA_URL - это URL-адрес, который можно использовать в наших шаблонах для файлов.
# Папку media необходимо создать в корневой папке проекта
#MEDIA_URL = '/ media /'
#MEDIA_ROOT = os.path.join (BASE_DIR, 'media')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media').replace('\\', '/')
MEDIA_URL = '/media/'

# Redirect to home URL after login (Default redirects to /accounts/profile/)
# Теперь, при входе в систему, вы по умолчанию должны перенаправляться на домашнюю страницу сайта а не на /accounts/profile/
LOGIN_REDIRECT_URL = '/'

# Сохранения изображения
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'haqtawlor',
    'API_KEY': '525581322115357',
    'API_SECRET': 'EI5OU9eSuJCIZpiN5scQoKvAQcc',
}
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# Отправка почты
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.mail.ru'
EMAIL_HOST_USER = 'tree082021@mail.ru' 
EMAIL_HOST_PASSWORD = 'dnCjumszgNEcXzhwF2Ss'
DEFAULT_FROM_EMAIL  = 'tree082021@mail.ru'
EMAIL_PORT = 25
EMAIL_USE_TLS = True

LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/login/'
