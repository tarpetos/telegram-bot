from bot.bot_main.main_objects_initialization import unique_table


def check_for_id(message):
    table_data = unique_table.select_table(f'table_{message.from_user.id}')

    temp_lst = []
    for count, value in enumerate(table_data):
        temp_lst.append(int(table_data[count][0]))

    return temp_lst

def check_for_password_id(message):
    id_data = unique_table.select_pass_gen_id(f'pass_gen_table_{message.from_user.id}')

    temp_lst = []
    for id_value in id_data:
        temp_lst.append(int(id_value[0]))

    return temp_lst

