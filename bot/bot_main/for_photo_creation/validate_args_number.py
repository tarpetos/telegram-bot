from bot.bot_main.for_photo_creation.photo_size import get_data_from_txt
from bot.bot_main.for_photo_creation.remake_user_photo import create_new_photo


async def validate_args(formatted_lst, message):
    try:
        if len(formatted_lst) == 6:
            get_error_state = create_new_photo(
                user_data=formatted_lst[0],
                pos_x=int(formatted_lst[1]),
                pos_y=int(formatted_lst[2]),
                img_width=int(formatted_lst[3]),
                img_height=int(formatted_lst[4]),
                img_font=int(formatted_lst[5]),
            )
        elif len(formatted_lst) == 4:
            get_error_state = create_new_photo(
                user_data=formatted_lst[0],
                pos_x=int(formatted_lst[1]),
                pos_y=int(formatted_lst[2]),
                img_font=int(formatted_lst[3]),
            )
        elif len(formatted_lst) == 2 and check_for_int_type(
            formatted_lst[0], formatted_lst[1]
        ):
            get_error_state = create_new_photo(
                img_width=int(formatted_lst[0]),
                img_height=int(formatted_lst[1]),
            )
        elif len(formatted_lst) == 2:
            get_error_state = create_new_photo(
                user_data=formatted_lst[0],
                img_font=int(formatted_lst[1]),
            )
        elif len(formatted_lst) == 1:
            get_error_state = create_new_photo(
                user_data=formatted_lst[0],
            )
        else:
            get_error_state = create_new_photo(
                user_data=formatted_lst[0],
                pos_x=int(formatted_lst[1]),
                pos_y=int(formatted_lst[2]),
            )

        if get_error_state:
            await message.reply(
                f"Coordinate X or Y are out of image bounds! Try again.\n{get_data_from_txt()}",
                parse_mode="HTML",
            )
            return False
    except ValueError:
        await message.reply(
            f"One or more arguments has incorrect value! Try again.\n{get_data_from_txt()}",
            parse_mode="HTML",
        )
        return False
    except IndexError:
        await message.reply(
            f"Your input is incorrect! Try again.\n{get_data_from_txt()}",
            parse_mode="HTML",
        )
        return False

    return True


def check_for_int_type(str1: str, str2: str) -> bool:
    for char in str1, str2:
        if char.isdigit():
            continue
        else:
            return False

    return True
