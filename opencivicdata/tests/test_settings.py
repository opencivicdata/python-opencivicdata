import os

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
        "NAME": os.getenv("POSTGRES_DB", "test"),
        "USER": os.getenv("POSTGRES_USER", "test"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD", "test"),
        "HOST": "localhost",
    }
}
MIDDLEWARE_CLASSES = ()
GDAL_LIBRARY_PATH = os.getenv("GDAL_LIBRARY_PATH")
GEOS_LIBRARY_PATH = os.getenv('GEOS_LIBRARY_PATH')
