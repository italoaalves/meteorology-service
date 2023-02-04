from datetime import datetime

from config.db import Db
from model.weather_forecast import WeatherForecast

class WeatherForecastDAO:
    def __init__(self):
        self.db = Db()
        self.table_name = "weather_forecasts"

        query = f'''CREATE TABLE IF NOT EXISTS `{self.table_name}` (
                        `id`            int(11)   NOT NULL AUTO_INCREMENT PRIMARY KEY,
                        `day`           DATE      NOT NULL,
                        `min_temp`      INTEGER   NOT NULL,
                        `max_temp`      INTEGER   NOT NULL,
                        `precipitation` FLOAT NOT NULL,
                        `timestamp` DATETIME
                        )
                    ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin AUTO_INCREMENT=1 ;'''

        self.db.execute(query)

    def create(self, weather_forecast):
        return self.db.execute(f'INSERT INTO {self.table_name} (day, min_temp, max_temp, precipitation, timestamp) VALUES (%s, %s, %s, %s, %s)',
                        (weather_forecast.day, weather_forecast.min_temp, weather_forecast.max_temp, weather_forecast.precipitation, datetime.now()))

    def exists(self, weather_forecast):
        pass
