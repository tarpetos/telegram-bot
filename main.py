from aiogram import executor

from bot.bot_main import main_objects_initialization
from bot.bot_main.main_bot_modules import main_commands, random_numbers_generation, show_user_info, \
    time_commands, sticker_command, weather_command, currency_converter, youtube_search_command, get_keyword_command,\
    password_generator_command, add_text_to_photo_command, task_scheduler, keywords_for_interaction

bot = main_objects_initialization.bot
dp = main_objects_initialization.dp


def main():
    executor.start_polling(dp, skip_updates=True)


if __name__ == '__main__':
    main()
