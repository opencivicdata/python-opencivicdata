from django.apps import AppConfig
import os


class BaseConfig(AppConfig):
    name = "opencivicdata.legislative"
    verbose_name = "Open Civic Data - Legislative"
    path = os.path.dirname(__file__)
