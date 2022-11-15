import mysql
import mysql.connector


class CreateUniqueTables:
    def __init__(self):
        self.con = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='1111',
            database='unique_tables'
        )
        self.cur = self.con.cursor()

    def create_table(self, user_id):
        self.cur.execute(
            """
            CREATE TABLE IF NOT EXISTS `%s` (
                id INT PRIMARY KEY AUTO_INCREMENT,
                user_data VARCHAR(768),
                CONSTRAINT unique_data UNIQUE(user_data)
            )
            """, (user_id,)
        )

    def select_table(self, user_id):
        self.create_table(user_id)
        self.cur.execute(
            """
            SELECT id, user_data FROM `%s`
            ORDER BY id;
            """, (user_id,)
        )

        result = self.cur.fetchall()
        return result

    def insert_into_table(self, user_id, user_data):
        self.create_table(user_id)
        self.cur.execute(
            "INSERT IGNORE INTO `%s` (user_data) VALUES (%s)",
            (user_id, user_data)
        )

        self.con.commit()

    def update_table(self, user_id, user_data, table_id):
        self.create_table(user_id)
        self.cur.execute(
            """
            UPDATE unique_tables.`%s` t
            SET t.user_data = %s
            WHERE t.id = %s;
            """,
            (user_id, user_data, table_id)
        )

        self.con.commit()

    def delete_from_table(self, user_id, table_id):
        self.create_table(user_id)
        self.cur.execute(
            """
            DELETE FROM `%s`
            WHERE id = %s
            """,
            (user_id, table_id)
        )

        self.con.commit()
