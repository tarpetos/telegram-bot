import mysql
import mysql.connector


class UsersDataStore:
    def __init__(self):
        self.con = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='1111',
            database='bot_db'
        )
        self.cur = self.con.cursor()
        self.update_start_date_after_month()


    def create_table(self):
        self.cur.execute(
            '''
            CREATE TABLE IF NOT EXISTS users_info(
                id INT PRIMARY KEY AUTO_INCREMENT,
                user_id INT NOT NULL,
                username VARCHAR(200) NOT NULL,
                full_name VARCHAR(200) NOT NULL,
                chat_id VARCHAR(30) NOT NULL,
                start_msg_date DATE DEFAULT(CURRENT_DATE),
                CONSTRAINT unique_data UNIQUE(user_id)
            )
            '''
        )


    def update_start_date_after_month(self):
        self.cur.execute(
            '''
            UPDATE users_info, statistics
            SET start_msg_date = CURDATE()
            WHERE DATEDIFF(usage_date, start_msg_date) > 30
            '''
        )

        self.con.commit()


    def connect_to_db(self, user_id, username, full_name, chat_id):
        self.cur.execute(
            '''
            INSERT IGNORE INTO users_info (user_id, username, full_name, chat_id)
            VALUES (%s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE username = %s, full_name = %s, chat_id = %s 
            ''',
            (user_id, username, full_name, chat_id, username, full_name, chat_id)
        )

        self.con.commit()