from . base import *
BASE_DIR = os.path.join(BASE_DIR)
SECRET_KEY = 'r+jan1w%a-!(96k2gb9hf8fn(g08t8gclx#_g-6y)6!pen)_4%'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '../../db.sqlite3'),
    }
}
