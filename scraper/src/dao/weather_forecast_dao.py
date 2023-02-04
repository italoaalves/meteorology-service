from datetime import datetime

from config.db import Db
from model.weather_forecast import WeatherForecast

class WeatherForecastDAO:
    def __init__(self):
        self.db = Db()
        self.table_name = "weather_forecasts"

        query = f'''CREATE TABLE IF NOT EXISTS `{self.table_name}` (
                        `id`            int(11)    NOT NULL AUTO_INCREMENT PRIMARY KEY,
                        `date`          DATE       NOT NULL,
                        `date_slug`     varchar(8) NOT NULL,
                        `min_temp`      INTEGER    NOT NULL,
                        `max_temp`      INTEGER    NOT NULL,
                        `precipitation` FLOAT      NOT NULL,
                        `timestamp`     DATETIME
                        )
                    ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin AUTO_INCREMENT=1 ;'''

        self.db.execute(query)

    def create(self, weather_forecast):
        query = f'INSERT INTO {self.table_name} (date, date_slug, min_temp, max_temp, precipitation, timestamp) VALUES (%s, %s, %s, %s, %s, %s)'
        values = (weather_forecast.date, weather_forecast.date_slug, weather_forecast.min_temp, weather_forecast.max_temp, weather_forecast.precipitation, datetime.now())
        return self.db.execute(query, values)

    def exists_by_date_slug(self, date_slug):
        return self.db.execute(f'SELECT id FROM {self.table_name} WHERE date_slug=%s', (date_slug,)).fetchone() != None

    def update(self, weather_forecast):
        query = f'UPDATE {self.table_name} SET min_temp = %s, max_temp = %s, precipitation = %s, timestamp = %s WHERE date_slug=%s'
        values = (weather_forecast.min_temp, weather_forecast.max_temp, weather_forecast.precipitation, datetime.now(), weather_forecast.date_slug)
        return self.db.execute(query, values)
