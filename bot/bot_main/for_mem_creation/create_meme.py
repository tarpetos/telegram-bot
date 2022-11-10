import random
import textwrap
import warnings

from bot.bot_main.for_mem_creation import extract_random_data

from PIL import Image, ImageFont, ImageDraw


def create_meme():
    warnings.filterwarnings('ignore', category=DeprecationWarning)

    mem_image = Image.open('img/test.jpg')
    data = extract_random_data.get_bullshit()
    mem_text = f'{extract_random_data.get_random_data(data)}'.upper()

    mem_image = change_size_statement(mem_image)
    text_wrap = textwrap.wrap(mem_text, width=text_wrap_width(mem_image))

    IMAGE_WIDTH, IMAGE_HEIGHT = mem_image.size
    draw = ImageDraw.Draw(mem_image)
    font = ImageFont.truetype('fonts/AdverGothicC.ttf', change_font_size(mem_image))

    rand_col_1 = random.randint(0, 255)
    rand_col_2 = random.randint(0, 255)
    rand_col_3 = random.randint(0, 255)

    current_height, padding = IMAGE_HEIGHT / 1.3, 10
    print(text_wrap)
    for new_line in text_wrap:
        print(new_line)
        text_width, text_height = draw.textsize(new_line, font=font)
        draw.text(((IMAGE_WIDTH - text_width) / 2, current_height),
                  new_line,
                  font=font,
                  fill=(rand_col_1, rand_col_2, rand_col_3))
        current_height += text_height + padding

    mem_image.save('img/result.jpg')


def change_size_statement(mem_image: Image) -> Image:
    width, height = mem_image.size

    if width >= 500 and height < 400:
        return mem_image.resize((width * 2, int(height * 1.75)))
    elif height >= 500 and width < 400:
        return mem_image.resize((int(width * 1.75), height * 2))
    elif height == width or (width > 500 and height > 500):
        return mem_image
    else:
        return mem_image.resize((500, 500))


def change_font_size(mem_image: Image) -> int:
    width, height = mem_image.size

    if width >= 500 and height < 400:
        return 20
    elif height >= 500 and width < 400:
        return 20
    elif height == width and height < 500 and width < 500:
        return 20
    elif width > 500 and height > 500:
        return 30
    else:
        return 30


def text_wrap_width(mem_image: Image) -> int:
    temp = change_font_size(mem_image)
    print('Font size:', temp)
    if temp == 30:
        return 15
    else:
        return 20

