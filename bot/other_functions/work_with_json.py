import os

from bot.bot_main.main_objects_initialization import unique_table
from bot.other_functions.write_password_data_to_json import write_to_json


async def send_json(call):
    make_json_dir()
    user_id = call.from_user.id
    password_data_list = unique_table.select_pass_gen_table(f'pass_gen_table_{user_id}')
    write_to_json(user_id, password_data_list)

    with open(f'users_json_files/user_json_{user_id}.json', 'rb') as json_file:
        json_content = json_file.read()

    sent_message = await call.bot.send_document(
        chat_id=call.message.chat.id,
        document=('Passwords.json', json_content),
        caption=f'Json file for <code>@{call.from_user.username}</code>',
        parse_mode='HTML'
    )

    return sent_message


def make_json_dir():
    path = f'users_json_files'

    if not os.path.exists(path):
        os.makedirs(path)


def remove_json(call):
    path_to_json = f'users_json_files/user_json_{call.from_user.id}.json'

    if os.path.exists(path_to_json):
        os.remove(path_to_json)
