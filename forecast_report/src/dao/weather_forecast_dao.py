from db.Db import Db

class WeatherForecastDAO:
    def __init__(self):
       self.db = Db()

    def list(self):
       return self.db.execute('SELECT * FROM users', None).fetchall()
