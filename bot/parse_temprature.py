import requests
from bs4 import BeautifulSoup as BS


def parse_avarage_today_temp(url: str) -> str:
    r = requests.get(url)
    html = BS(r.content, 'html.parser')
    avarage_today_temp = html.select('.today-temp')
    print('Середня температура сьогодні:', avarage_today_temp[0].text)

    return avarage_today_temp[0].text


def parse_today_temp(url: str) -> list:
    r = requests.get(url)
    html = BS(r.content, 'html.parser')

    today_temp = html.select('.temperature td')

    new_list = []
    for td in today_temp:
        new_list.append(td.text)

    new_list = [(new_list[i - 1], new_list[i]) for i in range(1, len(new_list), 2)]

    return new_list


def parse_avarage_precipitation_probability(url: str) -> int:
    r = requests.get(url)
    html = BS(r.content, 'html.parser')

    precipitation_probability = html.select('tr:nth-child(8) td')
    count = 0
    temp = 0
    precipitation_probability_list = []
    for td in precipitation_probability:
        if td.text == '-':
            precipitation_probability_list.append(0)
            temp = temp
        else:
            precipitation_probability_list.append(int(td.text))
            temp += int(td.text)
        count += 1

    return max(precipitation_probability_list)
