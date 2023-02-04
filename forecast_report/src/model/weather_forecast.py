class WeatherForecast:
    def __init__(self, id, date, date_slug, min_temp, max_temp, precipitation, timestamp=None):
        self.id = int(id)
        self.date = date
        self.date_slug = date_slug
        self.min_temp = int(min_temp)
        self.max_temp = int(max_temp)
        self.precipitation = float(precipitation)
        self.timestamp = timestamp
