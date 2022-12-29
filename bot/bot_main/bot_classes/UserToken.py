import mysql
import mysql.connector

class UserToken:
    def __init__(self):
        self.con = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='1111',
            database='bot_db'
        )
        self.cur = self.con.cursor()
        self.create_table()


    def create_table(self):
        self.cur.execute(
            '''
            
            CREATE TABLE IF NOT EXISTS generated_tokens (
                id INT PRIMARY KEY AUTO_INCREMENT,
                user_id INT NOT NULL,
                user_token VARCHAR(150),
                CONSTRAINT unique_token UNIQUE (user_id),
                FOREIGN KEY (user_id) REFERENCES users_info(user_id) ON DELETE CASCADE ON UPDATE CASCADE
            )
            '''
        )


    def select_all_tokens(self):
        self.cur.execute(
            '''
            SELECT user_token FROM generated_tokens
            '''
        )

        all_tokens_tuple_lst = self.cur.fetchall()
        all_tokens_lst = [token_tuple[0] for token_tuple in all_tokens_tuple_lst]

        return all_tokens_lst


    def select_token(self, get_user_id):
        self.cur.execute(
            '''
            SELECT user_token FROM generated_tokens
            WHERE user_id = %s
            ''',
            (get_user_id,)
        )

        get_token = self.cur.fetchone()

        if get_token:
            return get_token[0]


    def add_token(self, get_user_id, get_new_token):
        self.cur.execute(
            '''
            INSERT INTO generated_tokens(user_id, user_token)
            VALUES (%s, %s)
            ON DUPLICATE KEY UPDATE user_token = %s 
            ''',
            (get_user_id, get_new_token, get_new_token)
        )

        self.con.commit()


    # def update_token(self, get_new_token, get_user_id):
    #     self.cur.execute(
    #         '''
    #         UPDATE generated_tokens
    #         SET user_token = %s
    #         WHERE user_id = %s
    #         ''',
    #         (get_new_token, get_user_id,)
    #     )


    def remove_token(self, get_user_id):
        self.cur.execute(
            '''
            DELETE FROM generated_tokens
            WHERE user_id = %s
            ''',
            (get_user_id,)
        )

        self.con.commit()
