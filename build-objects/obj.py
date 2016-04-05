# minecraft cool objects library for Minecraft
# made during Alexander Patlukh's course in Moscow Coding School

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

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
