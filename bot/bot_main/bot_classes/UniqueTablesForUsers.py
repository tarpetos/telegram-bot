from bot.bot_main.bot_classes.ConnectionDB import ConnectionDB
from bot.other_functions.get_id_and_convert import get_id_from_str


class UniqueTablesForUsers(ConnectionDB):
    def __init__(self):
        super().__init__()
        self.cur = self.con.cursor()
        self.date_id_procedure()
        self.month_avg_statistics_view()


    def date_id_procedure(self):
        self.cur.execute(
            '''
            CREATE PROCEDURE IF NOT EXISTS add_date_and_id(IN get_user_id INT)
                BEGIN
                    DECLARE date_now DATE;
                    SET date_now = CURDATE();
    
                    INSERT IGNORE INTO statistics(usage_date, user_id)
                    VALUES (date_now, get_user_id);
                END
            '''
        )

        self.con.commit()


    def month_avg_statistics_view(self):
        self.cur.execute(
            '''
            CREATE OR REPLACE VIEW statistics_view AS
            SELECT u.start_msg_date,
                   (SELECT s2.usage_date
                    FROM statistics s2
                    WHERE s2.user_id = s.user_id
                    ORDER BY s2.usage_date DESC
                    LIMIT 1) AS usage_date,
                   s.user_id,
                   ROUND(AVG(s.task_sched_delete_num), 0) AS task_sched_delete_avg,
                   ROUND(AVG(s.task_sched_update_num), 0) AS task_sched_update_avg,
                   ROUND(AVG(s.task_sched_insert_num), 0) AS task_sched_insert_avg,
                   ROUND(AVG(s.pass_gen_delete_num), 0) AS pass_gen_delete_avg,
                   ROUND(AVG(s.pass_gen_update_num), 0) AS pass_gen_update_avg,
                   ROUND(AVG(s.pass_gen_insert_num), 0) AS pass_gen_insert_avg
            FROM statistics s
            JOIN users_info u ON s.user_id = u.user_id
            WHERE DATEDIFF(s.usage_date, u.start_msg_date) < 31
            GROUP BY s.user_id;
            '''
        )

        self.con.commit()


    def cursor_usage(self):
        pass

########################################################################################################################
#################################################### TASK SCHEDULER ####################################################
########################################################################################################################

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


    def trigger_on_delete_task(self, trigger_name, table_name, user_id):
        # self.cur.execute('DROP TRIGGER IF EXISTS delete_from_task')
        self.cur.execute(
            '''
            CREATE TRIGGER IF NOT EXISTS `%s`
            BEFORE DELETE ON `%s`
            FOR EACH ROW
                BEGIN
                    DECLARE date_now DATE;
                    DECLARE get_user_id INT;
    
                    SET date_now = CURDATE();
                    SET get_user_id = %s;
    
                    UPDATE statistics
                    SET task_sched_delete_num = task_sched_delete_num + 1
                    WHERE usage_date = date_now AND user_id = get_user_id;
                END
            ''', (trigger_name, table_name, user_id)
        )


    def trigger_change_task(self, trigger_name,  table_name, user_id):
        # self.cur.execute('DROP TRIGGER IF EXISTS change_task')
        self.cur.execute(
            '''
            CREATE TRIGGER IF NOT EXISTS `%s`
            BEFORE UPDATE ON `%s`
            FOR EACH ROW
                BEGIN
                    DECLARE date_now DATE;
                    DECLARE get_user_id INT;
    
                    SET date_now = CURDATE();
                    SET get_user_id = %s;
    
                    UPDATE statistics
                    SET task_sched_update_num = task_sched_update_num + 1
                    WHERE usage_date = date_now AND user_id = get_user_id;
                END
            ''', (trigger_name, table_name, user_id)
        )


    def trigger_add_task(self, trigger_name, table_name, user_id):
        # self.cur.execute('DROP TRIGGER IF EXISTS add_task')
        self.cur.execute(
            '''
            CREATE TRIGGER IF NOT EXISTS `%s`
            BEFORE INSERT ON `%s`
            FOR EACH ROW
                BEGIN
                    DECLARE date_now DATE;
                    DECLARE get_user_id INT;
    
                    SET date_now = CURDATE();
                    SET get_user_id = %s;
    
                    UPDATE statistics
                    SET task_sched_insert_num = task_sched_insert_num + 1
                    WHERE usage_date = date_now AND user_id = get_user_id;
                END
            ''', (trigger_name, table_name, user_id)
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


    def delete_from_table(self, user_id, table_id):
        self.create_table(user_id)

        converted_id = get_id_from_str(user_id)
        trigger_name = f'delete_task_{converted_id}'
        self.cur.execute(
            'CALL add_date_and_id(%s)', (converted_id,)
        )
        self.trigger_on_delete_task(trigger_name, user_id, converted_id)

        self.cur.execute(
            '''
            DELETE FROM `%s`
            WHERE id = %s
            ''',
            (user_id, table_id)
        )

        self.con.commit()


    def update_table(self, user_id, user_data, table_id):
        self.create_table(user_id)

        converted_id = get_id_from_str(user_id)
        trigger_name = f'change_task_{converted_id}'
        self.cur.execute(
            'CALL add_date_and_id(%s)', (converted_id,)
        )
        self.trigger_change_task(trigger_name, user_id, converted_id)

        self.cur.execute(
            '''
            UPDATE `%s`
            SET user_data = %s
            WHERE id = %s;
            ''',
            (user_id, user_data, table_id)
        )

        self.con.commit()


    def insert_into_table(self, user_id, user_data):
        self.create_table(user_id)

        converted_id = get_id_from_str(user_id)
        trigger_name = f'add_task_{converted_id}'
        self.cur.execute(
            'CALL add_date_and_id(%s)', (converted_id,)
        )
        self.trigger_add_task(trigger_name, user_id, converted_id)

        self.cur.execute(
            'INSERT IGNORE INTO `%s` (user_data) VALUES (%s)',
            (user_id, user_data)
        )

        self.con.commit()

########################################################################################################################
################################################## PASSWORD GENERATOR ##################################################
########################################################################################################################

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


    def trigger_on_delete_password(self, trigger_name, table_name, user_id):
        self.cur.execute(
            '''
            CREATE TRIGGER IF NOT EXISTS `%s`
            BEFORE DELETE ON `%s`
            FOR EACH ROW
                BEGIN
                    DECLARE date_now DATE;
                    DECLARE get_user_id INT;
    
                    SET date_now = CURDATE();
                    SET get_user_id = %s;
    
                    UPDATE statistics
                    SET pass_gen_delete_num = pass_gen_delete_num + 1
                    WHERE usage_date = date_now AND user_id = get_user_id;
                END
            ''', (trigger_name, table_name, user_id)
        )


    def trigger_change_desc_password(self, trigger_name, table_name, user_id):
        self.cur.execute(
            '''
            CREATE TRIGGER IF NOT EXISTS `%s`
            BEFORE UPDATE ON `%s`
            FOR EACH ROW
                BEGIN
                    DECLARE date_now DATE;
                    DECLARE get_user_id INT;
    
                    SET date_now = CURDATE();
                    SET get_user_id = %s;
    
                    UPDATE statistics
                    SET pass_gen_update_num = pass_gen_update_num + 1
                    WHERE usage_date = date_now AND user_id = get_user_id;
                END
            ''', (trigger_name, table_name, user_id)
        )


    def trigger_add_password(self, trigger_name, table_name, user_id):
        self.cur.execute(
            '''
            CREATE TRIGGER IF NOT EXISTS `%s`
            BEFORE INSERT ON `%s`
            FOR EACH ROW
                BEGIN
                    DECLARE date_now DATE;
                    DECLARE get_user_id INT;
    
                    SET date_now = CURDATE();
                    SET get_user_id = %s;
    
                    UPDATE statistics
                    SET pass_gen_insert_num = pass_gen_insert_num + 1
                    WHERE usage_date = date_now AND user_id = get_user_id;
                END
            ''', (trigger_name, table_name, user_id)
        )


    def select_pass_gen_table(self, user_id):
        self.create_pass_gen_table(user_id)
        self.cur.execute(
            '''
            SELECT * FROM `%s`
            ORDER BY id;
            ''', (user_id,)
        )

        table_rows = self.cur.fetchall()

        return table_rows

    def select_pass_gen_id(self, user_id):
        self.create_pass_gen_table(user_id)
        self.cur.execute(
            '''
            SELECT id FROM `%s`
            ORDER BY id;
            ''', (user_id,)
        )

        result = self.cur.fetchall()
        return result


    def select_description(self, user_id):
        self.create_pass_gen_table(user_id)
        self.cur.execute(
            '''
            SELECT password_description FROM `%s`
            ORDER BY id;
            ''', (user_id,)
        )

        result = self.cur.fetchall()
        return str(result)


    def delete_from_password_table(self, user_id, table_id):
        self.create_table(user_id)

        converted_id = get_id_from_str(user_id)
        trigger_name = f'delete_password_{converted_id}'
        self.cur.execute(
            'CALL add_date_and_id(%s)', (converted_id,)
        )
        self.trigger_on_delete_password(trigger_name, user_id, converted_id)

        self.cur.execute(
            '''
            DELETE FROM `%s`
            WHERE id = %s
            ''',
            (user_id, table_id)
        )

        self.con.commit()


    def update_password_desc(self, user_id, user_desc, table_id):
        self.create_pass_gen_table(user_id)

        converted_id = get_id_from_str(user_id)
        trigger_name = f'change_password_{converted_id}'
        self.cur.execute(
            'CALL add_date_and_id(%s)', (converted_id,)
        )
        self.trigger_change_desc_password(trigger_name, user_id, converted_id)

        self.cur.execute(
            '''
            UPDATE `%s`
            SET password_description = %s
            WHERE id = %s;
            ''',
            (user_id, user_desc, table_id)
        )

        self.con.commit()


    def update_password(self, user_id, user_password, length, has_repetetive, table_id):
        self.create_pass_gen_table(user_id)

        converted_id = get_id_from_str(user_id)
        trigger_name = f'change_password_{converted_id}'
        self.cur.execute(
            'CALL add_date_and_id(%s)', (converted_id,)
        )
        self.trigger_change_desc_password(trigger_name, user_id, converted_id)

        self.cur.execute(
            '''
            UPDATE `%s`
            SET generated_password = %s, password_length = %s, has_repetetive = %s
            WHERE id = %s;
            ''',
            (user_id, user_password, length, has_repetetive, table_id)
        )

        self.con.commit()


    def insert_password_data(self, user_id, user_desc, generated_pass, password_length, has_repetetive):
        self.create_pass_gen_table(user_id)

        converted_id = get_id_from_str(user_id)
        trigger_name = f'add_password_{converted_id}'
        self.cur.execute(
            'CALL add_date_and_id(%s)', (converted_id,)
        )
        self.trigger_add_password(trigger_name, user_id, converted_id)

        self.cur.execute(
            '''
            INSERT INTO `%s` (password_description, generated_password, password_length, has_repetetive) 
            VALUES (%s, %s, %s, %s)
            ''',
            (user_id, user_desc, generated_pass, password_length, has_repetetive)
        )

        self.con.commit()
