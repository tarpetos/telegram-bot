from aiogram import executor

from bot.bot_main import main_objects_initialization
from bot.bot_main.commands_and_keywords import main_commands, random_numbers_generation_command, user_info_command, \
    sticker_command, keywords_command, time_commands, add_text_to_photo_command,  weather_command, \
    youtube_search_command, currency_converter_command, task_scheduler_command, password_generator_command, \
    keywords_for_interaction

bot = main_objects_initialization.bot
dp = main_objects_initialization.dp


def main():
    executor.start_polling(dp, skip_updates=True)


if __name__ == '__main__':
    main()
