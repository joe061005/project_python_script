# This script is to initialize the DB

from classes.Database import Database
from classes.API import API
import time

API = API()
Database = Database()

# https://companiesmarketcap.com/tech/largest-tech-companies-by-market-cap/
top10List = ["AAPL", "MSFT", "GOOG", "AMZN", "NVDA", "TSLA", "META", "TSM", "AVGO", "ORCL"]

count = 0
for x in top10List:
    if count == 4:
        print("waiting for 1 minute due to API limit...")
        time.sleep(61)
        count = 0
    print(f"------ processing {x} ------")
    detail = API.get_ticker_details(x)['results']
    print(detail)
    url = Database.upload_image_to_cloudinary(detail['branding']['icon_url'] + f"?apiKey={API.API_Key}")
    Database.insert_ticker_data(url, detail['market_cap'], x, detail['name'])
    count += 2