from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from artistsIngestion import ingester

INTERVAL_OF_UPDATE = 1 # in minute

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(ingester.update_artists, 'interval', minutes=INTERVAL_OF_UPDATE)
    scheduler.start()
