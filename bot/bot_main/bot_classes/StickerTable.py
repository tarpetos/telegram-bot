from bot.bot_main.bot_classes.ConnectionDB import ConnectionDB


class StickerTable(ConnectionDB):
    def __init__(self):
        super().__init__()
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

    def insert_into_sticker_table(self, sticker_id):
        self.cur.execute(
            '''
            INSERT IGNORE INTO stickers(sticker)
            VALUES (%s)
            ''',
            (sticker_id,)
        )

        self.con.commit()