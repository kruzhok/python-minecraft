# minecraft cool objects library for Minecraft
# made during Alexander Patlukh's course in Moscow Coding School

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
import random

# butterfly

def butterfly(x,y,z):
    
    #body
    mc.setBlocks(x+5,y+5,z,x+8,y+5,z+1,35,14)
    mc.setBlocks(x+9,y+5,z-1,x+10,y+5,z-1,35,14)
    mc.setBlocks(x+9,y+5,z+2,x+10,y+5,z+2,35,14)
    mc.setBlock(x+11,y+5,z-2,35,14)
    mc.setBlock(x+11,y+5,z+3,35,14)
    mc.setBlocks(x+12,y+5,z-3,x+12,y+5,z-4,35,14)
    mc.setBlocks(x+12,y+5,z+4,x+12,y+5,z+5,35,14)
    mc.setBlock(x+13,y+5,z-4,35,14)
    mc.setBlock(x+13,y+5,z+5,35,14)
    #wings
    mc.setBlock(x+2,y+5,z-4,35,3)
    mc.setBlock(x+2,y+5,z+5,35,3)
    mc.setBlocks(x+3,y+5,z-1,x+4,y+5,z-3, 35,3)
    mc.setBlock(x+3,y+5,z-1,0)
    mc.setBlocks(x+3,y+5,z+2,x+4,y+5,z+4, 35,3)
    mc.setBlock(x+3,y+5,z+2,0)
    mc.setBlocks(x+5,y+5,z-2,x+8,y+5,z-2, 35,3)
    mc.setBlocks(x+5,y+5,z+3,x+8,y+5,z+3, 35,3)
    mc.setBlocks(x+6,y+5,z-3,x+9,y+5,z-3, 35,3)
    mc.setBlock(x+7,y+5,z-3,0)
    mc.setBlocks(x+6,y+5,z+4,x+9,y+5,z+4, 35,3)
    mc.setBlock(x+7,y+5,z+4,0)
    mc.setBlocks(x+7,y+5,z-4,x+10,y+5,z-4, 35,3)
    mc.setBlock(x+8,y+5,z-4,0)
    mc.setBlocks(x+7,y+5,z+5,x+10,y+5,z+5, 35,3)
    mc.setBlock(x+8,y+5,z+5,0)
    mc.setBlocks(x+8,y+5,z-5,x+11,y+5,z-5, 35,3)
    mc.setBlock(x+9,y+5,z-5,0)
    mc.setBlocks(x+8,y+5,z+6,x+11,y+5,z+6, 35,3)
    mc.setBlock(x+9,y+5,z+6,0)
    mc.setBlocks(x+9,y+5,z-6,x+12,y+5,z-6, 35,3)
    mc.setBlocks(x+9,y+5,z+7,x+12,y+5,z+7, 35,3)
    mc.setBlock(x+12,y+5,z-7,35,3)
    mc.setBlock(x+12,y+5,z+8,35,3)
    
#house with 2 stained-glass window
def stainGlassHouse(x,y,z):
    #коробка из кирпича
    mc.setBlocks(x-5,y,z-5,x+5,y+12,z+5,45)
    #коробка из воздуха
    mc.setBlocks(x-4,y,z-4,x+4,y+11,z+4,0)
    #сделать пол
    mc.setBlocks(x-5,y-1,z-5,x+5,y-1,z+5,1)
    #сделать дверь 1 в ширину 2 в высоту с калиткой из акации id 187
    mc.setBlocks(x,y,z+5,x,y+2,z+5,0)
    mc.setBlock(x,y+1,z+5,187)
    #сделаем витраж
    mc.setBlocks(x-3,y+4,z+5,x+3,y+10,z+5,95,5)
    mc.setBlocks(x+3,y+4,z-5,x-3,y+10,z-5,95,5)
    
#house with 7 windows, door, roof
def fourWindowsHouse(x,y,z):
    #пол
    mc.setBlocks(x+5,y-1,z+5,x-5,y-1,z-5,17)
    #стены
    mc.setBlocks(x+5,y,z+5,x-5,y+10,z-5,45)
    mc.setBlocks(x+4,y,z+4,x-4,y+9,z-4,0)
    #окна
    mc.setBlocks(x-1,y+1,z+5,x-4,y+4,z+5,95,2)
    mc.setBlocks(x+1,y+6,z+5,x+4,y+9,z+5,95,2)
    mc.setBlocks(x-1,y+6,z+5,x-4,y+9,z+5,95,2)
    mc.setBlocks(x-1,y+1,z-5,x-4,y+4,z-5,95,2)
    mc.setBlocks(x+1,y+6,z-5,x+4,y+9,z-5,95,2)
    mc.setBlocks(x-1,y+6,z-5,x-4,y+9,z-5,95,2)
    mc.setBlocks(x+1,y+1,z-5,x+4,y+4,z-5,95,2)
    #дверь
    mc.setBlocks(x+1,y,z+5,x+1,y+1,z+5,0)
    mc.setBlock(x+1,y,z+5,187)
    #крыша
    mc.setBlocks(x-6,y+11,z-6,x+6,y+11,z+6,41)

#house with traingle roof from lighter blocks
def traingleRoofHouse(x,y,z):
    #grass

    mc.setBlocks(x-10, y-1,z-10,x+10, y-1, z+10, 2)

    #road
    mc.setBlocks(x-10,y-1,z+11,x+10,y-1,z+14,1)

    #house

    mc.setBlocks(x-5,y,z-5,x+5,y+10,z+5,168)
    mc.setBlocks(x-4,y,z-4,x+4,y+9,z+4,0)

    #windows

    mc.setBlocks(x-5,y+2,z-1,x-5,y+3,z-2,20)
    mc.setBlocks(x-5,y+2,z+1,x-5,y+3,z+2,20)
    mc.setBlocks(x-5,y+5,z-1,x-5,y+6,z-2,20)
    mc.setBlocks(x-5,y+5,z+1,x-5,y+6,z+2,20)

    mc.setBlocks(x+5,y+2,z-1,x+5,y+3,z-2,20)
    mc.setBlocks(x+5,y+2,z+1,x+5,y+3,z+2,20)
    mc.setBlocks(x+5,y+5,z-1,x+5,y+6,z-2,20)
    mc.setBlocks(x+5,y+5,z+1,x+5,y+6,z+2,20)

    mc.setBlocks(x+1,y+5,z+5,x-1,y+7,z+5,20)

    #door
    mc.setBlocks(x+1,y,z+5,x-1,y+2,z+5,0)
    mc.setBlocks(x+1,y+1,z+5,x-1,y+1,z+5,184)

    #roof
    a=2
    while a>=-5:
        mc.setBlocks(x-5-a,y+10,z-5-a,x+5+a,y+10,z+5+a,89)
        a-=1
        y+=1

# Car which moves permanently and Stieve inside

def car(x,y,z):
    while True:
        mc.setBlocks(x+2,y-1,z-20,x+9,y-1,z+20,35,15)
         #красная шерсть — корпус машины 35.14
         #x — расстоние до тачки и её ширина
         #y — высота
         #z — длина
        mc.setBlocks(x+5,y+1,z,x+7,y+2,z+7,35,14)
         #стекло
        mc.setBlocks(x+5,y+3,z+2,x+7,y+4,z+5,20)

         #колеса — из черной шерсти 35,15
        mc.setBlocks(x+4,y,z+1,x+5,y+1,z+2,35,15)
        mc.setBlocks(x+4,y,z+5,x+5,y+1,z+6,35,15)
        mc.setBlocks(x+7,y,z+1,x+8,y+1,z+2,35,15)
        mc.setBlocks(x+7,y,z+5,x+8,y+1,z+6,35,15)
        #Стив внутри
        mc.player.setTilePos(x+6,y+3,z+4)
        z = z - 1
        time.sleep(0.5)
        mc.setBlocks(x,y,z,x+10,y+10,z+10,0)

# house with road, grass and tree

def houseWithRoad(x,y,z):
        #газон
    mc.setBlocks(x-10,y-1,z-10,x+10,y-1,z+10,2)
    #построим коробку
    mc.setBlocks(x-5,y-1,z-5,x+4,y+9,z+4,5)
    mc.setBlocks(x-4,y,z-4,x+3,y+8,z+3,0)
    #построим окна и вход
    mc.setBlocks(x-4,y+6,z+4,x-2,y+7,z+4,20)
    mc.setBlocks(x-4,y+3,z+4,x-2,y+4,z+4,20)
    mc.setBlocks(x+1,y+6,z+4,x+3,y+7,z+4,20)
    mc.setBlocks(x+1,y,z+4,x+2,y+2,z+4,0)
    #тротуар и дорога
    mc.setBlocks(x-10,y,z+6,x+10,y,z+9,44)
    mc.setBlocks(x-10,y-1,z+10,x+10,y-1,z+16,35,15)
    mc.setBlocks(x-10,y,z+17,x+10,y,z+19,44)
    #дерево
    mc.setBlocks(x+6,y+2,z-1,x+8,y+5,z+1,18)
    mc.setBlocks(x+7,y-1,z,x+7,y+4,z,5,1)

def musicPlayer(x,y,z):
    while True:
        time.sleep(0.2)
        mc.setBlocks(x+5,y,z-3,x+5,y+5,z+3,0)
        mc.setBlocks(x+5,y,z-3,x+5,y+random.randint(0,5),z-3,35,1)
        mc.setBlocks(x+5,y,z-2,x+5,y+random.randint(0,5),z-2,35,2)
        mc.setBlocks(x+5,y,z-1,x+5,y+random.randint(0,5),z-1,35,3)
        mc.setBlocks(x+5,y,z,x+5,y+random.randint(0,5),z,35,4)
        mc.setBlocks(x+5,y,z+1,x+5,y+random.randint(0,5),z+1,35,5)
        mc.setBlocks(x+5,y,z+2,x+5,y+random.randint(0,5),z+2,35,6)
        mc.setBlocks(x+5,y,z+3,x+5,x+random.randint(0,5),z+3,35,7)

def Image(ImageName,X0,Y0,Z0):
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
            while y < img.height:
                res = 255*3
                pixel = data[x,y]
                for color in colors:
                    r = pixel[0]-color[0]
                    g = pixel[1]-color[1]
                    b = pixel[2]-color[2]
                    if math.fabs(r)+math.fabs(g)+math.fabs(b) < res:
                        res = math.fabs(r)+math.fabs(g)+math.fabs(b)
                        block = 35,color[3]
                mc.setBlock(X0+x,Y0,Z0+y,block)
                y = y + 1
            mc.postToChat(str(int(x / img.width * 100))+"%")
            x = x + 1
        mc.postToChat("done.")
