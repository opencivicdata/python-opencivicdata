# not tests, just Django settings
SECRET_KEY = "test"
INSTALLED_APPS = (
    "opencivicdata.core.apps.BaseConfig",
    "opencivicdata.legislative.apps.BaseConfig",
    "opencivicdata.elections.apps.BaseConfig",
)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "test",
        "USER": "test",
        "PASSWORD": "test",
        "HOST": "localhost",
    }
}
MIDDLEWARE_CLASSES = ()
