from enum import Enum


class Command(str, Enum):
    START = "start"
    HELP = "help"
    TIME = "time"
    CURRENT_WEATHER = "current_weather"
    CURRENCY_CONVERTER = "currency_converter"
    DATE_CALCULATOR = "date_calculator"
    TASK_SCHEDULER = "task_scheduler"
    IMAGE_EDITOR = "image_editor"
    PASSWORD_GENERATOR = "password_generator"
    KEYWORD_LIST = "keyword_list"

    @classmethod
    def __len__(cls) -> int:
        return len(cls._member_names_)
