def keyboard_length_choice(user_choice) -> int:
    if user_choice == 'very_easy':
        return 10
    elif user_choice == 'easy':
        return 20
    elif user_choice == 'normal':
        return 30
    elif user_choice == 'hard':
        return 40
    elif user_choice == 'very_hard':
        return 50
    elif user_choice == 'unbreakable':
        return 100
