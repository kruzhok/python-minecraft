from mcpi.minecraft import Minecraft
from mcpi.minecraftstuff import MinecraftDrawing
mc = Minecraft.create()
md = MinecraftDrawing(mc)
while True:
    name = input('Your nickname is:  ')
    try:
        id= mc.getPlayerEntityId(name)
    except:
        print('Wrong nickname, bro')
    else:
        break
while True:
    password = input('Enter password: ')
    if password == 'stupidpassword':
        pos = mc.entity.getTilePos(id)
        x,y,z = pos.x,pos.y,pos.z

        def setFarmSpace(id,x,y,z):
            mc.setBlocks(x-50,y-1,z-50,x+50,y+20,z+50,0)
            mc.setBlocks(x-50,y-1,z-50,x+50,y-1,z+50,2)

            mc.setBlocks(x-50,y,z-50,x+50,y,z+50,139)
            mc.setBlocks(x-49,y,z-49,x+49,y,z+49,0)
            mc.setBlocks(x-50,y,z-29,x-50,y,z-26,0)

        setFarmSpace(id,x,y,z)

        def plants(id,x,y,z):
               mc.setBlocks(x-49,y-1,z-25,x-30,y-1,z-15,60)
               mc.setBlocks(x-49,y,z-25,x-30,y,z-15,38,8)
               #изгородь
               mc.setBlocks(x+49,y,z-49,x+49,y,z+49,31,1)
               mc.setBlocks(x-49,y,z-49,x+49,y,z-49,6,2)
               mc.setBlocks(x-49,y,z+49,x+49,y,z+49,6,3)

        plants(id,x,y,z)

        def traingleRoofHouse(id,x,y,z):
            #grass

            mc.setBlocks(x-10, y-1,z-10,x+10, y-1, z+10, 2)
            mc.setBlocks(x-9, y,z-9,x+10, y, z+10, 38,4)

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

            mc.setBlock(x,y,z-3,355)

            #door
            mc.setBlocks(x+1,y,z+5,x-1,y+2,z+5,0)
            mc.setBlocks(x+1,y+1,z+5,x-1,y+1,z+5,184)
            #smallroad
            mc.setBlocks(x+1,y-1,z+5,x-1,y-1,z+10,1)

            #roof
            a=2
            while a>=-5:
                mc.setBlocks(x-5-a,y+10,z-5-a,x+5+a,y+10,z+5+a,89)
                a-=1
                y+=1
        traingleRoofHouse(id,x-40,y,z-40)

        def roads(id,x,y,z):
            #road
            mc.setBlocks(x-50,y-1,z-29,x+50,y-1,z-26,1)
            mc.setBlocks(x-29,y-1,z-49,x-27,y-1,z+49,1)
            mc.setBlocks(x-49,y-1,z-16,x-30,y-1,z-13,1)
            mc.setBlocks(x-49,y-1,z+1,x-30,y-1,z+4,1)
            mc.setBlocks(x-49,y-1,z+38,x-30,y-1,z+35,1)

        roads(id,x,y,z)

        def zagons(id,x,y,z):
            #загон 1
            mc.setBlocks(x-49,y,z-12,x-30,y,z,85)
            mc.setBlocks(x-49,y,z-11,x-31,y,z-1,0)
            mc.setBlock(x-30,y,z-5,187,1)

            #загон 2
            mc.setBlocks(x-49,y,z+34,x-30,y,z+5,85)
            mc.setBlocks(x-49,y,z+33,x-31,y,z+6,0)
            mc.setBlock(x-30,y,z+10,187,1)
        zagons(id,x,y,z)

        def pool(id,x,y,z):
            mc.setBlocks(x-26,y,z-49,x-15,y,z-30,139,1)
            mc.setBlocks(x-25,y,z-49,x-16,y,z-31,0)
            #mc.setBlocks(x-21,y,z-30,x-19,y,z-30,0)
            mc.setBlocks(x-25,y-1,z-49,x-16,y-1,z-31,8)
        pool(id,x,y,z)

        def mangal(id,x,y,z):
            mc.setBlocks(x-26,y-1,z-25,x-15,y-1,z-17,155,1)
            mc.setBlocks(x-22,y,z-17,x-19,y+2,z-18,1,2)
            mc.setBlocks(x-21,y+1,z-18,x-20,y+1,z-18,0)
            mc.setBlocks(x-21,y+1,z-18,x-20,y+1,z-18,51)
        mangal(id,x,y,z)

        def parnik(id,x,y,z):
            mc.setBlocks(x-49,y,z+49,x-30,y+6,z+39,20)
            mc.setBlocks(x-48,y,z+48,x-31,y+5,z+40,0)
            mc.setBlocks(x-39,y,z+43,x-30,y+2,z+45,0)
            mc.setBlocks(x-48,y-1,z+48,x-31,y-1,z+40,60)
            mc.setBlocks(x-48,y,z+48,x-31,y,z+40,103)
            mc.setBlocks(x-30,y,z+43,x-48,y,z+45,0)
            mc.setBlocks(x-30,y-1,z+43,x-48,y-1,z+45,44,5)
        parnik(id,x,y,z)

        def setBigHouse(id,x,y,z):
            mc.setBlocks(x-8,y,z-8,x+8,y+6,z+8,179)
            mc.setBlocks(x-7,y,z-7,x+7,y+5,z+7,0)

            mc.setBlocks(x-8,y+2,z-7,x-8,y+4,z-5,20)
            mc.setBlocks(x-8,y+2,z-3,x-8,y+4,z+2,20)
            mc.setBlocks(x-8,y+2,z+7,x-8,y+4,z+5,20)
            mc.setBlocks(x+8,y+2,z-7,x+8,y+4,z+7,95,2)
            a=0
            while a<=10:
                md.drawHorizontalCircle(x,y+a,z+16,8,179)
                md.drawHorizontalCircle(x,y+a,z-16,8,179)
                a+=1
            mc.setBlocks(x,y,z-8,x,y+3,z-8,0)
            mc.setBlocks(x,y,z+8,x,y+3,z+8,0)

            mc.setBlocks(x-8,y+4,z+15,x-8,y+8,z+17,20)
            mc.setBlocks(x-8,y+4,z-15,x-8,y+8,z-17,20)

            mc.setBlocks(x+8,y+4,z+15,x+8,y+8,z+17,20)
            mc.setBlocks(x+8,y+4,z-15,x+8,y+8,z-17,20)

            mc.setBlocks(x-8,y-1,z-24,x+8,y-1,z+24,155,1)
            a=0
            while a<=8:
                mc.setBlocks(x-9+a,y+11+a,z-7-a,x+8-a,y+11+a,z-25+a,133)
                mc.setBlocks(x-9+a,y+11+a,z+7+a,x+8-a,y+11+a,z+25-a,133)
                a+=1

            mc.setBlocks(x-8,y,z+16,x-8,y+2,z+16,0)
            mc.setBlocks(x-8,y,z-16,x-8,y+2,z-16,0)
            mc.setBlock(x-8,y+1,z-16,186,1)
            mc.setBlock(x-8,y+1,z+16,186,1)
        setBigHouse(id,x+41,y,z+25)
        break
    else:
        print('Wrong password')
