import mysql
import mysql.connector


class StickerDataTable:
    def __init__(self):
        self.con = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='1111',
            database='bot_db'
        )
        self.cur = self.con.cursor()
        self.create_table_stickers()

    def create_table_stickers(self):
        self.cur.execute(
            '''
            CREATE TABLE IF NOT EXISTS stickers(
                id INT PRIMARY KEY AUTO_INCREMENT,
                sticker VARCHAR(80),
                CONSTRAINT unique_sticker UNIQUE(sticker)
            )
            '''
        )

    def get_sticker(self):
        self.cur.execute(
            '''
            SELECT sticker FROM stickers
            ORDER BY id;
            '''
        )

        result = self.cur.fetchall()

        return result
