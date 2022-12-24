import random
import textwrap
import warnings

from PIL import Image, ImageFont, ImageDraw

from bot.bot_main.for_photo_creation.photo_size import write_to_txt


def create_new_photo(user_data=' ', pos_x=0, pos_y=0, img_width=0, img_height=0, img_font=20):

    warnings.filterwarnings('ignore', category=DeprecationWarning)

    used_image = Image.open('imgs/test.jpg')

    if img_width == 0 and img_height == 0:
        width, height = used_image.size
        used_image = change_size_statement(width, height, used_image)
    else:
        used_image = change_size_statement(img_width, img_height, used_image)

    IMAGE_WIDTH, IMAGE_HEIGHT = used_image.size
    write_to_txt(IMAGE_WIDTH, IMAGE_HEIGHT)

    default_font_size = 20
    font_size = change_font_size(img_font, default_font_size)

    if ((pos_x or pos_y) < 0) or (pos_x > IMAGE_WIDTH or pos_y > pos_y):
        return True

    draw = ImageDraw.Draw(used_image)
    font = ImageFont.truetype('fonts/AdverGothicC.ttf', font_size)

    random_color = change_color()

    lines = []
    line = ''
    line_height = font.getsize('A')[1]

    for word in user_data.split(' '):
        if draw.textsize(line + ' ' + word, font=font)[0] <= IMAGE_WIDTH - pos_x:
            line += ' ' + word
        else:
            lines.append(line.strip())
            line = word

    if line:
        lines.append(line.strip())

    for line in lines:
        draw.text((pos_x, pos_y), line, fill=random_color, font=font)
        pos_y += line_height + (font_size * 0.2)

    used_image.save('imgs/result.jpg')


def create_new_photo_auto_config(user_data=' '):
    warnings.filterwarnings('ignore', category=DeprecationWarning)

    used_image = Image.open('imgs/test_auto_conf.jpg')
    IMAGE_WIDTH, IMAGE_HEIGHT = used_image.size

    draw = ImageDraw.Draw(used_image)
    # 20 big 'A' with font size = 50 is width 722. One 'A' == 36
    if IMAGE_WIDTH <= 500:
        font_size = int(IMAGE_WIDTH * 0.06)
        wrap_width = font_size
    else:
        font_size = int(IMAGE_WIDTH * 0.04)
        wrap_width = int(font_size * 0.8)

    print(IMAGE_WIDTH, IMAGE_HEIGHT)
    text_wrap = textwrap.wrap(user_data, width=wrap_width)
    font = ImageFont.truetype('fonts/AdverGothicC.ttf', font_size)

    current_height, padding = IMAGE_HEIGHT / 1.75, 10
    font_color = change_color()
    for new_line in text_wrap:
        text_width, text_height = draw.textsize(new_line, font=font)
        draw.text(
            ((IMAGE_WIDTH - text_width) / 2, current_height),
            new_line,
            font=font,
            fill=font_color
        )
        current_height += text_height + padding

    used_image.save('imgs/result_auto_conf.jpg')


def change_size_statement(new_width: int, new_height: int, image: Image) -> Image:
    width, height = image.size

    if new_width == width and new_height == height:
        return image
    else:
        return image.resize((new_width, new_height))


def change_font_size(new_font_size: int, default_font_size: int) -> int:
    if new_font_size == default_font_size:
        return default_font_size
    else:
        return new_font_size


def change_color() -> tuple:
    rand_col_1 = random.randint(128, 255)
    rand_col_2 = random.randint(128, 255)
    rand_col_3 = random.randint(128, 255)

    return rand_col_1, rand_col_2, rand_col_3
