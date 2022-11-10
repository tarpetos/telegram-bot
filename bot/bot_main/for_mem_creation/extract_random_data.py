from random import choice
import mysql
import mysql.connector


# get bullshit
def get_bullshit():
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='1111',
        database='bot_db'
    )

    cursor = mydb.cursor()

    cursor.execute(
        """
        SELECT bullshit FROM bot
        ORDER BY id;
        """
    )

    result = cursor.fetchall()

    return result


# get sticker
def get_sticker():
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='1111',
        database='bot_db'
    )

    cursor = mydb.cursor()

    cursor.execute(
        """
        SELECT sticker FROM stickers
        ORDER BY id;
        """
    )

    result = cursor.fetchall()

    return result


# get conversation data
def get_conversation_data():
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='1111',
        database='bot_db'
    )

    cursor = mydb.cursor()

    cursor.execute(
        """
        SELECT conversation FROM conversation_data
        ORDER BY id;
        """
    )

    result = cursor.fetchall()

    return result


# choose random bullshit, sticker, conversation data
def get_random_data(data_arg):
    result = choice(data_arg)
    return result[0]
