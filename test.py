from classes.Database import Database
from classes.API import API

API = API()
print(API.get_ticker_daily_price("AAPL"))