from mysite.settings import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/
from django.conf.global_settings import CSRF_COOKIE_SECURE

from mysite.settings import INSTALLED_APPS

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure--)7qk0p$)xa5^6+&n71%kmp^1rs6+3-$@e0a#_jt6k9^&q-mz*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# INSTALLED_APPS = []

# sites framework
SITE_ID = 2


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

STATICFILES_DIRS = [
    BASE_DIR / "statics",
]

# CSRF_COOKIE_SECURE = True

X_FRAME_OPTIONS = 'SAMEORIGIN'