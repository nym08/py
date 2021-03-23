from PIL import Image, ImageFont, ImageDraw
import time

header_path = 'img\\header.png'
header = Image.open(header_path).copy()

body_path = 'img\\body.png'
body = Image.open(body_path).copy()


def add_text_to_image(img, text, font_path, font_size, font_color, height, width, max_length=740):
    position = (width, height)
    font = ImageFont.truetype(font_path, font_size)
    draw = ImageDraw.Draw(img)
    if draw.textsize(text, font=font)[0] > max_length:
        while draw.textsize(text + '…', font=font)[0] > max_length:
            text = text[:-1]
        text = text + '…'

    draw.text(position, text, font_color, font=font)

    return img

user_name = 'unko'
font_path = "C:\\Windows\\Fonts\\Meiryo UI\\meiryo.ttc"
font_size = 10
font_color = (255, 255, 255)
height = 0
width = 0
img = add_text_to_image(header, user_name, font_path,
                        font_size, font_color, height, width)

img.save('output\\unko' + str(time.time()) + '.png')
