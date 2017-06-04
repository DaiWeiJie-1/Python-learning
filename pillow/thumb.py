from PIL import Image

def thumb():
    im = Image.open('image1.png')
    print(im.format,im.size,im.mode)
    im.thumbnail((100,100))
    im.save('thumb.png','PNG')


thumb()

