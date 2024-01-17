import re
import requests
from bs4 import BeautifulSoup as Bs
from typing import List, Tuple, Any


def parse_temp_at_time(url: str) -> str:
    r = requests.get(url)
    html = Bs(r.content, "html.parser")
    time = html.select(".imgBlock p")
    temp_at_time = html.select(".today-temp")

    return time[0].text + ": " + temp_at_time[0].text


def parse_minmax_temp(url: str) -> str:
    r = requests.get(url)
    html = Bs(r.content, "html.parser")
    min_temp = html.select(".min span")
    max_temp = html.select(".max span")

    return (
            "Min temperature: "
            + min_temp[0].text
            + "C\n"
            + "Max temperature: "
            + max_temp[0].text
            + "C\n"
    )


def parse_today_temp(url: str) -> list:
    r = requests.get(url)
    html = Bs(r.content, "html.parser")

    today_temp = html.select(".temperature td")

    new_list = []
    for td in today_temp:
        new_list.append(td.text)

    return new_list


def list_of_tuples(url: str) -> List[Tuple[Any, Any]]:
    initial_list = parse_today_temp(url)
    new_list = [
        (initial_list[i - 1], initial_list[i]) for i in range(1, len(initial_list), 2)
    ]
    return new_list


def parse_average_precipitation_probability(url: str) -> int:
    r = requests.get(url)
    html = Bs(r.content, "html.parser")

    precipitation_probability = html.select("tr:nth-child(8) td")
    count = 0
    temp = 0
    precipitation_probability_list = []
    for td in precipitation_probability:
        if td.text == "-":
            precipitation_probability_list.append(0)
            temp = temp
        else:
            precipitation_probability_list.append(int(td.text))
            temp += int(td.text)
        count += 1

    return max(precipitation_probability_list)


def check_for_negative_temp(temperature: float) -> str:
    if temperature > 0:
        return "+" + str(temperature) + "°C"
    else:
        return str(temperature) + "°C"


def find_average_temp_between_two(url: str) -> List[str]:
    temp_lst = list_of_tuples(url)
    result_list = []

    for i in temp_lst:
        sum_of_two = 0

        for j in range(2):
            result = int(re.search(r"-*\d+", i[j]).group())
            sum_of_two += result

        result_list.append(check_for_negative_temp(sum_of_two / 2))

    return result_list


def average_day_temp(url: str) -> str:
    average_temp = 0
    count = 0
    for i in parse_today_temp(url):
        average_temp += int(re.search(r"-*\d+", i).group())
        count += 1

    return (
            "Average temperature: " + check_for_negative_temp(average_temp / count) + "\n\n"
    )
