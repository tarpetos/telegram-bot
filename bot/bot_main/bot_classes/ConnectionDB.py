import os
import mysql
import mysql.connector

from dotenv import load_dotenv, find_dotenv


class ConnectionDB:
    def __init__(self):
        load_dotenv(find_dotenv())
        self.con = mysql.connector.connect(
            host=os.getenv("HOST"),
            user=os.getenv("DB_USER"),
            passwd=os.getenv("PASSWORD"),
            database=os.getenv("DATABASE"),
        )
        self.cur = self.con.cursor()

    def close_connection(self):
        if self.con.is_connected():
            self.cur.close()
            self.con.close()

    def __del__(self):
        self.close_connection()
