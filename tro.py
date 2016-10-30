from mcpi.minecraft import Minecraft
from time import sleep
mc = Minecraft.create()
name = input('Yuor name: ')
password = input('Password')
if password == 'stupidpassword':
    ID = mc.getPlayerEntityId(name)
    pos = mc.entity.getTilePos(ID)
    x,y,z = pos.x,pos.y,pos.z
    def trololo(x,y,z):
        a=(35,15)
        c=(35,7)
        b=35
        f=0
        k=(35,13)
        bigArray = [
            [f,f,f,f,f,f,f,f,f,f,f,c,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
            [f,f,f,f,f,f,f,f,f,c,a,a,a,a,a,c,c,c,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,a,a],
            [f,f,f,f,f,f,f,c,a,a,c,b,b,b,b,b,b,b,c,c,c,c,b,b,b,b,b,b,c,c,c,b,b,b,b,b,a,a],
            [f,f,f,f,f,c,a,a,b,b,b,b,b,b,c,c,b,b,b,b,b,b,b,b,b,c,c,c,c,c,c,c,c,b,b,b,b,a,c],
            [f,f,f,f,f,c,a,b,b,b,b,c,c,b,b,b,c,b,b,b,b,b,c,c,b,b,b,b,b,b,c,c,c,c,b,b,b,c,a],
            [f,f,f,f,c,a,c,b,b,b,c,b,b,b,b,b,c,b,b,b,b,b,c,b,b,b,b,b,b,b,b,b,c,b,b,b,b,b,a,c],
            [f,f,f,f,c,a,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,c,a,a,a,a,c,b,b,b,b,b,b,b,b,c,a],
            [f,f,f,c,a,a,b,b,b,b,b,a,a,a,a,c,b,b,b,b,b,b,c,a,a,b,a,a,a,a,a,c,b,b,b,b,b,b,b,a,a],
            [f,f,c,a,a,b,c,b,c,b,a,a,a,a,a,a,a,b,c,b,b,b,a,b,b,c,a,a,a,a,a,a,c,c,c,b,b,b,b,c,a,a],
            [f,f,c,a,b,c,b,b,b,b,b,b,b,b,c,c,a,a,c,b,b,b,a,a,a,c,b,b,c,b,b,b,b,b,c,a,a,a,c,b,b,c,a],
            [f,c,a,c,b,b,c,a,a,c,b,b,b,b,b,b,c,c,b,b,b,b,b,c,b,b,b,b,a,a,b,b,c,a,a,c,b,b,a,a,b,b,c,a],
            [f,c,a,c,b,b,c,c,c,a,a,a,a,b,b,b,a,c,b,b,b,b,b,b,b,b,b,b,b,c,a,a,c,b,b,b,a,b,b,a,c,b,b,a],
            [f,c,a,c,b,b,b,b,c,b,c,c,b,b,b,a,a,b,b,b,b,b,c,a,c,b,b,b,b,b,b,b,b,b,a,a,a,c,b,b,a,b,b,a],
            [f,f,c,a,b,c,b,b,a,b,b,b,b,c,a,a,b,b,b,b,b,b,c,c,a,c,b,b,b,b,b,c,a,a,c,b,a,a,a,c,a,b,b,a],
            [f,f,c,a,c,b,b,a,a,b,b,b,c,c,a,a,b,b,b,b,a,a,a,b,a,b,b,b,c,a,a,a,c,b,b,b,a,b,b,a,b,b,b,a],
            [f,f,c,a,a,b,b,a,a,a,c,b,b,b,b,b,a,a,c,b,b,b,b,b,c,c,a,a,a,c,b,a,b,b,c,a,a,b,b,b,b,b,a],
            [f,f,f,c,a,b,b,a,a,c,a,a,a,c,b,b,b,a,b,b,b,c,a,a,a,a,c,b,b,b,b,a,a,a,a,a,b,b,b,b,b,a,a],
            [f,f,f,c,a,b,b,a,b,c,b,b,a,a,a,a,a,a,a,a,a,c,c,b,b,a,b,b,c,a,a,a,c,b,a,b,b,b,b,b,a,a],
            [f,f,f,c,a,c,b,a,a,a,b,b,c,b,b,b,a,b,b,b,c,b,b,b,b,a,a,a,a,a,c,a,b,a,a,b,b,b,b,a,a],
            [f,f,f,c,a,c,b,a,a,a,a,a,a,a,c,a,a,c,c,a,a,c,a,a,a,a,a,c,b,b,b,c,a,a,b,b,b,b,b,a],
            [f,f,f,c,a,c,b,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,c,b,a,b,b,b,b,a,a,b,b,b,b,b,a,a],
            [f,f,f,c,a,c,b,a,a,a,a,a,a,a,a,a,a,a,a,c,a,c,b,b,b,b,a,b,b,c,a,a,b,b,b,b,b,b,a],
            [f,f,f,c,a,b,b,c,a,a,b,a,b,a,b,b,a,b,b,b,c,c,b,b,b,b,c,a,a,a,b,b,b,b,b,b,c,a],
            [f,f,f,c,a,b,b,b,a,a,c,a,b,c,c,b,c,c,b,b,c,a,b,b,c,a,a,a,c,b,b,b,c,c,b,c,a],
            [f,f,f,c,a,b,b,b,b,b,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,c,b,b,b,c,c,c,c,c,a,a],
            [f,f,f,c,a,b,b,b,b,b,b,b,b,b,b,c,c,c,c,c,b,b,b,b,b,b,b,c,c,c,b,c,a,a],
            [f,f,f,c,a,b,c,b,b,c,c,b,b,b,b,b,b,b,b,b,b,b,b,c,c,c,c,b,b,c,a,a],
            [f,f,f,c,a,b,b,c,c,b,b,c,b,b,b,b,b,b,b,b,c,c,c,c,b,b,b,c,a,a],
            [f,f,f,c,a,b,b,b,c,c,c,c,b,b,b,b,b,b,b,b,b,b,b,b,b,c,a,a],
            [f,f,f,c,a,a,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,c,c,a,a,a],
            [f,f,f,f,c,a,a,b,b,b,b,b,b,b,b,b,b,c,a,a,a,a,a],
            [f,f,f,f,f,f,c,a,a,a,a,a,a,a,a,a,a,a],
            ]
        for level in bigArray:
            z=pos.z
            for block in level:
                mc.setBlock(x+3,y+3,z,block)
                z+=1
            y-=1
    trololo(x,y,z)

