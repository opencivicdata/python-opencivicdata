import os

from django.apps import AppConfig


class BaseConfig(AppConfig):
    name = "opencivicdata.elections"
    verbose_name = "Open Civic Data - Elections"
    path = os.path.dirname(__file__)
