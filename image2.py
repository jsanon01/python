from PIL import Image

im = Image.open("big_data.png")
im.rotate(45).show()
