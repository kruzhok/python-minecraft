from mcpi.minecraft import Minecraft
from time import sleep
mc = Minecraft.create()

x,y,z = -142,103,133

b=(35,15)
c=35
d=35
e=(35,17)
f=(35,14)
g=(35,12)
j=(35,8)
bigList = [
                   [b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b],
                   [b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b],
                   [b,b,b,b,b,b,b,b,e,b,e,b,b,b,b,b,b,b,b,b,b],
                   [b,b,b,b,b,b,e,e,e,e,e,e,e,b,b,b,b,b,b,b,b],
                   [b,b,b,b,b,b,e,e,e,e,e,e,e,e,e,b,b,b,b,b,b],
                   [b,b,b,b,b,e,e,e,c,c,c,c,e,e,e,b,b,b,b,b,b],
                   [b,b,b,b,e,e,e,c,b,b,b,b,c,b,e,e,b,b,b,b,b],
                   [b,b,b,b,e,e,c,b,b,b,b,b,b,c,e,e,b,b,b,b,b],
                   [b,b,b,e,e,c,b,b,b,b,b,b,b,b,c,d,b,b,b,b,b],
                   [b,b,b,b,e,c,b,b,b,b,b,b,b,b,d,b,d,b,b,b,b],
                   [b,b,b,b,b,c,b,g,j,b,b,b,g,j,b,b,d,b,b,b,b],
                   [b,b,b,b,b,c,b,j,j,b,b,b,j,j,b,d,b,b,b,b,b],
                   [b,b,b,b,b,c,b,b,b,b,b,b,b,b,d,b,b,b,b,b,b],
                   [b,b,b,b,b,c,b,f,f,f,b,b,b,b,c,b,b,b,b,b,b],
                   [b,b,b,b,b,c,b,f,f,f,b,b,b,b,c,b,b,b,b,b,b],
                   [b,b,b,b,b,b,c,f,f,f,b,b,b,b,c,b,b,b,b,b,b],
                   [b,b,b,b,b,b,b,c,f,b,b,b,b,c,b,b,b,b,b,b,b],
                   [b,b,b,b,b,b,b,b,c,b,b,b,c,b,b,b,b,b,b,b,b],
                   [b,b,b,b,b,b,b,b,b,c,b,c,b,b,b,b,b,b,b,b,b],
                   [b,b,b,b,b,b,b,b,b,b,c,b,b,b,b,b,b,b,b,b,b],
                   [b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b],
       ]
for line in bigList:
      for block in line:
            mc.setBlock(x-10,y+21,z+3,block)
            x+=1
      x=-142
      y-=1
      sleep(1)
