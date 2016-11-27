from mcpi.minecraft import Minecraft
from time import sleep
mc = Minecraft.create()
x,y,z = 48, 109,28

def setCactus(x,y,z):
    mc.setBlocks(x,y,z,x+12,y+4,z,(35,12))
    mc.setBlocks(x+2,y+1,z,x+10,y+3,z,(35,14))
    mc.setBlocks(x,y-1,z,x,y+1,z,(0))
    mc.setBlocks(x+12,y-1,z,x+12,y+1,z,(0))
    mc.setBlocks(x+1,y+3,z,x+11,y+3,z,(35,14))
    mc.setBlocks(x+3,y+5,z,x+9,y+15,z,(35,13))
    mc.setBlocks(x+4,y+5,z,x+8,y+14,z,(35,5))
    mc.setBlocks(x+2,y+15,z,x+4,y+15,z,(0))
    mc.setBlocks(x+8,y+15,z,x+10,y+15,z,(0))
    mc.setBlock(x+3,y+14,z,0)
    mc.setBlock(x+9,y+14,z,0)
    mc.setBlock(x+4,y+14,z,(35,13))
    mc.setBlock(x+8,y+14,z,(35,13))
    mc.setBlocks(x+9,y+7,z,x+12,y+11,z,(35,13))
    mc.setBlocks(x+9,y+8,z,x+11,y+10,z,(35,5))
    mc.setBlock(x+12,y+11,z,0)
    mc.setBlock(x+12,y+7,z,0)
    mc.setBlock(x+5,y+12,z,(35,15))
    mc.setBlock(x+7,y+10,z,(35,15))
    mc.setBlock(x+5,y+8,z,(35,15))
    mc.setBlock(x+7,y+6,z,(35,15))
def setFlower(x,y,z):
    mc.setBlock(x+6,y+17,z,(35,2))
    mc.setBlock(x+6,y+16,z,(35,4))
    mc.setBlock(x+6,y+15,z,(35,2))
    mc.setBlock(x+5,y+16,z,(35,2))
    mc.setBlock(x+7,y+16,z,(35,2))
def removeFlower(x,y,z):
    mc.setBlock(x+6,y+17,z,0)
    mc.setBlock(x+6,y+16,z,0)
    mc.setBlock(x+6,y+15,z,0)
    mc.setBlock(x+5,y+16,z,0)
    mc.setBlock(x+7,y+16,z,0)

while True:
      setCactus(x,y,z)
      sleep(101)
      setFlower(x,y,z)
      sleep(101)
      removeFlower(x,y,z)
