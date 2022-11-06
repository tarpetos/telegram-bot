from PIL import Image, ImageFont, ImageDraw
import extract_random_data


def create_meme():
    mem_image = Image.open('img/test.jpg')
    mem_image = change_size_statement(mem_image)

    title_font = ImageFont.truetype('fonts/PlayfairDisplay-Regular.ttf', change_font_size(mem_image))

    data = extract_random_data.get_bullshit()
    title_text = f'{extract_random_data.get_random_data(data)}'

    image_editable = ImageDraw.Draw(mem_image)

    image_editable.text(change_font_place(mem_image, image_editable, title_text), title_text, font=title_font)
    mem_image.save('img/result.jpg')


def change_size_statement(mem_image):
    width, height = mem_image.size
    if (width or height) < 500:
        new_size = (500, 500)
        mem_image = mem_image.resize(new_size)

    return mem_image


def replace_string(title_text):
    result = ''
    for symbols in range(0, len(title_text)):
        result += title_text.replace(title_text, 'a')

    return result


def change_font_place(mem_image, image_editable, title_text):
    photo_width, photo_height = mem_image.size

    temp_str = replace_string(title_text)
    text_width, text_height = image_editable.textsize(temp_str)

    return ((photo_width / 2) - (text_width * 2.25)), ((photo_height - text_height) / 1.25)


def change_font_size(mem_image):
    width, height = mem_image.size

    if (width and height) < 500:
        return 30
    elif 1000 > (width and height) >= 500:
        return 60
    else:
        return 90
