import requests
import configparser

class API:
    def __init__(self):
        self.API_Key = API.get_API_Key()
        self.base_URL = "https://api.polygon.io"

    @staticmethod
    def get_API_Key():
        config = configparser.ConfigParser()
        config.read('./config/config.ini')
        return config['polygon']['API_Key']

    def get_ticker_details(self, ticker):
        endpoint = f"/v3/reference/tickers/{ticker}?apiKey={self.API_Key}"
        response = requests.get(f"{self.base_URL}{endpoint}")
        return response.json()