import json
from config import CURRENCY_URL, BITCOIN_URL
from urllib.request import urlopen

response = urlopen(CURRENCY_URL)
data_json_list = json.loads(response.read())

bitcoin_response = urlopen(BITCOIN_URL)
bitcoin_json = json.loads(bitcoin_response.read())


def find_dollars_buy_in_hryvnias() -> float:
    return 1 / float(data_json_list[0]['buy'])


def find_euros_buy_in_hryvnias() -> float:
    return 1 / float(data_json_list[1]['buy'])


def find_dollars_buy_in_euros() -> float:
    return float(data_json_list[1]['buy']) / float(data_json_list[0]['buy'])


def find_hryvnias_buy_in_euros() -> float:
    return float(data_json_list[1]['buy'])


def find_euros_buy_in_dollars() -> float:
    return float(data_json_list[0]['buy']) / float(data_json_list[1]['buy'])


def find_hryvnias_buy_in_dollars() -> float:
    return float(data_json_list[0]['buy'])


def find_dollars_sale_in_hryvnias() -> float:
    return 1 / float(data_json_list[0]['sale'])


def find_euros_sale_in_hryvnias() -> float:
    return 1 / float(data_json_list[1]['sale'])


def find_dollars_sale_in_euros() -> float:
    return float(data_json_list[1]['sale']) / float(data_json_list[0]['sale'])


def find_hryvnias_sale_in_euros() -> float:
    return float(data_json_list[1]['sale'])


def find_euros_sale_in_dollars() -> float:
    return float(data_json_list[0]['sale']) / float(data_json_list[1]['sale'])


def find_hryvnias_sale_in_dollars() -> float:
    return float(data_json_list[0]['sale'])


def bitcoin_price() -> float:
    return float(bitcoin_json['price'])
