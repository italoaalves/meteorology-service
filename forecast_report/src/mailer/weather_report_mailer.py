from config.mailer import Mailer
from datetime import datetime

class WeatherReportMailer:
    def __init__(self):
        self.mailer = Mailer()

    def send_email(self, weather_report_list):
        body = self.load_view()

        ul_content = []
        for weather_report in weather_report_list:
            li =   (f'<li>'
                     '    <span>{weather_report.min_temp} graus</span>'
                     '    <span>{weather_report.max_temp} graus</span>'
                     '    <span>{weather_report.precipitation}%</span>'
                     '</li>')

            ul_content.append(li)

        self.mailer.send_email(f'Daily weather report for {str(datetime.now())}', body)

    def load_view(self):
        with open('./view/weather_report_mailer.html', 'r') as file:
            return file.read()
