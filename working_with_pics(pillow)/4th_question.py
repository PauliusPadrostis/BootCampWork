"""
Write a program that, given a photo and RGB values, will adjust each pixel accordingly. I.e. if the value
is positive - it would be added, if it is negative - it would be subtracted. Do not allow final values
to be less than zero and greater than 255!
"""

from PIL import Image, ImageFilter, ImageEnhance, ImageOps


def line(num):
    if num > 255:
        return 255
    elif num < 0:
        return 0
    return num


def change_colors_by_pixel(pic, red, green, blue):
    image = Image.open(pic)
    data = image.getdata()
    new_data = []
    for pixel in data:
        r = line(pixel[0] + red)
        g = line(pixel[1] + green)
        b = line(pixel[2] + blue)
        new_data.append((r, g, b))
    image.putdata(new_data)
    image.show()


change_colors_by_pixel("dog.jpg", red=-150, green=-250, blue=-150)
