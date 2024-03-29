import os
import json

from bot.other_functions.encryption_decryption import decrypt

NUMBER_OF_JSON_IDENTS = 12


def write_to_json(user_id, table_rows):
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

    directory = "users_json_files"
    file_path = os.path.join(directory, f"user_json_{user_id}.json")

    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(file_path, "w") as outfile:
        json.dump(data, outfile, indent=NUMBER_OF_JSON_IDENTS, ensure_ascii=False)