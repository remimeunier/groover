from django.apps import AppConfig


class ApiConfig(AppConfig):
    name = 'api'

    def ready(self):
        from artistsIngestion import scheduler
        scheduler.start()
