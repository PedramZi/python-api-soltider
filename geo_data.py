class GeoData:
    def __init__(self, rec: dict):
        self.lat = rec["lat"]
        self.lon = rec["lon"]
        self.city = rec["name"]