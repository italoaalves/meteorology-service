class WeatherForecast:
    def __init__(self, date, date_slug, min_temp, max_temp, precipitation, timestamp=None):
        self.date = date
        self.date_slug = date_slug
        self.min_temp = min_temp
        self.max_temp = max_temp
        self.precipitation = precipitation
        self.timestamp = timestamp
