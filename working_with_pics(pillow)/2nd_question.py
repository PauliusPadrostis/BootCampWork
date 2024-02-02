"""
Create a function that accepts

picture values of contrast, chrominance, sharpness and brightness
save or not value and adjust the picture settings accordingly. It would show the picture on the screen.
Depending on the selection, saved or not.
Save to a file by appending e.g. to the original name. '_modified', say dog_modified.jpg.
"""

from PIL import Image, ImageFilter, ImageEnhance


def img_corr(pic, contrast, color, sharpness, brightness):
    image = Image.open(f"{pic}.jpg")

    image = ImageEnhance.Contrast(image).enhance(contrast)
    image = ImageEnhance.Color(image).enhance(color)
    image = ImageEnhance.Sharpness(image).enhance(sharpness)
    image = ImageEnhance.Brightness(image).enhance(brightness)

    image.show()

    save_mode = input("Save picture? (Y/N): ")
    if save_mode:
        image.save(f"{pic}_modified.jpg")


image = "dog"
img_corr(image, 1.1, 1.5, 2, 2)
