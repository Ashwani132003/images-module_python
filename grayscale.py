from images import Image

im = Image('ezgif.com-gif-maker (1).gif')

for i in range(im.getWidth()):
    for j in range(im.getHeight()):
        r,g,b = im.getPixel(i,j)
        r = int(r*0.587)
        g = int(g*0.299)
        b = int(b*0.114)
        lum = r + g + b
        im.setPixel(i,j,(lum, lum, lum))
im.draw()
