from db.Db import Db
from model.wheater_forecast import WheaterForecast

class WeatherForecastDAO:
    def __init__(self):
      self.db = Db()
      self.table_name = "weather_forecasts"

      self.db.execute('''CREATE TABLE IF NOT EXISTS `weather_forecasts` (
                        `id`            int(11)   NOT NULL AUTO_INCREMENT,
                        `day`           DATE      NOT NULL,
                        `min_temp`      INTEGER   NOT NULL,
                        `max_temp`      INTEGER   NOT NULL,
                        `precipitation` FLOAT NOT NULL,
                        PRIMARY KEY (`id`)
                        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin
                     AUTO_INCREMENT=1 ;''')

    def create(self, weather_forecast):
       return self.db.execute(f'INSERT INTO {self.table_name} (day, min_temp, max_temp, precipitation) VALUES (?, ?, ?, ?)', None)

   def exists(self, weather_forecast)
