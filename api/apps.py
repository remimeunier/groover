from django.apps import AppConfig
from django.conf import settings

class ApiConfig(AppConfig):
    name = 'api'

    def ready(self):
        from artistsIngestion import scheduler
        scheduler.start()
