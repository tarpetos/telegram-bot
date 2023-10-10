import json
from typing import Any

from bot.config import CURRENCY_URL, BITCOIN_URL
from urllib.request import urlopen


def get_response_data(url: str) -> Any:
    response = urlopen(url)
    data_json_list = json.loads(response.read())
    return data_json_list


def find_dollars_buy_in_hryvnias() -> float:
    data_json_list = get_response_data(CURRENCY_URL)
    return 1 / float(data_json_list[1]["buy"])


def find_euros_buy_in_hryvnias() -> float:
    data_json_list = get_response_data(CURRENCY_URL)
    return 1 / float(data_json_list[0]["buy"])


def find_dollars_buy_in_euros() -> float:
    data_json_list = get_response_data(CURRENCY_URL)
    return float(data_json_list[0]["buy"]) / float(data_json_list[1]["buy"])


def find_hryvnias_buy_in_euros() -> float:
    data_json_list = get_response_data(CURRENCY_URL)
    return float(data_json_list[0]["buy"])


def find_euros_buy_in_dollars() -> float:
    data_json_list = get_response_data(CURRENCY_URL)
    return float(data_json_list[1]["buy"]) / float(data_json_list[0]["buy"])


def find_hryvnias_buy_in_dollars() -> float:
    data_json_list = get_response_data(CURRENCY_URL)
    return float(data_json_list[1]["buy"])


def find_dollars_sale_in_hryvnias() -> float:
    data_json_list = get_response_data(CURRENCY_URL)
    return 1 / float(data_json_list[1]["sale"])


def find_euros_sale_in_hryvnias() -> float:
    data_json_list = get_response_data(CURRENCY_URL)
    return 1 / float(data_json_list[0]["sale"])


def find_dollars_sale_in_euros() -> float:
    data_json_list = get_response_data(CURRENCY_URL)
    return float(data_json_list[0]["sale"]) / float(data_json_list[1]["sale"])


def find_hryvnias_sale_in_euros() -> float:
    data_json_list = get_response_data(CURRENCY_URL)
    return float(data_json_list[0]["sale"])


def find_euros_sale_in_dollars() -> float:
    data_json_list = get_response_data(CURRENCY_URL)
    return float(data_json_list[1]["sale"]) / float(data_json_list[0]["sale"])


def find_hryvnias_sale_in_dollars() -> float:
    data_json_list = get_response_data(CURRENCY_URL)
    return float(data_json_list[1]["sale"])


# def bitcoin_price() -> float:
#     bitcoin_json_list = get_response_data(BITCOIN_URL)
#     return float(bitcoin_json_list["price"])


def bitcoin_price() -> float:
    bitcoin_json_list = get_response_data(BITCOIN_URL)
    return float(bitcoin_json_list["bpi"]["USD"]["rate_float"])
