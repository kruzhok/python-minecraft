from mcpi.minecraft import Minecraft
mc = Minecraft.create()
name = input('Enter your nickname, bro: ')
ID = mc.getPlayerEntityId(name)
pos = mc.entity.getTilePos(ID)
x,y,z = pos.x,pos.y,pos.z
def Shuttle(x,y,z):
    #cтрою корпус
    mc.setBlocks(x+2,y,z-2,x+14,y+4,z+2,159,14)
    #строю кабину
    mc.setBlocks(x+10,y+1,z-2,x+14,y+4,z+2,20)
    #строю пустоту
    mc.setBlocks(x+3,y+1,z-1,x+13,y+3,z+1,0)
    #строю люк
    mc.setBlock(x+8,y+4,z,96)
    #строю нос
    mc.setBlocks(x+15,y+1,z-1,x+15,y+3,z+1,20)
    mc.setBlock(x+16,y+2,z,20)
    #строю левое крыло
    mc.setBlocks(x+3,y+1,z-3,x+8,y+1,z-3,49)
    mc.setBlocks(x+3,y+1,z-4,x+7,y+1,z-4,49)
    mc.setBlocks(x+3,y+1,z-5,x+6,y+1,z-5,49)
    mc.setBlocks(x+3,y+1,z-6,x+5,y+1,z-6,49)
    mc.setBlocks(x+3,y+1,z-7,x+4,y+1,z-7,49)
    mc.setBlock(x+3,y+1,z-8,49)
    #строю правое крыло
    mc.setBlocks(x+3,y+1,z+3,x+8,y+1,z+3,49)
    mc.setBlocks(x+3,y+1,z+4,x+7,y+1,z+4,49)
    mc.setBlocks(x+3,y+1,z+5,x+6,y+1,z+5,49)
    mc.setBlocks(x+3,y+1,z+6,x+5,y+1,z+6,49)
    mc.setBlocks(x+3,y+1,z+7,x+4,y+1,z+7,49)
    mc.setBlock(x+3,y+1,z+8,49)
    #строю хвост
    mc.setBlocks(x+3,y+5,z,x+6,y+5,z,41)
    mc.setBlocks(x+3,y+6,z,x+5,y+6,z,41)
    mc.setBlocks(x+3,y+7,z,x+4,y+7,z,41)
    mc.setBlock(x+3,y+8,z,41)
    #лава
    mc.setBlock(x+1,y,z-2,11)
    mc.setBlock(x+1,y,z+2,11)
Shuttle(x,y,z)
