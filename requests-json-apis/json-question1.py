"""
download this file. write a program that will read the contents of a file and reformat it like this:

{
  "colors": [
    {
      "color": "black",
      "rgb": "255, 255, 255",
      "hex": "#000"
    },
    {
      "color": "white",
      "rgb": "0, 0, 0",
      "hex": "#FFF"
    }
etc.

Save the result to a .json file on your computer.
"""


import json

reformatted_dict = {
    "colors": []
}

with open('style.json', 'r') as file:
    str_style = file.read()

    str_style_dict = json.loads(str_style)

    for color_info in str_style_dict['colors']:
        new_color_info = {
            'color': color_info['color'],
            'rgb': ', '.join(map(str, color_info['code']['rgba'][:3])),
            'hex': color_info['code']['hex']
        }
        reformatted_dict['colors'].append(new_color_info)

with open('new_style_json.json', 'w') as file:
    json.dump(reformatted_dict, file, indent=3)


