# -*- coding: utf-8 -*-
from .base import *
import os


def get_env_variable(var_name):
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the %s environment variable" % var_name
        raise ImproperlyConfigured(error_msg)

DEBUG = True

DB_PASSWORD = get_env_variable("DB_PASSWORD")

DATABASES = {
    'default': {
        'ENGINE'  : 'django.db.backends.mysql',
        'NAME'    : 'squashire_db',
        'USER'    : 'diego',
        'PASSWORD': DB_PASSWORD,
    }
}
