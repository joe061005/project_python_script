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

    def fetch_data(self, query):
        myCursor = self.DB.cursor()
        myCursor.execute(query)
        return myCursor.fetchall()

    def insert_crypto(self, crypto):
        myCursor = self.DB.cursor()
        myCursor.execute("INSERT INTO crypto (Symbol, Price, Percent, Time) VALUES (%s, %s, %s, %s)",
                            (crypto[0], float(crypto[1]), float(crypto[2]), datetime.fromtimestamp(crypto[3]/1000).strftime('%Y-%m-%d %H:%M:%S')))
        self.DB.commit()

    def insert_crypto_zone(self, cryptoList, zone):
        myCursor = self.DB.cursor()
        # get zone ID
        myCursor.execute(f"SELECT id FROM zone where Name = '{zone}'")
        zoneID = myCursor.fetchall()[0][0]

        # get cryptoID
        myCursor.execute("SELECT id FROM crypto where Symbol IN (%s)" % ','.join(['%s'] * len(cryptoList)), tuple([ f'{x}BUSD' for x in cryptoList]))
        cryptoID = myCursor.fetchall()

        for x in cryptoID:
             myCursor.execute("INSERT INTO cryptozone (cryptoID, zoneID) VALUES (%s, %s)", (int(x[0]), int(zoneID)))
             self.DB.commit()

    def insert_network(self, network):
        myCursor = self.DB.cursor()
        myCursor.execute(f"INSERT INTO network (network) VALUES ('{network}')")
        self.DB.commit()

    def update_crypto(self, crypto):
        myCursor = self.DB.cursor()
        myCursor.execute(f"UPDATE FROM ")

