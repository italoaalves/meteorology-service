from os import getenv
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger

scheduler = BlockingScheduler()
@scheduler.scheduled_job(CronTrigger(day_of_week=getenv('WEEK_INTERVAL'),
                                        hour=getenv('HOUR'),
                                        minute=getenv('MINUTE'),
                                        timezone=getenv('TIMEZONE')
                                    ))
def application():
    # Send message to scrapper
    # Receive db updated message
    # call project report service
    pass

scheduler.start()
