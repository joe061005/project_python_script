# This script is to update the market cap of the top 10 tech stocks every 24 hours

from classes.Database import Database
from classes.API import API
import time

API = API()
Database = Database()

# https://companiesmarketcap.com/tech/largest-tech-companies-by-market-cap/
top10List = ["AAPL", "MSFT", "GOOG", "AMZN", "NVDA", "TSLA", "META", "TSM", "AVGO", "ORCL"]

count = 0
for x in top10List:
    if count == 5:
        print("waiting for 1 minute due to API limit...")
        time.sleep(65)
        count = 0
    print(f"------ processing {x} ------")
    detail = API.get_ticker_details(x)['results']
    print(detail)
    if Database.check_ticker_data(x) == 0:
        Database.insert_ticker_data(detail['branding']['icon_url'] + f"?apiKey={API.API_Key}", detail['market_cap'], x, detail['name'])
    else:
        Database.update_ticker_data(x, detail['market_cap'])
    count += 1


