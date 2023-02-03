from db.Db import Db
from model.wheater_forecast import WheaterForecast

class WheaterForecastDAO:
    def __init__(self):
      self.db = Db()
      self.table_name = "daily_forecasts"

      if not self.db.table_exists(self.table_name):
         self.db.execute('''CREATE TABLE `users` (
                           `id`            int(11)   NOT NULL AUTO_INCREMENT,
                           `day`           DATE      NOT NULL,
                           `min_temp`      INTEGER   NOT NULL,
                           `max_temp`      INTEGER   NOT NULL,
                           `precipitation` FLOAT NOT NULL,
                           PRIMARY KEY (`id`)
                           ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin
                        AUTO_INCREMENT=1 ;''')

    def create(self, wheater_forecast):
       return self.db.execute(f'INSERT INTO {self.table_name} (column1, column2, column3,etc) VALUES (value1, value2, value3)', None)
