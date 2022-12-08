# not tests, just Django settings
SECRET_KEY = "test"
INSTALLED_APPS = (
    "opencivicdata.core.apps.BaseConfig",
    "opencivicdata.legislative.apps.BaseConfig",
    "opencivicdata.elections.apps.BaseConfig",
)
DATABASES = {
    "default": {
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        "NAME": "test",
        "USER": "test",
        "PASSWORD": "test",
        "HOST": "localhost",
    }
}
MIDDLEWARE_CLASSES = ()
