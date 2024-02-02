"""
Write a program that, given a picture and given the R G B values
of a pixel, would change all pixels with any one value above the specified limit to white and the rest to black.
"""

from PIL import Image


def turn_binary(image, r, g, b):
    image = Image.open(image)
    data = image.getdata()
    new_data = []
    black = (0, 0, 0)
    white = (255, 255, 255)
    for pixel in data:
        if pixel[0] >= r or pixel[1] >= g or pixel[2] >= b:
            new_data.append(white)
        else:
            new_data.append(black)
    image.putdata(new_data)
    image.show()


turn_binary("dog.jpg", 200, 170, 120)
