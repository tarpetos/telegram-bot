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

    dominant_color = get_image_general_color(used_image, IMAGE_WIDTH, IMAGE_HEIGHT)
    font_color = visible_color(dominant_color)

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
        draw.text((pos_x, pos_y), line, fill=font_color, font=font)
        pos_y += line_height + (font_size * 0.2)

    used_image.save('imgs/result.jpg')


def create_new_photo_auto_config(clr_choice: bool, user_data=' '):
    warnings.filterwarnings('ignore', category=DeprecationWarning)

    used_image = Image.open('imgs/test_auto_conf.jpg')
    IMAGE_WIDTH, IMAGE_HEIGHT = used_image.size

    draw = ImageDraw.Draw(used_image)
    # 20 big 'A' with font size = 50 is width 722. One 'A' == 36
    if IMAGE_WIDTH <= 500:
        font_size = int(IMAGE_WIDTH * 0.1)
        wrap_width = int(font_size * 0.8)
    elif IMAGE_WIDTH <= 1000:
        font_size = int(IMAGE_WIDTH * 0.05)
        wrap_width = int(font_size * 0.8)
    else:
        font_size = int(IMAGE_WIDTH * 0.03)
        wrap_width = int(font_size * 0.8)

    text_wrap = textwrap.wrap(user_data, width=wrap_width)
    font = ImageFont.truetype('fonts/AdverGothicC.ttf', font_size)

    current_height, padding = IMAGE_HEIGHT - font_size, 10

    generalized_color = get_image_general_color(used_image, IMAGE_WIDTH, IMAGE_HEIGHT)
    if clr_choice:
        font_color = visible_color(generalized_color)
    else:
        font_color = change_color(generalized_color)

    for new_line in text_wrap[::-1]:
        text_width, text_height = draw.textsize(new_line, font=font)
        draw.text(
            ((IMAGE_WIDTH - text_width) / 2, current_height),
            new_line,
            font=font,
            fill=font_color
        )
        current_height -= text_height + padding

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


def get_image_general_color(image: Image, width, height) -> tuple:
    colors = image.getcolors(image.size[0] * image.size[1])
    colors.sort(key=lambda t: t[0], reverse=True)

    full_pixels_num = width * height
    sum_red = 0
    sum_green = 0
    sum_blue = 0

    for color_counter, color in enumerate(colors, 1):
        color_coeff = 1 + (color[0] / full_pixels_num)
        sum_red += int(color[1][0] * color_coeff)
        sum_green += int(color[1][1] * color_coeff)
        sum_blue += int(color[1][2] * color_coeff)

    color_number = len(colors) * 2
    result_color = sum_red // color_number, sum_green // color_number, sum_blue // color_number

    return result_color

def visible_color(background: tuple) -> tuple:
    red_clr = 255 - background[0]
    green_clr = 255 - background[1]
    blue_clr = 255 - background[2]
    opposite_bg_color = red_clr, green_clr, blue_clr

    return opposite_bg_color


def change_color(background: tuple) -> tuple:
    brightness = (background[0] * 299 + background[1] * 587 + background[2] * 114) // 1000

    if brightness < 128:
        rand_col_1 = random.randint(128, 255)
        rand_col_2 = random.randint(128, 255)
        rand_col_3 = random.randint(128, 255)
    else:
        rand_col_1 = random.randint(0, 127)
        rand_col_2 = random.randint(0, 127)
        rand_col_3 = random.randint(0, 127)

    return rand_col_1, rand_col_2, rand_col_3

