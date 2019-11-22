from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')

filterd_img = img.filter(ImageFilter.BLUR)
filterd_img.save("blur.png",'png')

filterd_img = img.convert('L')
box = (100,100,400,400)
region = filterd_img.crop(box)
region.show()

# filterd_img.save("gre.png",'png')

# print(img.format)
# print(img.size)
# print(img.mode)

# print(dir(img))

# img.show()
# filterd_img2.show()

img.rotate(90).show()
img.show()
img.resize((300,300)).show()

