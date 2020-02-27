from PIL import Image

im = Image.open("test.jpg")
w, h = im.size
im = im.crop((0,0,w, h - 20))

print(im.size)