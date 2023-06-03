from PIL import Image

im = Image.open("../image.jpeg")
im2 = im.resize((400, 400))
im2.save('6.jpg')