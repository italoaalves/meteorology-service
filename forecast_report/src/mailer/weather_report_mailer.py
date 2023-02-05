from config.mailer import Mailer
from datetime import datetime

class WeatherReportMailer:
    def __init__(self):
        self.mailer = Mailer()

    def send_email(self, weather_report_list):
        weather_forecast_tbody = ""
        for weather_forecast in weather_report_list:
            tr = (f'''<tr>
                        <td>{weather_forecast.date.strftime("%-d de %B")}</td>
                        <td>{weather_forecast.min_temp}°</td>
                        <td>{weather_forecast.max_temp}°</td>
                        <td>{(float(weather_forecast.precipitation) * 100):.1f}%</td>
                    </tr>
                ''')

            weather_forecast_tbody += '\n' + tr

        body = (f'''
                <!doctype html>
                <html lang="pt-br">
                    <head>
                        <meta charset="utf-8">
                        <style>
                            * {{box-sizing: border-box;}}
                            table {{text-align: left; border-spacing: 20px;}}
                        </style>
                    </head>
                    <body style="padding-top: 20px; text-align: center; background-color: #e2e0d5; font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;">
                        <h1 style="font-weight: normal; color: #222c3c;">Seu boletim diário de tempo chegou:</h1>
                        <p>Confira a tabela com os dias dentro dos filtros definidos.<p>
                        <div style="padding: 16px">
                            <table align="center" style="background-color: whitesmoke; padding: 16px; border-radius: 5px; width: 100%;">
                                <thead>
                                    <tr>
                                        <th>Dia</th>
                                        <th>Temp. Min</th>
                                        <th>Temp. Max</th>
                                        <th>Risco de chuva</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    {weather_forecast_tbody}
                                </tbody>
                            </table>
                        </div>

                    </body>
                </html>
        ''')
        self.mailer.send_email(f'Daily weather report for {str(datetime.now().strftime("%-d de %B"))}', body)

    def load_view(self):
        with open('./view/weather_report_mailer.html', 'r') as file:
            return file.read()
