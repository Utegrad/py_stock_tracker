"""
Django settings for py_stock_tracker project.

"""

import os
import environ

ROOT_DIR = environ.Path(__file__) - 3 # (py_stock_tracker/config/settings/base.py - 3 = py_stock_tracker/)
env = environ.Env(DEBUG=(bool, False),)
env.read_env()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = ROOT_DIR()


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

ALLOWED_HOSTS = []

DEBUG_TOOLBAR_PATCH_SETTINGS = False