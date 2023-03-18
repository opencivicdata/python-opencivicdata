import os

from django.apps import AppConfig


class BaseConfig(AppConfig):
    name = "opencivicdata.legislative"
    verbose_name = "Open Civic Data - Legislative"
    path = os.path.dirname(__file__)
