from mcpi.minecraft import Minecraft
mc = Minecraft.create()
name = '_vPro_Play_'
ID=mc.getPlayerEntityId(name)
pos = mc.entity.getTilePos(ID)
x,y,z = pos.x,pos.y,pos.z

def setPyramid(x,y,z):
    #расчищу пространство
    mc.setBlocks(x-14,y,z-14,x+14,y+14,z+14,0)
    #Строим пирамиду
    mc.setBlocks(x-14,y-1,z-14,x+14,y-1,z+14,(201))
    mc.setBlocks(x-13,y,z-13,x+13,y,z+13,(179,1))
    mc.setBlocks(x-12,y+1,z-12,x+12,y+1,z+12,(179,1))
    mc.setBlocks(x-11,y+2,z-11,x+11,y+2,z+11,(179,1))
    mc.setBlocks(x-10,y+3,z-10,x+10,y+3,z+10,(179,1))
    mc.setBlocks(x-9,y+4,z-9,x+9,y+4,z+9,(179,1))
    mc.setBlocks(x-8,y+5,z-8,x+8,y+5,z+8,(179,1))
    mc.setBlocks(x-7,y+6,z-7,x+7,y+6,z+7,(179,1))
    mc.setBlocks(x-6,y+7,z-6,x+6,y+7,z+6,(179,1))
    mc.setBlocks(x-5,y+8,z-5,x+5,y+8,z+5,(179,1))
    mc.setBlocks(x-4,y+9,z-4,x+4,y+9,z+4,(179,1))
    mc.setBlocks(x-3,y+10,z-3,x+3,y+10,z+3,(179,1))
    mc.setBlocks(x-2,y+11,z-2,x+2,y+11,z+2,(179,1))
    mc.setBlocks(x-1,y+12,z-1,x+1,y+12,z+1,(179,1))
    mc.setBlock(x,y+13,z,169)

    #строить комнаты
    mc.setBlocks(x-6,y,z-6,x+6,y+5,z+6,0)
    mc.setBlocks(x-6,y-4,z-6,x+12,y-2,z+6,0)
    mc.setBlock(x-4,y-1,z,96)
    #строим ступеньки
    mc.setBlock(x+14,y,z,155,5)
    mc.setBlock(x+13,y+1,z,155,5)

    mc.setBlocks(x+5,y,z,x+6,y,z,155,5)


    mc.setBlock(x+6,y+1,z,155,5)
    #строим ворота
    mc.setBlocks(x+10,y+2,z-1,x+12,y+4,z+1,41)
    mc.setBlocks(x+7,y+2,z,x+12,y+3,z,0)

setPyramid(x,y,z)
