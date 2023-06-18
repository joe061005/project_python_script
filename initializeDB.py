# This script is to initialize the DB

from classes.Database import Database
from classes.API import API
import time

API = API()
Database = Database()

# https://companiesmarketcap.com/tech/largest-tech-companies-by-market-cap/
top10List = ["AAPL", "MSFT", "GOOG", "AMZN", "NVDA", "TSLA", "META", "TSM", "AVGO", "ORCL"]

index = 1 if API.get_market_status() == "closed" else 0

for x in top10List:
    print(f"------ processing {x} ------")
    capDetail = API.get_ticker_details(x)['results']
    print(f"Market Cap: {capDetail['market_cap']}")
    lastClosePrice = API.get_ticker_daily_price(x)['results'][index]['c']
    print(f"Last Close Price: {lastClosePrice}")
    url = Database.upload_image_to_cloudinary(capDetail['branding']['icon_url'] + f"?apiKey={API.API_Key}")
    Database.insert_ticker_data(url, capDetail['market_cap'], x, capDetail['name'], lastClosePrice)
    print("waiting for 1 minute due to API limit...")
    time.sleep(61)