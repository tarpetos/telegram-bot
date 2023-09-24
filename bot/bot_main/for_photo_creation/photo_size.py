def get_ratio(width, height) -> str:
    if width > height:
        return f"{round(width / height, 2)} : 1"
    elif width < height:
        return f"1 : {round(height / width, 2)}"
    else:
        return "1 : 1"


def write_to_txt(width, height):
    sides_ratio = get_ratio(width, height)
    with open("bot/bot_main/for_photo_creation/photo_size.txt", "w+") as size_txt:
        size_txt.write(
            f"Width: <code>{width}</code>\n"
            f"Height: <code>{height}</code>\n"
            f"Approximate sides ratio: <code>{sides_ratio}</code>\n"
        )


def get_data_from_txt() -> str:
    with open("bot/bot_main/for_photo_creation/photo_size.txt", "r") as size_txt:
        result = size_txt.read()

    return result
