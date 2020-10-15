from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from artistsIngestion import ingester

INTERVAL_OF_UPDATE = 1 # in minute ; Set to 1 for dev purpose, change it for production

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(ingester.update_artists, 'interval', minutes=INTERVAL_OF_UPDATE)
    scheduler.start()
