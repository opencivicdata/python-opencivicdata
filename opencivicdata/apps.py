from django.apps import AppConfig
import os

class BaseConfig(AppConfig):
    name = 'opencivicdata'
    verbose_name = 'Open Civic Data'
    path = os.path.dirname(__file__)
