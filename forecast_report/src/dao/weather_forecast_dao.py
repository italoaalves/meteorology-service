from db.Db import Db

class WeatherForecastDAO:
    def __init__(self):
        self.db = Db()
        self.table_name = "weather_forecasts"

    def list(self):
        return self.db.execute(f'SELECT * FROM `{self.table_name}`', None).fetchall()
