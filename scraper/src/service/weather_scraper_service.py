import requests
from os import getenv
from bs4 import BeautifulSoup

from datetime import datetime

from dao.weather_forecast_dao import WeatherForecastDAO
from model.weather_forecast import WeatherForecast


HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
    "Accept": "text/html",
    "wc-locale-group": "BR",
    "Accept-Language": "pt-BR",
    "Accept-Encoding": "gzip, deflate",
}

class WeatherScraperService:
    def __init__(self):
        self.weather_forecast_dao = WeatherForecastDAO()

    def run(self):
        response = requests.get(getenv('WEATHER_PROVIDER'), headers= HEADERS)
        page = BeautifulSoup(response.content, 'html.parser')

        weather_list = page.find('div', attrs={'class': 'DailyForecast--DisclosureList--nosQS'})
        daily_weather = weather_list.find_all('summary', attrs={'class': 'Disclosure--Summary--3GiL4'})

        for day in daily_weather[1:]:
            try:
                max_temp = int(day.find('span', attrs={'class': 'DetailsSummary--highTempValue--3PjlX'}).text[:-1])
                min_temp = int(day.find('span', attrs={'class': 'DetailsSummary--lowTempValue--2tesQ'}).text[:-1])
                precipitation_div = day.find('div', attrs={'class': 'DetailsSummary--precip--1a98O'})
                precipitation = float(precipitation_div.find('span', attrs={'data-testid': 'PercentageValue'}).text[:-1])/100

                day_number = int(day.find('h3', attrs={'class': 'DetailsSummary--daypartName--kbngc'}).text.split()[-1])
                date = datetime.now()
                date = date.replace(day=day_number)

                weather_forecast = WeatherForecast(date, min_temp, max_temp, precipitation)
                self.weather_forecast_dao.create(weather_forecast)
            except ValueError as e:
                print(e)

