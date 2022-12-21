import re


def exctract_from_user_input_days_num(user_input):
    days_num_pattern = re.compile('[1-9]+[0-9]*')

    days_num = re.findall(days_num_pattern, user_input)
    return int(days_num[0])


def exctract_from_user_input_days_and_date(user_input):
    days_num = exctract_from_user_input_days_num(user_input)
    date_pattern = re.compile('([1-9]|0[1-9]|[1-2][0-9]|3[0-1]).([1-9]|0[1-9]|1[0-2]).([1-9]+.*[0-9]+)')

    result_date = re.findall(date_pattern, user_input)

    int_list = []
    for date_element in result_date[0]:
        int_list.append(int(date_element))
    result_date = int_list

    return days_num, result_date
