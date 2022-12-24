from string import digits, ascii_letters, punctuation


def keyboard_content_choice(user_choice) -> str:
    if user_choice == 'all_characters':
        return digits + ascii_letters + punctuation
    elif user_choice == 'only_letters':
        return ascii_letters
    elif user_choice == 'only_digits':
        return digits
    elif user_choice == 'letters_digits':
        return digits + ascii_letters
    elif user_choice == 'letters_signs':
        return ascii_letters + punctuation
    elif user_choice == 'digits_signs':
        return digits + punctuation
