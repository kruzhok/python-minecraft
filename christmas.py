from mcpi.minecraft import Minecraft
from mcpi.minecraftstuff import MinecraftDrawing
mc=Minecraft.create()
md=MinecraftDrawing(mc)

x,y,z = 289,114,-108
def yolka(x,y,z):
    def traingle(x,y,z,r):
        for a in range(0,r+1):
            md.drawHorizontalCircle(x,y+a,z,r-a,35,5)

    r=20
    for i in range(0,5):
        traingle(x,y+10,z,r)
        y+=8
        r-=4
    y=114
    mc.setBlocks(x-1,y,z-1,x+1,y+43,z+1,5,1)
yolka(x,y,z)

#украшения
#mc.setBlocks(x-1,y+47,z-1,x+1,y+49,z+1,169)



