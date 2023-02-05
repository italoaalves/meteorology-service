from config.db import Db
from model.weather_forecast import WeatherForecast

class WeatherForecastDAO:
    def __init__(self):
        self.db = Db()
        self.table_name = "weather_forecasts"

    def find_all_by_start_date(self, date):
        db_list = self.db.execute(f'SELECT * FROM `{self.table_name}` WHERE date >= %s', (date,)).fetchall()
        return [WeatherForecast(*element) for element in db_list]
