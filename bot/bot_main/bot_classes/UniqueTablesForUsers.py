import json
import os
import mysql
import mysql.connector

from bot.other_functions.write_password_data_to_json import write_to_json


class UniqueTablesForUsers:
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
            '''
            CREATE TABLE IF NOT EXISTS `%s` (
                id INT PRIMARY KEY AUTO_INCREMENT,
                user_data VARCHAR(768),
                CONSTRAINT unique_data UNIQUE(user_data)
            )
            ''', (user_id,)
        )

    def create_pass_gen_table(self, user_id):
        self.cur.execute(
            '''
            CREATE TABLE IF NOT EXISTS `%s` (
                id INT PRIMARY KEY AUTO_INCREMENT,
                password_description VARCHAR(384),
                generated_password VARCHAR(384),
                password_length INT,
                has_repetetive BOOLEAN,
                CONSTRAINT unique_data UNIQUE(password_description)
            )
            ''', (user_id,)
        )

    def select_table(self, user_id):
        self.create_table(user_id)
        self.cur.execute(
            '''
            SELECT id, user_data FROM `%s`
            ORDER BY id;
            ''', (user_id,)
        )

        result = self.cur.fetchall()
        return result

    def select_pass_gen_table(self, user_id):
        self.create_pass_gen_table(user_id)
        self.cur.execute(
            '''
            SELECT id, password_description, generated_password, password_length, has_repetetive FROM `%s`
            ORDER BY id;
            ''', (user_id,)
        )

        table_rows = self.cur.fetchall()

        write_to_json(user_id, table_rows)

        return table_rows

    def select_pass_gen_id(self, user_id):
        self.create_table(user_id)
        self.cur.execute(
            '''
            SELECT id FROM `%s`
            ORDER BY id;
            ''', (user_id,)
        )

        result = self.cur.fetchall()
        return result

    def insert_into_table(self, user_id, user_data):
        self.create_table(user_id)
        self.cur.execute(
            'INSERT IGNORE INTO `%s` (user_data) VALUES (%s)',
            (user_id, user_data)
        )

        self.con.commit()

    def update_table(self, user_id, user_data, table_id):
        self.create_table(user_id)
        self.cur.execute(
            '''
            UPDATE unique_tables.`%s` t
            SET t.user_data = %s
            WHERE t.id = %s;
            ''',
            (user_id, user_data, table_id)
        )

        self.con.commit()

    def update_password_desc(self, user_id, user_desc, table_id):
        self.create_table(user_id)
        self.cur.execute(
            '''
            UPDATE unique_tables.`%s` t
            SET t.password_description = %s
            WHERE t.id = %s;
            ''',
            (user_id, user_desc, table_id)
        )

        self.con.commit()


    def update_password(self, user_id, user_password, length, has_repetetive, table_id):
        self.create_table(user_id)
        self.cur.execute(
            '''
            UPDATE unique_tables.`%s` t
            SET t.generated_password = %s, t.password_length = %s, t.has_repetetive = %s
            WHERE t.id = %s;
            ''',
            (user_id, user_password, length, has_repetetive, table_id)
        )

        self.con.commit()


    def delete_from_table(self, user_id, table_id):
        self.create_table(user_id)
        self.cur.execute(
            '''
            DELETE FROM `%s`
            WHERE id = %s
            ''',
            (user_id, table_id)
        )

        self.con.commit()
