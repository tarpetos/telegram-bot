import mysql
import mysql.connector


class ConnectionDB:
    def __init__(self):
        self.con = mysql.connector.connect(
            host='localhost',
            user='my_root',
            passwd='12/TaRaNtOs/34',
            database='bot_db'
        )
