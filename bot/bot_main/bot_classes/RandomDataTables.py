import mysql
import mysql.connector


class RandomDataTables:
    def __init__(self):
        self.con = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='1111',
            database='bot_db'
        )
        self.cur = self.con.cursor()

    def create_table_bot(self):
        self.cur.execute(
            """
            CREATE TABLE IF NOT EXISTS bot(
                id INT PRIMARY KEY AUTO_INCREMENT,
                bullshit VARCHAR(200)
            )
            """
        )

    def create_table_conversation_data(self):
        self.cur.execute(
            """
            CREATE TABLE IF NOT EXISTS conversation_data(
                id INT PRIMARY KEY AUTO_INCREMENT,
                conversation VARCHAR(768),
                CONSTRAINT unique_data UNIQUE(conversation)
            )
            """
        )

    def create_table_stickers(self):
        self.cur.execute(
            """
            CREATE TABLE IF NOT EXISTS stickers(
                id INT PRIMARY KEY AUTO_INCREMENT,
                sticker VARCHAR(80),
                CONSTRAINT unique_sticker UNIQUE(sticker)
            )
            """
        )
