from images import Image

i = Image('ezgif.com-gif-maker (1).gif')

width = i.getWidth()
height = i.getHeight()

print(width)
print(height)

print(i.getPixel(40,60))

i.setPixel(40,60,(250,230,216))



i.draw()
i.clone()
print(i)

