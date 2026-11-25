from api_base import ApiBase
from geo_data import GeoData


class GeoApi(ApiBase):
    def parse_data(self, data):
        return [GeoData(rec) for rec in data]