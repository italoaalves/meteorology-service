from os import getenv
from datetime import date, datetime

from dao.weather_forecast_dao import WeatherForecastDAO
from mailer.weather_report_mailer import WeatherReportMailer

class ForecastReportService:
    def __init__(self):
        self.weather_forecast_dao = WeatherForecastDAO()
        self.mailer = WeatherReportMailer()

    def send_report(self):
        weather_forecast_list = self.weather_forecast_dao.find_all_by_start_date(datetime.now().date())
        weather_forecast_filtered = filter(self.filter_thresholds, weather_forecast_list)

        self.mailer.send_email(weather_forecast_filtered)

    def filter_thresholds(self, weather_forecast):
        if weather_forecast.min_temp <=  int(getenv('MIN_TEMP')) or weather_forecast.max_temp >= int(getenv('MAX_TEMP')) or weather_forecast.precipitation >= float(getenv('PRECIPITATION')):
            return True
        return False
