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

DATABASES = {
    'default': {
        'ENGINE'  : 'django.db.backends.mysql',
        'NAME'    : get_env_variable("DB_NAME"),    #'squashire_db',
        'USER'    : get_env_variable("DB_USER"),    #'diego',
        'PASSWORD': get_env_variable("DB_PASSWORD"),
    }
}
