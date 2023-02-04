from os import getenv
from dao.weather_forecast_dao import WeatherForecastDAO
from mailer.weather_report_mailer import WeatherReportMailer


class ForecastReportService:
    def __init__(self):
        self.weather_forecast_dao = WeatherForecastDAO()
        self.mailer = WeatherReportMailer()

    def send_report(self):
        weather_forecast_list = self.weather_forecast_dao.find_all()
        weather_forecast_filtered = filter(self.filter_thresholds, weather_forecast_list)

        self.mailer.send_email(weather_forecast_filtered)

    def filter_thresholds(self, weather_forecast):
        if weather_forecast.min_temp <  getenv('MIN_TEMP') and weather_forecast.max_temp > getenv('MAX_TEMP') and weather_forecast.precipitation > getenv('PRECIPITAION'):
            return True
        return False
