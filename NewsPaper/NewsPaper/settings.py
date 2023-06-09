"""
Django settings for NewsPaper project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-qso#wt)05b((e0^smu_0ak8()cn&+6*gg&)tvucfa2#!hm$$z@'

DEBUG = True


ALLOWED_HOSTS = ['127.0.0.1']


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'django.contrib.flatpages',
    'django_filters',
    # The following apps are required:
    'django.contrib.auth',
    'django.contrib.messages',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    # 'allauth.socialaccount.providers.yandex',
    'news.apps.NewsConfig',
    # 'django_apscheduler',
    'sign',
    'protect',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]

# Указываем, куда будем сохранять кэшируемые файлы! Не забываем
# создать папку cache_files внутри папки с manage.py!
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
#         'LOCATION': os.path.join(BASE_DIR, 'cache_files'),
#     }
# }


ROOT_URLCONF = 'NewsPaper.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # allauth needs this
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

WSGI_APPLICATION = 'NewsPaper.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'ru-Ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

USE_L10N = True

DATE_INPUT_FORMATS = [
    "%d %b %Y",  # '25 Oct 2006'
    "%m/%d/%y",  # '10/25/06'
    "%Y-%m-%d",  # '2006-10-25'
    "%m/%d/%Y",  # '10/25/2006'
    "%b %d %Y",  # 'Oct 25 2006'
    "%b %d, %Y",  # 'Oct 25, 2006'
    "%d %b, %Y",  # '25 Oct, 2006'
    "%B %d %Y",  # 'October 25 2006'
    "%B %d, %Y",  # 'October 25, 2006'
    "%d %B %Y",  # '25 October 2006'
    "%d %B, %Y",  # '25 October, 2006'
    ]


APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"

APSCHEDULER_RUN_NOW_TIMEOUT = 25  # Seconds


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / "static"
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = '/news/'  # стрю., на которую перенаправляется
# пользователь после успешного входа на сайт, здесь корневая страница сайта
LOGIN_URL = '/accounts/login/'  # страница аутентификации


# для регистрации и входа по почте необходимы:
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_CONFIRM_EMAIL_ON_GET = False

ACCOUNT_FORMS = {'signup': 'sign.models.CommonSignupForm'}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = str(os.getenv("EMAIL_HOST"))
EMAIL_PORT = str(os.getenv("EMAIL_PORT"))
EMAIL_HOST_USER = str(os.getenv('EMAIL_HOST_USER'))
EMAIL_HOST_PASSWORD = str(os.getenv("EMAIL_HOST_PASSWORD"))
EMAIL_USE_SSL = True
# DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
# DEFAULT_FROM_EMAIL = str(os.getenv("DEFAULT_FROM_EMAIL"))


DEFAULT_FROM_EMAIL = EMAIL_HOST_USER + '@yandex.ru'  # если ya - + '@yandex.ru'

SERVER_EMAIL = EMAIL_HOST_USER + "@yandex.ru"
# SERVER_EMAIL = os.getenv("SERVER_EMAIL")
EMAIL_ADMIN = os.getenv("EMAIL_ADMIN")


# e-mail format !!!
# RECIPIENT_LIST = [(mail.split('|')[0], mail.split('|')[1]) for mail in os.getenv("RECIPIENT_LIST").split(',')]

ADMINS = [(em.split('|')[0], em.split('|')[1]) for em in os.getenv("ADMINS").split(',')]

# ADMINS = os.getenv("ADMINS")

# MANAGERS = [(manager.split('|')[0], manager.split('|')[1]) for manager in os.getenv("MANAGERS").split(',')]


# для отправки писем в консоль вместо реального мейла
if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# No 1
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '[%(asctime)s] %(levelname)-9s %(message)s'
        },
        'warning_email': {
            'format': '[%(asctime)s] %(levelname)-9s %(message)s %(pathname)s'
        },
        'error': {
            'format': '[%(asctime)s] %(levelname)-9s %(message)s %(pathname)s %(exc_info)s'
        },
        'general_security': {
            'format': '[%(asctime)s] %(levelname)-9s %(module)s: %(message)s'
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'general': {
            'level': 'INFO',
            'filters': ['require_debug_false'],  # *
            'class': 'logging.FileHandler',
            'formatter': 'general_security',
            'filename': 'general.log'
        },
        'error': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'formatter': 'error',
            'filename': 'errors.log'
        },
        'secure': {
            'class': 'logging.FileHandler',
            'formatter': 'general_security',
            'filename': 'security.log'
        },
        'admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],  # *
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'warning_email',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'general'],
            'level': 'INFO',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['error', 'admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.server': {
            'handlers': ['error', 'admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.template': {
            'handlers': ['error'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.db.backends': {
            'handlers': ['error'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.security': {
            'handlers': ['secure'],
            'propagate': True,
        },
    }
}