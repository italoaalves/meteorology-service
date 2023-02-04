from os import getenv
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.interval import IntervalTrigger
from service.weather_scraper_service import WeatherScraperService

scheduler = BlockingScheduler()
@scheduler.scheduled_job(IntervalTrigger(hours=int(getenv('DB_UPDATE_INTERVAL'))))
def application():
    WeatherScraperService().run()

# When starting always update
WeatherScraperService().run()

scheduler.start()
