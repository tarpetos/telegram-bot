def check_year(years):
    years_message = str(years)

    if years_message.endswith(('11', '12', '13', '14')):
        years_message = 'років'
    elif years_message.endswith('1'):
        years_message = 'рік'
    elif years_message.endswith(('2', '3', '4')):
        years_message = 'роки'
    else:
        years_message = 'років'

    return years_message


def check_month(months):
    months_message = str(months)

    if months_message.endswith(('11', '12')):
        months_message = 'місяців'
    elif months_message.endswith('1'):
        months_message = 'місяць'
    elif months_message.endswith(('2', '3', '4')):
        months_message = 'місяці'
    else:
        months_message = 'місяців'

    return months_message


def check_day(days):
    days_message = str(days)

    if days_message.endswith(('11', '12', '13', '14')):
        days_message = 'днів'
    elif days_message.endswith('1'):
        days_message = 'день'
    elif days_message.endswith(('2', '3', '4')):
        days_message = 'дні'
    else:
        days_message = 'днів'

    return days_message
