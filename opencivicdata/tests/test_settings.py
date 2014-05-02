# not tests, just Django settings
SECRET_KEY = 'test'
INSTALLED_APPS = ('opencivicdata',)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'testdb',
        'USER': 'test',
        'PASSWORD': 'test',
        'HOST': 'localhost',
    }
}
