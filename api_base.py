from abc import ABC, abstractmethod
import requests

class ApiBase(ABC):
    @abstractmethod
    def parse_data(self, data):
        pass

    def fetch(self, url, params):
        response = requests.get(url, params=params, timeout=20)
        response.raise_for_status()
        return self.parse_data(response.json())