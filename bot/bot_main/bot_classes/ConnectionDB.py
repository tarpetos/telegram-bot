import mysql
import mysql.connector


class ConnectionDB:
    def __init__(self):
        self.con = mysql.connector.connect(
            host='localhost',

            # local
            user='root',
            passwd='1111',

            # remote
            # user='my_root',
            # passwd='12/TaRaNtOs/34',

            database='bot_db'
        )
