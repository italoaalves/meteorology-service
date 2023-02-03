
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger

from config.settings import SCHEDULER

scheduler = BlockingScheduler()
@scheduler.scheduled_job(CronTrigger(day_of_week=SCHEDULER['WEEK_INTERVAL'],
                                        hour=SCHEDULER['HOUR'],
                                        minute=SCHEDULER['MINUTE'],
                                        timezone=SCHEDULER['TIMEZONE']
                                    ))
def application():
    # Send message to scrapper
    # Receive db updated message
    # call project report service
    pass

scheduler.start()
