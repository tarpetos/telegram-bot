def keyboard_length_choice(user_choice: str) -> int:
    password_complexities = {
        "very_easy": 10,
        "easy": 20,
        "normal": 30,
        "hard": 40,
        "very_hard": 50,
        "unbreakable": 100,
    }

    for complexity_key in password_complexities:
        if user_choice == complexity_key:
            return password_complexities[complexity_key]
