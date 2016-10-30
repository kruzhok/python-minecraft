from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time
name = input('Enter your name: ')
ID = mc.getPlayerEntityId(name)
pos = mc.entity.getTilePos(ID)
x,y,z = pos.x,pos.y,pos.z
u = 35,14#head-up
h = 35#head-down
b = 57#breast
p = 1#press
a = 41#arms
ll = 89#legs
s = 35#skin
o = 0#air
veryBigArray = [
    [
        [o,o,o,o,o,o,o,o],
        [o,o,o,o,o,o,o,o],
        [o,o,o,o,o,o,o,o],
        [o,o,o,o,o,o,o,o],
        [o,o,p,p,p,p,o,o],
        [o,o,p,p,p,p,o,o],
        [o,o,p,p,p,p,o,o],
        [o,o,o,o,o,o,o,o],
        [o,o,o,o,o,o,o,o],
        [o,o,o,o,o,o,o,o],
        [o,o,o,o,o,o,o,o],
        ],
        [
        [o,o,o,u,u,o,o,o],
        [o,o,o,h,h,o,o,o],
        [a,a,b,b,b,b,a,a],
        [a,a,b,b,b,b,a,a],
        [a,a,p,p,p,p,a,a],
        [s,s,p,p,p,p,s,s],
        [o,o,p,p,p,p,o,o],
        [o,ll,ll,o,o,ll,ll,o],
        [o,ll,ll,o,o,ll,ll,o],
        [o,ll,ll,o,o,ll,ll,o],
        [o,ll,ll,o,o,ll,ll,o]
        ],
        [
        [o,o,o,u,u,o,o,o],
        [o,o,o,h,h,o,o,o],
        [a,a,b,b,b,b,a,a],
        [a,a,b,b,b,b,a,a],
        [a,a,p,p,p,p,a,a],
        [s,s,p,p,p,p,s,s],
        [o,o,p,p,p,p,o,o],
        [o,ll,ll,o,o,ll,ll,o],
        [o,ll,ll,o,o,ll,ll,o],
        [o,ll,ll,o,o,ll,ll,o],
        [o,ll,ll,o,o,ll,ll,o]
        ],
        [
        [o,o,o,o,o,o,o,o],
        [o,o,o,o,o,o,o,o],
        [o,o,b,b,b,b,o,o],
        [o,o,b,b,b,b,o,o],
        [o,o,p,p,p,p,o,o],
        [o,o,p,p,p,p,o,o],
        [o,o,p,p,p,p,o,o],
        [o,o,o,o,o,o,o,o],
        [o,o,o,o,o,o,o,o],
        [o,o,o,o,o,o,o,o],
        [o,o,o,o,o,o,o,o]
        ]
        ]
for letter in veryBigArray:
    y = pos.y
    for level in letter:
        x = pos.x
        for block in level:
            mc.setBlock(x,y,z,block)
            x+=1
        y-=1
    z-=1
