import mysql
import mysql.connector

from bot.bot_main.bot_classes.RandomDataTables import RandomDataTables


class ExtractRandomData:
    def __init__(self, create_tables=RandomDataTables()):
        self.con = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='1111',
            database='bot_db'
        )
        self.create_table = create_tables
        self.cur = self.con.cursor()

    # get bullshit
    def get_bullshit(self):
        self.create_table.create_table_bot()
        self.cur.execute(
            """
            SELECT bullshit FROM bot
            ORDER BY id;
            """
        )

        result = self.cur.fetchall()

        return result

    # get conversation data
    def get_conversation_data(self):
        self.create_table.create_table_conversation_data()

        self.cur.execute(
            """
            SELECT conversation FROM conversation_data
            ORDER BY id;
            """
        )

        result = self.cur.fetchall()

        return result

    # get sticker
    def get_sticker(self):
        self.create_table.create_table_stickers()

        self.cur.execute(
            """
            SELECT sticker FROM stickers
            ORDER BY id;
            """
        )

        result = self.cur.fetchall()

        return result
