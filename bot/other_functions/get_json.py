async def send_json(call):
    with open(f'users_json_files/user_json_pass_gen_table_{call.from_user.id}.json', 'rb') as json_file:
        json_content = json_file.read()

    sent_message = await call.bot.send_document(
        chat_id=call.message.chat.id,
        document=('Passwords.json', json_content),
        caption=f'Json file for <code>@{call.from_user.username}</code>',
        parse_mode='HTML'
    )

    return sent_message
