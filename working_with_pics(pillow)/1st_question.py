"""
We have a logo with a translucent background, size 128*128. Download it and redo it to remove 28 rows of pixels
each from the top and bottom. Save it as we will use it for the following tasks.
"""

from PIL import Image

box = (0, 28, 128, 100)
image = Image.open("logo.png")
result = image.crop(box)
result.show()
result.save("logo_m.png")
