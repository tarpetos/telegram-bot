from bot.bot_main.bot_classes.ConnectionDB import ConnectionDB


class StatisticsTable(ConnectionDB):
    def __init__(self):
        super().__init__()
        self.create_table()

    def create_table(self):
        self.cur.execute(
            """
            CREATE TABLE IF NOT EXISTS statistics (
                id INT PRIMARY KEY AUTO_INCREMENT,
                usage_date DATE NOT NULL,
                user_id INT NOT NULL,
                task_sched_delete_num INT DEFAULT 0,
                task_sched_update_num INT DEFAULT 0,
                task_sched_insert_num INT DEFAULT 0,
                pass_gen_delete_num INT DEFAULT 0,
                pass_gen_update_num INT DEFAULT 0,
                pass_gen_insert_num INT DEFAULT 0,
                CONSTRAINT unique_date_id UNIQUE (usage_date, user_id),
                FOREIGN KEY (user_id) REFERENCES users_info(user_id) ON DELETE CASCADE ON UPDATE CASCADE
            )
            """
        )
