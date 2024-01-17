from .keyboard_base import KeyboardBuilder
from ..enums.keyboard_callbacks import ConverterCallbackStorage

main_converter_menu = KeyboardBuilder()
main_converter_menu.add_column_button("Exchange rate", ConverterCallbackStorage.CURRENCY_RATE)
main_converter_menu.add_row_button("Converter", ConverterCallbackStorage.CURRENCY_CONVERTER)
main_converter_menu.add_column_button("Close keyboard", ConverterCallbackStorage.CLOSE_CONVERTER)

currency_rate_menu = KeyboardBuilder()
currency_rate_menu.add_column_button("Back", ConverterCallbackStorage.MAIN_CONVERTER_MENU_BACK)

convert_menu = KeyboardBuilder()
convert_menu.add_column_button("Dollar conversion", ConverterCallbackStorage.CONVERT_DOLLAR)
convert_menu.add_column_button("Euro conversion", ConverterCallbackStorage.CONVERT_EURO)
convert_menu.add_column_button("Hryvnia conversion", ConverterCallbackStorage.CONVERT_HRYVNIA)
convert_menu.add_column_button("Back", ConverterCallbackStorage.MAIN_CONVERTER_MENU_BACK)
