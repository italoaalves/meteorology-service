class WeatherForecast:
    def __init__(self, day, min_temp, max_temp, precipitation, timestamp=None):
        self.day = day
        self.min_temp = min_temp
        self.max_temp = max_temp
        self.precipitation = precipitation
        self.timestamp = timestamp

    def is_valid(self):
        pass
