class WeatherForecast:
    def __init__(self, id, day, min_temp, max_temp, precipitation, timestamp=None):
        self.id = int(id)
        self.day = day
        self.min_temp = int(min_temp)
        self.max_temp = int(max_temp)
        self.precipitation = float(precipitation)
        self.timestamp = timestamp
