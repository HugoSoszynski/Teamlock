#!/usr/bin/python

"""This file is part of Teamlock.

Teamlock is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Teamlock is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Teamlock.  If not, see <http://www.gnu.org/licenses/>."""

__author__ = "Olivier de Régis"
__credits__ = []
__license__ = "GPLv3"
__version__ = "3.0.0"
__maintainer__ = "Teamlock Project"
__email__ = "contact@teamlock.io"
__doc__ = ''

import os

"""
Django settings for Teamlock project.

Generated by 'django-admin startproject' using Django 1.11.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
try:
    from Teamlock.secret_key import SECRET_KEY
# File doesn't exist, we need to create it
except ImportError:
    from django.utils.crypto import get_random_string

    SETTINGS_DIR = os.path.abspath(os.path.dirname(__file__))
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    secret_key = get_random_string(50, chars)

    with open(os.path.join(SETTINGS_DIR, 'secret_key.py'), 'w') as f:
        f.write("SECRET_KEY = '{}'\n".format(secret_key))

    from Teamlock.secret_key import SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
DEBUG_LEVEL = "INFO"
DEV_MODE = False

ALLOWED_HOSTS = ["*"]

REDIS_HOST = "<redis_ip>"
REDIS_PORT = 6379

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',
    'gui',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'gui.middlewares.auth.AuthenticationMiddleware',
]

ROOT_URLCONF = 'Teamlock.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'Teamlock.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '<db_name>',
        'HOST': '<db_host>',
        'PORT': 5432,
        'USER': '<db_user>',
        'PASSWORD': '<db_password>'
    }
}

AUTHENTICATION_BACKENDS = (
    'teamlock_toolkit.auth.AuthenticationBackend',
)

# AUTH_LDAP_USER_FLAGS_BY_GROUP = {
#     'is_active': 'cn=active,ou=users,ou=groups,dc=example,dc=org',
#     'is_staff': 'cn=staff,ou=users,ou=groups,dc=example,dc=org',
#     'is_superuser': 'cn=superuser,ou=users,ou=groups,dc=example,dc=org',
# }

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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

LOGIN_URL = "/login/"
AUTH_USER_MODEL = 'gui.TeamlockUser'

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


LOG_SETTINGS = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        "console": {
            "class": "logging.StreamHandler"
        },
        'file': {
            'level': DEBUG_LEVEL,
            'class': 'logging.FileHandler',
            'filename': '/var/log/teamlock/debug.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file', 'console'],
            'level': DEBUG_LEVEL,
            'propagate': True,
        },

        'auth': {
            'handlers': ['file', 'console'],
            'level': DEBUG_LEVEL,
            'propagate': True
        },

        'workspace': {
            'handlers': ['file', 'console'],
            'level': DEBUG_LEVEL,
            'propagate': True
        }
    },
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

SESSION_ENGINE = 'redis_sessions.session'
SESSION_COOKIE_AGE = 7200

SESSION_REDIS = {
    'host': REDIS_HOST,
    'port': REDIS_PORT,
    'db': 0,
    'prefix': 'teamlock_session',
}

STATIC_URL = '/static/'

PUBLIC_URI = "<https://demo.teamlock.io>"
