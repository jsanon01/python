"""
I want to import Python Library
I want to initalize 'img' to open image file
I want to calculate percentage and size
I want to save image in another file

Reference: https://opensource.com/life/15/2/resize-images-python
"""

import PIL
from PIL import Image


basewidth = 300

img = Image.open('traffic-lights.jpg')

wpercent = (basewidth / float(img.size[0]))

hsize = int((float(img.size[1]) * float(wpercent)))

img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)

img.save('traffic-lights2.jpg')

