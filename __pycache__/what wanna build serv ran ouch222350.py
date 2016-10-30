from mcpi.minecraft import Minecraft
mc=Minecraft.create()
from random import randint
name=input('your nick:')
try:
    ID=mc.getPlayerEntityId(name)
except:
    print('no such player on server')
else:
    pos=mc.entity.getTilePos(name)
    x,y,z=pos.x,pos.y,pos.z
  def setShuttle():
    #Making torse 1
    mc.setBlocks(x+3,y,z+1,x+12,y+5,z+7,42)
    mc.setBlocks(x+4,y+1,z+2,x+11,y+4,z+6,0)
    #2
    mc.setBlocks(x+13,y,z+1,x+22,y+5,z+7,42)
    mc.setBlocks(x+14,y+1,z+2,x+21,y+4,z+6,0)
    #3
    mc.setBlocks(x+2,y+1,z+2,x+1,y+4,z+6,42)
    mc.setBlocks(x,y+2,z+3,x-1,y+3,z+5,42)
    mc.setBlocks(x-2,y+3,z+4,x-2,y+2,z+4,42)
    #making wings 1
    mc.setBlocks(x+22,y+5,z+14,x+22,y+5,z+8,42)
    mc.setBlocks(x+22,y+5,z-6,x+22,y+5,z,42)
    #2
    mc.setBlocks(x+21,y+5,z+13,x+21,y+5,z+8,42)
    mc.setBlocks(x+20,y+5,z+13,x+20,y+5,z+8,42)
    mc.setBlocks(x+21,y+5,z-5,x+21,y+5,z,42)
    mc.setBlocks(x+20,y+5,z-5,x+20,y+5,z,42)
    #3
    mc.setBlock(x+19,y+5,z+12,x+19,y+5,z+8,42)
    mc.setBlock(x+19,y+5,z-4,x+19,y+5,z,42)
    #making lilghts
    mc.setBlocks(x+6,y+5,z+2,x+9,y+5,z+5,169)
    #making door place
    mc.setBlocks(x+12,y+1,z+4,x+13,y+2,z+4,0)
  down=randint(1,60)
  middle=randint(1,60)
  top=randint(1,60)
  def setFlag(down,middle,top):
    mc.setBlocks(x+2,y+3,z+1,x+2,y+3,z+5,down)
    mc.setBlocks(x+2,y+4,z+1,x+2,y+4,z+5,middle)
    mc.setBlocks(x+2,y+5,z+1,x+2,y+5,z+5,top)
  ans=input('what to build (flag or shuttle):')
  if ans=='flag' or ans=='Flag':
    setFlag(down,middle,top)
  elif ans=='Shuttle' or ans=='shuttle':
    setShuttle()
