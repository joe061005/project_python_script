import configparser
import mysql.connector
from datetime import datetime


class Database:
    def __init__(self):
        self.DB = self.initialize_database()

    @staticmethod
    def initialize_database():
        config = configparser.ConfigParser()
        config.read('./config/config.ini')
        return mysql.connector.connect(
            host=config['database']['host'],
            user=config['database']['user'],
            password=config['database']['password'],
            port=config['database']['port'],
            database=config['database']['database']
        )

    def check_ticker_data(self, ticker):
        myCursor = self.DB.cursor()
        myCursor.execute(f"SELECT * FROM stockInfo where Ticker = '{ticker}'")
        data = myCursor.fetchall()
        return len(data)

    def insert_ticker_data(self, url, cap, ticker, name):
        myCursor = self.DB.cursor()
        myCursor.execute("INSERT INTO stockInfo (ImageURL, MarketCap, Ticker, Name) VALUES (%s, %s, %s, %s)",
                            (url, int(cap), ticker, name))
        self.DB.commit()

    def update_ticker_data(self, ticker, market_cap):
        myCursor = self.DB.cursor()
        myCursor.execute(f"UPDATE stockInfo SET MarketCap = {market_cap} WHERE Ticker = '{ticker}' ")
        self.DB.commit()


