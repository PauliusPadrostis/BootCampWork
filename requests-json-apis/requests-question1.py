"""
https://cataas.com/cat uploads a different cat photo every time. Write a function that, after entering the parameters
 of how many photos we want, would save them to our computer.
"""

import requests
import os


def get_cat_photos(num_photos):
    os.mkdir(f'{num_photos}_cats')
    os.chdir(f'C:\\Users\\ITWORK\\PycharmProjects\\requests-json-apis\\{num_photos}_cats')

    for item in range(num_photos):
        r = requests.get('https://cataas.com/cat')
        with open(f'cat_{item}.png', 'wb' ) as cat_pic:
            cat_pic.write(r.content)


get_cat_photos(5)





