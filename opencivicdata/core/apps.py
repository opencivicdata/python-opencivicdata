from django.apps import AppConfig
import os


class BaseConfig(AppConfig):
    name = "opencivicdata.core"
    verbose_name = "Open Civic Data - Core"
    path = os.path.dirname(__file__)
    default_auto_field = "django.db.models.AutoField"
