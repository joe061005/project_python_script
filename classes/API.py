import requests
import configparser
import datetime

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

    def get_ticker_daily_price(self, ticker):
        today = datetime.datetime.utcnow()
        d = datetime.timedelta(days=5)
        a = (today - d).strftime("%Y-%m-%d")
        endpoint = f"/v2/aggs/ticker/{ticker}/range/1/day/{a}/{datetime.datetime.utcnow().strftime('%Y-%m-%d')}?adjusted=true&sort=desc&limit=120&apiKey={self.API_Key}"
        response = requests.get(f"{self.base_URL}{endpoint}")
        return response.json()

    def get_market_status(self):
        endpoint = f"/v1/marketstatus/now?apiKey={self.API_Key}"
        response = requests.get(f"{self.base_URL}{endpoint}")
        return response.json()["indicesGroups"]["nasdaq"]

