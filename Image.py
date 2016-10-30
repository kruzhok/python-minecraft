from mcpi.minecraft import Minecraft
import time
import random
ImageName = input("Image name:")
verticalOrHorisontal = input("for vertical image type \"vertical\". For horizontal any other input: ")
if verticalOrHorisontal=="vertical":
    print("You choosed vertical image. Type coordinates for left bottom edge")
else:
    print("You choosed vertical image. Type coordinates for left top edge")
X0 = int(input("X0:"))
Y0 = int(input("Y0:"))
Z0 = int(input("Z0:"))
def Image(ImageName,X0,Y0,Z0,verticalOrHorisontal):
    from PIL import Image
    import math
    mc = Minecraft.create()
    white = [221,221,221,0]#rgb, id
    orange = [219,125,62,1]#rgb, id
    magneta = [179,80,188,2]#rgb, id
    lightBlue = [107,138,201,3]#rgb, id
    yellow = [177,166,39,4]#rgb, id
    lime = [65,174,56,5]#rgb, id
    pink = [208,132,153,6]#rgb, id
    gray = [64,64,64,7]#rgb, id
    lightGray = [154,161,161,8]#rgb, id
    cyan = [46,110,137,9]#rgb, id
    purple = [126,61,181,10]#rgb, id
    blue = [46,56,141,11]#rgb, id
    brown = [79,50,31,12]#rgb, id
    green = [53,70,27,13]#rgb, id
    red = [150,52,48,14]#rgb, id
    black = [25,22,22,15]#rgb, id
    colors = [white,orange,magneta,lightBlue,yellow,lime,pink,gray,lightGray,cyan,purple,blue,brown,green,red,black]
    #enter your data here:
    img = Image.open(ImageName)#image
    #place
    if img.width*img.height > 500*500:
        mc.postToChat("the Image is too big!")
    else:
        data = img.load()
        x = 0
        while x < img.width:
            y = 0
            while y < img.height and y >= 0:
                res = 255*3
                if verticalOrHorisontal=="vertical":
                    pixel = data[x,img.height-1-y]
                else:
                    pixel = data[x,y]
                for color in colors:
                    r = pixel[0]-color[0]
                    g = pixel[1]-color[1]
                    b = pixel[2]-color[2]
                    if math.fabs(r)+math.fabs(g)+math.fabs(b) < res:
                        res = math.fabs(r)+math.fabs(g)+math.fabs(b)
                        block = 35,color[3]
                if verticalOrHorisontal=="vertical":
                    mc.setBlock(X0+x,Y0+y,Z0,block)
                else:
                    mc.setBlock(X0+x,Y0,Z0+y,block)
                y = y + 1
            mc.postToChat(str(int(x / img.width * 100))+"%")
            x = x + 1
        mc.postToChat("done.")
Image(ImageName,X0,Y0,Z0,verticalOrHorisontal)
