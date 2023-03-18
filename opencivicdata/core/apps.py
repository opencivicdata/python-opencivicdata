import os

from django.apps import AppConfig


class BaseConfig(AppConfig):
    name = "opencivicdata.core"
    verbose_name = "Open Civic Data - Core"
    path = os.path.dirname(__file__)
