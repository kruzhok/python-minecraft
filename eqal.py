from mcpi.minecraft import Minecraft
import time
import random
mc = Minecraft.create()
x,y,z = 57,68,40
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

musicPlayer(x,y,z)
