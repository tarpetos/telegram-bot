from bot.bot_main.main_objects_initialization import table


def check_for_id(message):
    table_data = table.select_table('table_' + str(message.from_user.id))

    temp_lst = []
    for count, value in enumerate(table_data):
        temp_lst.append(int(table_data[count][0]))

    return temp_lst
