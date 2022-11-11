import mysql
import mysql.connector


class StoreUsersData:
    def __init__(self):
        self.con = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='1111',
            database='bot_db'
        )
        self.cur = self.con.cursor()

    def create_table(self):
        self.cur.execute(
            """
            CREATE TABLE IF NOT EXISTS users_info(
                id INT PRIMARY KEY AUTO_INCREMENT,
                user_id VARCHAR(20) NOT NULL,
                username VARCHAR(200) NOT NULL,
                full_name VARCHAR(200) NOT NULL,
                chat_id VARCHAR(20) NOT NULL,
                CONSTRAINT unique_data UNIQUE(user_id, username, full_name)
            )
            """
        )

    def connect_to_db(self, user_id, username, full_name, chat_id):
        self.cur.execute(
            "INSERT IGNORE INTO users_info (user_id, username, full_name, chat_id) VALUES (%s, %s, %s, %s)",
            (user_id, username, full_name, chat_id)
        )

        self.con.commit()
