from decouple import config

from .base import *

DEBUG = False

ADMINS = [
    ('admin', 'admin@admin.com'),
]

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('POSTGRES_DB'),
        'USER': config('POSTGRES_USER'),
        'PASSWORD': config('POSTGRES_PASSWORD'),
        'HOST': 'db',
        'PORT': 5432,
    }
}

REDIS_URL = 'redis://ram_db:6379'
CHANNEL_LAYERS['default']['CONFIG']['hosts'] = [REDIS_URL]

MEMCACHED_URL = 'memcached://cache:11211'
CACHES['default']['LOCATION'] = MEMCACHED_URL
