from enum import Enum


class CallbackDataStorage(str, Enum):
    @classmethod
    def __len__(cls) -> int:
        return len(cls._member_names_)

    def __str__(self):
        return self.value


class ConverterCallbackStorage(CallbackDataStorage):
    CONVERT_DOLLAR = "convert_dollar"
    CONVERT_EURO = "convert_euro"
    CONVERT_HRYVNIA = "convert_hryvnia"
    CURRENCY_RATE = "currency_rate"
    CURRENCY_CONVERTER = "currency_converter"
    CLOSE_CONVERTER = "close_converter"
    MAIN_CONVERTER_MENU_BACK = "main_converter_menu_back"


class GeneratorCallbackStorage(CallbackDataStorage):
    ...


class SchedulerCallbackStorage(CallbackDataStorage):
    ...
