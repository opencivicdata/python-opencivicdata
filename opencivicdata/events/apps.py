from django.apps import AppConfig
import os


class BaseConfig(AppConfig):
    name = "opencivicdata.events"
    verbose_name = "Open Civic Data - Events"
    path = os.path.dirname(__file__)
