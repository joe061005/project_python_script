# This script is to update the market cap of the top 10 tech stocks every 24 hours

from classes.Database import Database
from classes.API import API
import time

API = API()
Database = Database()

# https://companiesmarketcap.com/tech/largest-tech-companies-by-market-cap/
top10List = ["AAPL", "MSFT", "GOOG", "AMZN", "NVDA", "TSLA", "META", "TSM", "AVGO", "ORCL"]

count = 0

index = 1 if API.get_market_status() == "closed" else 0

for x in top10List:
    if count == 4:
        print("waiting for 1 minute due to API limit...")
        time.sleep(61)
        count = 0
    print(f"------ processing {x} ------")
    capDetail = API.get_ticker_details(x)['results']
    print(f"Market Cap: {capDetail['market_cap']}")
    lastClosePrice = API.get_ticker_daily_price(x)['results'][index]['c']
    print(f"Last Close Price: {lastClosePrice}")
    Database.update_ticker_data(x, capDetail['market_cap'], lastClosePrice)
    count += 1


