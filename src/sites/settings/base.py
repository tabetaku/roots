import logging
import os

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
from sentry_sdk.integrations.excepthook import ExcepthookIntegration
from sentry_sdk.integrations.logging import LoggingIntegration

from infras.secrets.constants import SecretKey
from libs.log.sentry import before_send
from libs.secrets.secrets import Secrets

BASE_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ROOT_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
MOUNT_PATH = os.path.join(ROOT_PATH, 'mount')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = Secrets.get(SecretKey.SECRET_KEY)

DEBUG = False

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',

    # Apps
    'apps.domains.hello_world',
    'apps.domains.metadata',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'libs.django.admin.middlewares.AdminIPRestrictorMiddleware',
    'csp.middleware.CSPMiddleware',
]

ROOT_URLCONF = 'sites.urls'
WSGI_APPLICATION = 'sites.wsgi.application'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_PATH, 'templates'), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
        },
    },
]

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'roots',
        'USER': Secrets.get(SecretKey.WRITE_DB_USER),
        'PASSWORD': Secrets.get(SecretKey.WRITE_DB_PASSWORD),
        'HOST': Secrets.get(SecretKey.WRITE_DB_HOST),
        'PORT': Secrets.get(SecretKey.WRITE_DB_PORT),
    }
}

# Password validation

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Security
CORS_ORIGIN_ALLOW_ALL = False
CORS_ALLOW_CREDENTIALS = True

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

X_FRAME_OPTIONS = 'DENY'

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

# CSP_DEFAULT_SRC = ("'self'", "'unsafe-inline'",)

# Admin
RESTRICT_ADMIN = False
ALLOWED_ADMIN_IPS = ['127.0.0.1', '::1', ]
ALLOWED_ADMIN_IP_RANGES = ['127.0.0.0/24', '192.168.0.0/16', '172.16.0.0/12', '::/1', ]
ALLOWED_ADMIN_PROXY_COUNT = 0
RESTRICTED_APP_NAMES = ['admin', ]
GRAPPELLI_ADMIN_TITLE = '도라마 루츠'

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_PATH, 'static/src', ),)
STATIC_ROOT = os.path.join(BASE_PATH, 'static/dist')

# Sentry
SENTRY_IGNORE_ERRORS = (OSError, )
sentry_sdk.init(
    dsn=Secrets.get(SecretKey.SENTRY_DSN), before_send=before_send,
    integrations=[DjangoIntegration(), ExcepthookIntegration(always_run=True), LoggingIntegration(logging.INFO, logging.ERROR), ]
)

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(MOUNT_PATH, 'media')
