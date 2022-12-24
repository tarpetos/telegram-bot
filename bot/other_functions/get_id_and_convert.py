def get_id_from_str(table_name):
    return int(
        ''.join(
            decimal
            for decimal in table_name
            if decimal.isdecimal()
        )
    )
