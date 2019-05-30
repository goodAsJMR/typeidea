from .base import *  #NOQA

DEBUG = True

DATABASES = {
    'default': {

        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'students',
        'USER': 'root',
        'PASSWORD': 'superJmr2014',
        'HOST': 'localhost',
        'PORT': '3306',
    },
}
