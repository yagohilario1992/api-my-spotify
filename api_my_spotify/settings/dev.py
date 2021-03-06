from base import *

DEBUG = True

ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Celery
# CELERY_ALWAYS_EAGER = True
BROKER_URL = "redis://localhost:6379/0"
CELERY_RESULT_BACKEND = "redis://"
CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },

    'handlers': {
        'log_file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, '../my_spotify.log'),
            'maxBytes': 1024 * 1024 * 5,
            'formatter': 'verbose',
        },
        'null': {
            'class': 'django.utils.log.NullHandler',
        },
    },

    'loggers': {
        'django.request': {
            'handlers': ['log_file'],
            'propagate': True,
            'level': 'DEBUG',
        },
        'django': {
            'handlers': ['null', ],
        },
        'nomad_app': {
            'handlers': ['log_file'],
            'level': 'DEBUG',
        },
    }
}
