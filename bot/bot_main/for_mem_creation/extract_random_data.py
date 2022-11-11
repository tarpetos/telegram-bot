from random import choice


# choose random bullshit, sticker, conversation data
def get_random_data(data_arg):
    result = choice(data_arg)
    return result[0]
