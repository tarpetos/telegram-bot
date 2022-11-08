import json
from config import CURRENCY_URL
from urllib.request import urlopen

response = urlopen(CURRENCY_URL)
data_json_list = json.loads(response.read())


def find_dollars_buy_in_hryvnias() -> str:
    return format(round(1 / float(data_json_list[0]['buy']), 4), '.4f')


def find_euros_buy_in_hryvnias() -> str:
    return format(round(1 / float(data_json_list[1]['buy']), 4), '.4f')


def find_dollars_buy_in_euros() -> str:
    return format(round(float(data_json_list[1]['buy']) / float(data_json_list[0]['buy']), 4), '.4f')


def find_hryvnias_buy_in_euros() -> str:
    return format(round(float(data_json_list[1]['buy']), 4), '.3f')


def find_euros_buy_in_dollars() -> str:
    return format(round(float(data_json_list[0]['buy']) / float(data_json_list[1]['buy']), 4), '.4f')


def find_hryvnias_buy_in_dollars() -> str:
    return format(round(float(data_json_list[0]['buy']), 4), '.3f')


########################################################################################################################
########################################################################################################################


def find_dollars_sale_in_hryvnias() -> str:
    return format(round(1 / float(data_json_list[0]['sale']), 4), '.4f')


def find_euros_sale_in_hryvnias() -> str:
    return format(round(1 / float(data_json_list[1]['sale']), 4), '.4f')


def find_dollars_sale_in_euros() -> str:
    return format(round(float(data_json_list[1]['sale']) / float(data_json_list[0]['sale']), 4), '.4f')


def find_hryvnias_sale_in_euros() -> str:
    return format(round(float(data_json_list[1]['sale']), 4), '.3f')


def find_euros_sale_in_dollars() -> str:
    return format(round(float(data_json_list[0]['sale']) / float(data_json_list[1]['sale']), 4), '.4f')


def find_hryvnias_sale_in_dollars() -> str:
    return format(round(float(data_json_list[0]['sale']), 4), '.3f')


def bitcoin_buy() -> float:
    return round(float(data_json_list[3]['buy']), 4)


def bitcoin_sale() -> float:
    return round(float(data_json_list[3]['sale']), 4)
