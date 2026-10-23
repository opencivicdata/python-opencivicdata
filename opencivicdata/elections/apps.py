from django.apps import AppConfig
import os


class BaseConfig(AppConfig):
    name = "opencivicdata.elections"
    verbose_name = "Open Civic Data - Elections"
    path = os.path.dirname(__file__)
    default_auto_field = "django.db.models.AutoField"
