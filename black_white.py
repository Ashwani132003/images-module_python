from images import Image

im= Image('ezgif.com-gif-maker (1).gif')

width = im.getWidth()
height = im.getHeight()

for i in range(width):
    for j in range(height):
        (r,g,b) = im.getPixel(i,j)
        average = (r+g+b)//3
        if(average<128):
            im.setPixel(i,j,(0,0,0))
        else:
            im.setPixel(i,j,(255,255,255))

im.draw()