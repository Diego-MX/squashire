# -*- coding: utf-8 -*-
from .base import *
import os


DEBUG = True

ALLOWED_HOSTS = ['stage.squashitlan.com']

DATABASES = {
    'default': {
        'ENGINE'  : 'django.db.backends.mysql',     # GET_ENV_VARIABLE form .BASE
        'NAME'    : get_env_variable("DB_NAME"),    #'squashire_db',
        'USER'    : get_env_variable("DB_USER"),    #'diego',
        'PASSWORD': get_env_variable("DB_PASSWORD"),
    }
}
