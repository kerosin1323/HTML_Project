from PIL import Image

im = Image.open("KE.png")
size = im.size
im2 = im.crop((25, 35, 110, 90))
im2.save('8.png')