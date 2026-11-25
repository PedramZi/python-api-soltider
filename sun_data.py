class SunData:
    def __init__(self, rec: dict):
        self.sunrise = rec["sunrise"]
        self.sunset = rec["sunset"]
        self.timezone = rec.get("tzid")