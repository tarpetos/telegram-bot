import os
import mysql
import mysql.connector


from dotenv import load_dotenv, find_dotenv


class ConnectionDB:
    def __init__(self):
        load_dotenv(find_dotenv())
        self.con = mysql.connector.connect(
            host=os.getenv('HOST'),
            user=os.getenv('DB_USER'),
            passwd=os.getenv('PASSWORD'),
            database=os.getenv('DATABASE'),
        )
