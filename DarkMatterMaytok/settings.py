"""
Django settings for DarkMatterMaytok project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
from decouple import config

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY', default='SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True, cast=bool)

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django_comments_xtd',
    'django_comments',
    'payments.apps.PaymentsConfig',
    'core.apps.CoreConfig',
    'blog.apps.BlogConfig',
    'books.apps.BooksConfig',
    'wallet.apps.WalletConfig',
    'wiki.apps.WikiConfig',
    'rest_framework',
    'mptt',
    'drf_yasg',
    'corsheaders',
    'django_summernote',
    'social_django',
    'compressor',
    'dbbackup',
    'minio_storage',
    'django_json_widget',
    'martor',
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
]

ROOT_URLCONF = 'DarkMatterMaytok.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
                'core.context_processors.maytok_context'
            ],
        },
    },
]

WSGI_APPLICATION = 'DarkMatterMaytok.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DATABASE_NAME', default='mark2'),
        'USER': config('DATABASE_USER', default='mark2'),
        'PASSWORD': config('DATABASE_PASSWORD', default='mark2'),
        'HOST': config('DATABASE_HOST', default='localhost'),
        'PORT': config('DATABASE_PORT', default=''),
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'es-PE'

TIME_ZONE = 'America/Lima'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static/")

MEDIA_URL = '/uploads/'
MEDIA_ROOT = os.path.join(BASE_DIR, "uploads/")

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny'
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 100
}

CULQI_PUBLIC_KEY = config('CULQI_PUBLIC_KEY', default='I+1PL;2>^^ITSZ}_g.N;vZ-w|zMNm$S6H2~^-MCt#')
CULQI_PRIVATE_KEY = config('CULQI_PRIVATE_KEY', default='I+1PL;2>^O*L^c}_g.N;vZ-w|zMNm$S6H2~^-MCt#')

AUTH_USER_MODEL = 'core.User'

COMMENTS_APP = 'django_comments_xtd'
COMMENTS_XTD_MAX_THREAD_LEVEL = 1
COMMENTS_XTD_CONFIRM_EMAIL = True
SITE_ID = 3717

EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_HOST = config('EMAIL_HOST', default='EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT', default=587, cast=int)
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

CORS_ORIGIN_ALLOW_ALL = True

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "assets"),
    os.path.join(BASE_DIR, "build_books"),
]

X_FRAME_OPTIONS = 'SAMEORIGIN'
SOCIAL_AUTH_JSONFIELD_ENABLED = True

AUTHENTICATION_BACKENDS = [
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
]

SOCIAL_AUTH_FACEBOOK_KEY = config('SOCIAL_AUTH_FACEBOOK_KEY', default='SOCIAL_AUTH_FACEBOOK_KEY')
SOCIAL_AUTH_FACEBOOK_SECRET = config('SOCIAL_AUTH_FACEBOOK_SECRET', default='SOCIAL_AUTH_FACEBOOK_SECRET')
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'locale': 'es_ES',
    'fields': 'id, name, email'
}
SOCIAL_AUTH_FACEBOOK_API_VERSION = '5.0'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = config('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY', default='GOOGLE_OAUTH2_KEY')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = config('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET', default='GOOGLE_OAUTH2_SECRET')

SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
    'https://www.googleapis.com/auth/userinfo.email',
    'https://www.googleapis.com/auth/userinfo.profile'
]

LOGIN_REDIRECT_URL = '/'
SESSION_COOKIE_SECURE = config('SESSION_COOKIE_SECURE', default=False, cast=bool)
CSRF_COOKIE_SECURE = config('CSRF_COOKIE_SECURE', default=False, cast=bool)

COMPRESS_ENABLED = not DEBUG
COMPRESS_OFFLINE = True
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

CACHE_TTL = 60 * 60 * 24  # 24 hours

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    }
}

USER_RANK = [
    ('0', 'IRON'),
    ('1', 'BRONZE'),
    ('2', 'SILVER'),
    ('3', 'GOLD'),
    ('4', 'PLATINUM'),
    ('5', 'DIAMOND'),
    ('6', 'MASTER'),
    ('7', 'GRANDMASTER'),
    ('8', 'CHALLENGER'),
]

SUMMERNOTE_CONFIG = {
    'summernote': {
        'width': '100%',
    },
}

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.social_auth.associate_by_email',  # <--- enable this one
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)

DBBACKUP_STORAGE = 'storages.backends.dropbox.DropBoxStorage'
DBBACKUP_STORAGE_OPTIONS = {
    'oauth2_access_token': config('DROPBOX_TOKEN', default='DROPBOX_TOKEN'),
}
DBBACKUP_TMP_DIR = BASE_DIR
MINIO_STORAGE_ENDPOINT = config('MINIO_STORAGE_ENDPOINT', default='MINIO_STORAGE_ENDPOINT')
MINIO_STORAGE_ACCESS_KEY = config('MINIO_ACCESS_KEY', default='MINIO_ACCESS_KEY')
MINIO_STORAGE_SECRET_KEY = config('MINIO_SECRET_KEY', default='MINIO_SECRET_KEY')
MINIO_STORAGE_USE_HTTPS = True
MINIO_STORAGE_MEDIA_BUCKET_NAME = config('MINIO_STORAGE_MEDIA_BUCKET_NAME', default='MINIO_STORAGE_MEDIA_BUCKET')
MINIO_STORAGE_AUTO_CREATE_MEDIA_BUCKET = True

DEFAULT_FILE_STORAGE = "minio_storage.storage.MinioMediaStorage"
# STATICFILES_STORAGE = "minio_storage.storage.MinioStaticStorage"
"""
import logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}
"""

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SHOW_QUERIES = config('SHOW_QUERIES', cast=bool, default=False)
if SHOW_QUERIES is True:
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
            },
        },
        'root': {
            'handlers': ['console'],
            'level': 'WARNING',
        },
        'loggers': {
            'django.db': {
                'level': 'DEBUG',
                'handlers': ['console'],
            }
        },
    }

PAGE_SIZE = 7

LOG_TO_FILE = config('LOG_TO_FILE', cast=bool, default=False)

if LOG_TO_FILE is True:
    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "root": {"level": "INFO", "handlers": ["file"]},
        "handlers": {
            "file": {
                "level": "INFO",
                "class": "logging.FileHandler",
                "filename": "/var/log/django.log",
                "formatter": "app",
            },
        },
        "loggers": {
            "django": {
                "handlers": ["file"],
                "level": "INFO",
                "propagate": True
            },
        },
        "formatters": {
            "app": {
                "format": (
                    u"%(asctime)s [%(levelname)-8s] "
                    "(%(module)s.%(funcName)s) %(message)s"
                ),
                "datefmt": "%Y-%m-%d %H:%M:%S",
            },
        },
    }
