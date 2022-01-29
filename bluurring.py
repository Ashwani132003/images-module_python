
from images import Image
im = Image('ezgif.com-gif-maker.gif')

def tripleSum(triple1,trple2):

 (r1, g1, b1) = triple1
 (r2, g2, b2) = triple2
 return (r1 + r2, g1 + g2, b1 + b2)

for y in range(1, im.getHeight() - 1):
    for x in range(1, im.getWidth() - 1):
         oldP = im.getPixel(x, y)
         left = im.getPixel(x - 1, y) # To left
         right = im.getPixel(x + 1, y) # To right
         top = im.getPixel(x, y - 1) # Above
         bottom = im.getPixel(x, y + 1) # Below
         sums = reduce(tripleSum,
         [oldP, left, right, top, bottom])
#2
         averages = tuple(map(lambda x: x // 5, sums))
#3
         im.setPixel(x, y, averages)

im.draw()
 