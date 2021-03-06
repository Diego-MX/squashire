"""
Django settings for squashire project.

Ge  nerated by 'django-admin startproject' using Django 1.8.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from os.path import dirname, abspath
from django.core.exceptions import ImproperlyConfigured
from django.utils.translation import ugettext_lazy as _


def get_env_variable(var_name):
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the %s environment variable" % var_name
        raise ImproperlyConfigured(error_msg)


BASE_DIR = dirname(dirname(dirname(abspath(__file__))))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_env_variable('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

# ALLOWED_HOSTS = []


# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)
# For ALLAUTH
INSTALLED_APPS += (
    # The Django sites framework is required
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # Squash Apps
    'squashire.apps.game_manager',
    # Login via Google
    'allauth.socialaccount.providers.google',
)


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    # included for locale settings.
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
)

ROOT_URLCONF = 'squashire.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "squashire/templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # Internationalization.
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                # Required by allauth template tags
                "django.core.context_processors.request",
              # allauth specific context processors
              # Eventually commented because of ALLAUTH version.
              # http://stackoverflow.com/questions/31648019/no-module-named-allauth-account-context-processors
            #   "allauth.account.context_processors.account",
            #   "allauth.socialaccount.context_processors.socialaccount",
            ],
        },
    },
]


WSGI_APPLICATION = 'squashire.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

#DATABASES = {
    #'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    #}
#}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en_us'

LANGUAGES = (
    ('en',    _('English')),
    ('es-mx', _('Spanish (Mexico)')),
)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, '/squashire/locale'),
)

TIME_ZONE = 'America/Mexico_City'
USE_I18N  = True
USE_L10N  = True
USE_TZ    = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

#STATICFILES_DIRS = (
    # Location of your application should not be public web accessible.
    # os.path.join(BASE_DIR, "../../static"),
# )

STATIC_ROOT = os.path.join(BASE_DIR, '../static')


# These variables are needed to run ALLAUTH with Google.
AUTHENTICATION_BACKENDS = (
    # Default backend -- used to login by username in Django admin
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)

# Also Google authentication
SITE_ID                     = 1
ACCOUNT_USERNAME_REQUIRED   = False
ACCOUNT_EMAIL_VERIFICATION  = "none"
SOCIALACCOUNT_QUERY_EMAIL   = True
LOGIN_REDIRECT_URL          = "/"
