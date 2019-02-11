from .common import *

DEBUG = env.bool('DJANGO_DEBUG', default=True)

SECRET_KEY = env('SECRET_KEY')

DATABASES = {'default': env.db(), }

INTERNAL_IPS = env('INTERNAL_IPS')

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Boise'

USE_I18N = True

USE_L10N = True

USE_TZ = True
