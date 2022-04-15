import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('SECRET_KEY')

APP_ENVIRONMENT = os.getenv('APP_ENVIRONMENT')

DEBUG = os.getenv('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS').split(' ')


# ['127.0.0.1',
#  'localhost',
#  'youreventhub.herokuapp.com',
#              ]

# Application definition
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'eventhub.user_auth',
    'eventhub.user_profile',
    'eventhub.main',
    'eventhub.categories',
]

EVENTHUB_APPS = [
    'django_cleanup.apps.CleanupConfig',
]

INSTALLED_APPS =  DJANGO_APPS + THIRD_PARTY_APPS + EVENTHUB_APPS



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'eventhub.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'eventhub.wsgi.application'


# Database

DATABASES = None
if APP_ENVIRONMENT == 'Production':
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT', '5432'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'eventhub',
            'USER': 'user',
            'PASSWORD': 'password',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }



# Password validation

if APP_ENVIRONMENT == 'Production':
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
else:
    AUTH_PASSWORD_VALIDATORS = []

# Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = (
    BASE_DIR / 'static',
    )

#STATIC_URL = 'static/'
# if DEBUG:
#     STATICFILES_DIRS = (
#     BASE_DIR / 'static',
#     )
# else:
#     STATIC_ROOT = BASE_DIR / 'static'

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'mediafiles'

# Default primary key field type

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGOUT_REDIRECT_URL = 'home'

AUTH_USER_MODEL = 'user_auth.AppUser'
