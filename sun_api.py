from api_base import ApiBase
from sun_data import SunData


class SunApi(ApiBase):
    def parse_data(self, data):
        return SunData(data)