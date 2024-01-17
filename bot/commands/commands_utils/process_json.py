import json
import os
from typing import List, Tuple, Any

from aiogram import types

from .encryption_decryption import decrypt

NUMBER_OF_JSON_IDENTS = 12
JSON_DIR = "temp_data"


def make_json_dir() -> None:
    if not os.path.exists(JSON_DIR):
        os.makedirs(JSON_DIR)


def remove_json(call: types.CallbackQuery) -> None:
    path_to_json = os.path.join(JSON_DIR, f"json_{call.from_user.id}.json")

    if os.path.exists(path_to_json):
        os.remove(path_to_json)


def write_to_json(user_id: int, table_rows: List[Tuple[Any]]) -> None:
    data = [
        {
            "Password №": password_number,
            "ID": password_data[0],
            "Password description": password_data[1],
            "Password": decrypt(password_data[2]),
            "Length": password_data[3],
            "Has repetitive?": password_data[4],
        }
        for password_number, password_data in enumerate(table_rows, 1)
    ]

    file_path = os.path.join(JSON_DIR, f"json_{user_id}.json")
    make_json_dir()

    with open(file_path, "w") as outfile:
        json.dump(data, outfile, indent=NUMBER_OF_JSON_IDENTS, ensure_ascii=False)


def read_json(user_id: int) -> bytes:
    path_to_json = os.path.join(JSON_DIR, f"json_{user_id}.json")
    with open(path_to_json, "rb") as json_file:
        json_content = json_file.read()

    return json_content


async def table_is_empty_message(call: types.CallbackQuery) -> types.Message:
    sent_message = await call.message.edit_text(
        text="Table has no records. So, JSON is empty.",
        parse_mode="HTML",
    )
    await call.message.edit_reply_markup(reply_markup=call.message.reply_markup)
    return sent_message


async def json_message(call: types.CallbackQuery, json_content: bytes) -> types.Message:
    sent_message = await call.bot.send_document(
        chat_id=call.message.chat.id,
        document=("Passwords.json", json_content),
        caption=f"Json file for <code>@{call.from_user.username}</code>",
        parse_mode="HTML",
    )
    return sent_message


async def send_json(call: types.CallbackQuery, user_id: int, data_list: List[Tuple[Any]]) -> types.Message:
    make_json_dir()
    write_to_json(user_id, data_list)
    json_data = read_json(user_id)

    return await json_message(call, json_data)
