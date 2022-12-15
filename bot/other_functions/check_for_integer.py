def check_password_length_input(user_input) -> bool:
    if not user_input.isdigit():
        raise ValueError
    elif int(user_input) > 384 or int(user_input) <= 0:
        raise ValueError
    else:
        return True
