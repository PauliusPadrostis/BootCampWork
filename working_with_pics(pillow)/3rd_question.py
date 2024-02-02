"""
Create a program that, given a link to a directory, will iterate through all the files in it, select the photos,
resize them to the height you specify while keeping the aspect ratio, and place the logo you saved in the first task
in the lower right corner of each photo. Use .resize as the photo may need to be enlarged, not necessarily reduced.
The program must save the changed photos to the 'optimized' directory created in the same directory.
"""

from PIL import Image, ImageFilter, ImageEnhance, ImageOps
import os

pic_location = "C:\\Users\\ITWORK\\Desktop\\pictures"


def resize_n_add_logo(cat_location, width, height, logo):
    os.chdir(cat_location)
    pics = os.listdir()
    os.mkdir("Optimized")

    for pic in pics:
        image = Image.open(pic)
        log = Image.open(logo)
        image = ImageOps.contain(image, (width, height))
        logo_location = (image.size[0] - log.size[0], image.size[1] - log.size[1], image.size[0], image.size[1])
        image.paste(log, logo_location, log)
        os.chdir(f"{pic_location}\\Optimized")
        image.save(f"{pic}")
        os.chdir(cat_location)

    os.chdir("C:\\Users\\ITWORK\\PycharmProjects\\working_with_pics\\")


resize_n_add_logo(pic_location, 2000, 2000, "logo.png")
