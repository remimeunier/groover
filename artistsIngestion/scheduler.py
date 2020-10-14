from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from artistsIngestion import ingester

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(ingester.update_artists, 'interval', minutes=1)
    scheduler.start()
