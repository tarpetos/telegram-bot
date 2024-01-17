def check_user_id(message):
    user_id = ""
    if ", " in message:
        user_id = message[: message.find(",")]
    elif "," in message:
        user_id = message[: message.find(",")]
    elif ". " in message:
        user_id = message[: message.find(".")]
    elif "." in message:
        user_id = message[: message.find(".")]

    return user_id


def check_user_data(message):
    user_data = ""
    if ", " in message:
        user_data = message[message.find(",") + 2:]
    elif "," in message:
        user_data = message[message.find(",") + 1:]
    elif ". " in message:
        user_data = message[message.find(".") + 2:]
    elif "." in message:
        user_data = message[message.find(".") + 1:]

    return user_data
