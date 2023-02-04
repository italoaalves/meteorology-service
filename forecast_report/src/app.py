from os import getenv
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger

from service.forecast_report_service import ForecastReportService

scheduler = BlockingScheduler()
@scheduler.scheduled_job(CronTrigger(day_of_week=getenv('WEEK_INTERVAL'),
                                        hour=getenv('HOUR'),
                                        minute=getenv('MINUTE'),
                                        timezone=getenv('TIMEZONE')
                                    ))
def application():
    forecast_report_service = ForecastReportService()
    forecast_report_service.send_report()

scheduler.start()
