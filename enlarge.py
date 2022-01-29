from images import Image

im= Image('ezgif.com-gif-maker.gif')

width = im.getWidth()
height = im.getHeight()

print(width)
print(height)

print(im.getPixel(40,60))

for i in range(width):
    for j in range(height):
        im.width(width+10)



i.draw()