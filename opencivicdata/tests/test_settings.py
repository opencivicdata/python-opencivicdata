# not tests, just Django settings
SECRET_KEY = 'test'
INSTALLED_APPS = ('opencivicdata',)
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'test',
        'USER': 'test',
        'PASSWORD': 'test',
        'HOST': 'localhost',
    }
}
MIDDLEWARE_CLASSES = ()
