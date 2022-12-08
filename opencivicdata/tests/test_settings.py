# not tests, just Django settings
SECRET_KEY = "test"
INSTALLED_APPS = (
    "opencivicdata.core.apps.BaseConfig",
    "opencivicdata.legislative.apps.BaseConfig",
    "opencivicdata.elections.apps.BaseConfig",
)
GDAL_LIBRARY_PATH = '/opt/homebrew/Cellar/gdal/3.5.3_1/lib/libgdal.dylib'
GEOS_LIBRARY_PATH = '/opt/homebrew/Cellar/geos/3.11.1/lib/libgeos_c.dylib'
DATABASES = {
    "default": {
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        "NAME": "test",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "localhost",
    }
}
MIDDLEWARE_CLASSES = ()
