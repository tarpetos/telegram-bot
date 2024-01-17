import os
import mysql
import mysql.connector


class DatabaseConnector:
    def __init__(self):
        self.con = mysql.connector.connect(
            host=os.getenv("HOST"),
            user=os.getenv("DB_USER"),
            passwd=os.getenv("PASSWORD"),
            database=os.getenv("DATABASE"),
        )
        self.cur = self.con.cursor()
