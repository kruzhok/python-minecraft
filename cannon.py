from mcpi.minecraft import Minecraft
import obj as o
mc = Minecraft.create()
name = input('Yuor name: ')
ID = mc.getPlayerEntityId(name)
pos = mc.entity.getTilePos(ID)
x,y,z = pos.x,pos.y,pos.z

b=(5,5)
c=42
a=0
bigarray=[
    [
        [a,a,a,a,a,a,a,a,a,a,a,a,a,a],
        [a,a,a,a,a,a,a,a,a,a,a,a,a,a],
        [a,a,a,a,a,a,a,a,a,a,a,a,a,a],
        [a,a,a,a,a,a,a,a,a,a,a,a,a,a],
        [a,a,a,a,a,a,a,b,b,b,a,a,a,a],
        [a,a,a,a,a,a,a,b,a,b,a,a,a,a],
        [a,a,a,a,a,a,b,b,a,b,b,a,a,a],
        [a,a,a,a,a,a,b,a,a,a,b,a,a,a],
        [a,a,a,a,a,b,b,a,a,a,b,b,a,a],
        [a,a,a,a,b,b,b,b,b,b,b,b,b,a]


        ],
    [
        [a,a,a,a,a,a,a,a,a,a,a,a,a,a],
        [a,a,a,a,a,a,a,a,a,a,a,a,a,a],
        [a,a,a,a,a,a,a,a,a,a,a,a,a,a],
        [a,a,a,a,a,a,a,a,a,a,a,a,a,a],
        [a,a,a,a,a,a,a,b,b,b,a,a,a,a],
        [a,a,a,a,a,a,a,b,a,b,a,a,a,a],
        [a,a,a,a,a,a,b,b,a,b,b,a,a,a],
        [a,a,a,a,a,a,b,a,a,a,b,a,a,a],
        [a,a,a,a,a,b,b,a,a,a,b,b,a,a],
        [a,a,a,a,b,b,b,b,b,b,b,b,b,a]


        ],
    [
        [a,a,a,a,a,a,a,c,c,c,a,a,a,a],
        [a,a,a,a,a,a,a,c,c,c,a,a,a,a],
        [a,a,a,a,a,a,a,c,c,c,a,a,a,a],
        [a,a,a,a,a,a,a,c,c,c,a,a,a,a],
        [a,a,a,a,a,a,a,c,c,c,a,a,a,a],
        [a,a,a,a,a,a,a,c,c,c,a,a,a,a],
        [a,a,a,a,a,a,a,c,c,c,a,a,a,a],
        [a,a,a,a,a,a,a,c,c,c,a,a,a,a],
        [a,a,a,a,a,a,a,a,a,a,a,a,a,a],
        [a,a,a,a,a,a,a,a,a,a,a,a,a,a]


        ],
    [
        [a,a,a,a,a,a,a,c,c,c,a,a,a,a],
        [c,a,a,c,c,c,c,a,a,a,c,c,a,a],
        [c,a,a,c,c,c,c,a,a,a,c,c,a,a],
        [c,a,a,c,c,c,c,a,a,a,c,c,a,a],
        [c,a,a,c,c,c,c,a,a,a,c,c,a,a],
        [c,a,a,c,c,c,c,a,a,a,c,c,a,a],
        [c,a,a,c,c,c,c,a,a,a,c,c,a,a],
        [a,a,a,a,a,a,a,c,c,c,a,a,a,a],
        [a,a,a,a,a,a,a,a,a,a,a,a,a,a],
        [a,a,a,a,a,a,a,a,a,a,a,a,a,a]


        ],
    [
        [a,a,a,a,a,a,a,c,c,c,a,a,a,a],
        [c,a,a,c,c,c,c,a,a,a,c,c,a,a],
        [a,c,c,a,a,a,a,a,a,a,a,a,c,a],
        [a,c,c,a,a,a,a,a,a,a,a,a,c,a],
        [a,c,c,a,a,a,a,a,a,a,a,a,c,a],
        [a,c,c,a,a,a,a,a,a,a,a,a,c,a],
        [c,a,a,c,c,c,c,a,a,a,c,c,a,a],
        [a,a,a,a,a,a,a,c,c,c,a,a,a,a],
        [a,a,a,a,a,a,a,a,a,a,a,a,a,a],
        [a,a,a,a,a,a,a,a,a,a,a,a,a,a]


        ],
    [
        [a,a,a,a,a,a,a,c,c,c,a,a,a,a],
        [c,a,a,c,c,c,c,a,a,a,c,c,a,a],
        [a,c,c,a,a,a,a,a,a,a,a,a,c,a],
        [a,a,a,a,a,a,a,a,a,a,a,a,a,c],
        [a,a,a,a,a,a,a,a,a,a,a,a,a,c],
        [a,c,c,a,a,a,a,a,a,a,a,a,c,a],
        [c,a,a,c,c,c,c,a,a,a,c,c,a,a],
        [a,a,a,a,a,a,a,c,c,c,a,a,a,a],
        [a,a,a,a,a,a,a,a,a,a,a,a,a,a],
        [a,a,a,a,a,a,a,a,a,a,a,a,a,a]


        ],
    [
        [a,a,a,a,a,a,a,c,c,c,a,a,a,a],
        [c,a,a,c,c,c,c,a,a,a,c,c,a,a],
        [a,c,c,a,a,a,a,a,a,a,a,a,c,a],
        [a,a,a,a,a,a,a,a,a,a,a,a,a,c],
        [a,a,a,a,a,a,a,a,a,a,a,a,a,c],
        [a,c,c,a,a,a,a,a,a,a,a,a,c,a],
        [c,a,a,c,c,c,c,a,a,a,c,c,a,a],
        [a,a,a,a,a,a,a,c,c,c,a,a,a,a],
        [a,a,a,a,a,a,a,a,a,a,a,a,a,a],
        [a,a,a,a,a,a,a,a,a,a,a,a,a,a]


        ],
    [
        [a,a,a,a,a,a,a,c,c,c,a,a,a,a],
        [c,a,a,c,c,c,c,a,a,a,c,c,a,a],
        [a,c,c,a,a,a,a,a,a,a,a,a,c,a],
        [a,c,c,a,a,a,a,a,a,a,a,a,c,a],
        [a,c,c,a,a,a,a,a,a,a,a,a,c,a],
        [a,c,c,a,a,a,a,a,a,a,a,a,c,a],
        [c,a,a,c,c,c,c,a,a,a,c,c,a,a],
        [a,a,a,a,a,a,a,c,c,c,a,a,a,a],
        [a,a,a,a,a,a,a,a,a,a,a,a,a,a],
        [a,a,a,a,a,a,a,a,a,a,a,a,a,a]


        ],
    [
        [a,a,a,a,a,a,a,c,c,c,a,a,a,a],
        [c,a,a,c,c,c,c,a,a,a,c,c,a,a],
        [c,a,a,c,c,c,c,a,a,a,c,c,a,a],
        [c,a,a,c,c,c,c,a,a,a,c,c,a,a],
        [c,a,a,c,c,c,c,a,a,a,c,c,a,a],
        [c,a,a,c,c,c,c,a,a,a,c,c,a,a],
        [c,a,a,c,c,c,c,a,a,a,c,c,a,a],
        [a,a,a,a,a,a,a,c,c,c,a,a,a,a],
        [a,a,a,a,a,a,a,a,a,a,a,a,a,a],
        [a,a,a,a,a,a,a,a,a,a,a,a,a,a]


        ],
    [
        [a,a,a,a,a,a,a,c,c,c,a,a,a,a],
        [a,a,a,a,a,a,a,c,c,c,a,a,a,a],
        [a,a,a,a,a,a,a,c,c,c,a,a,a,a],
        [a,a,a,a,a,a,a,c,c,c,a,a,a,a],
        [a,a,a,a,a,a,a,c,c,c,a,a,a,a],
        [a,a,a,a,a,a,a,c,c,c,a,a,a,a],
        [a,a,a,a,a,a,a,c,c,c,a,a,a,a],
        [a,a,a,a,a,a,a,c,c,c,a,a,a,a],
        [a,a,a,a,a,a,a,a,a,a,a,a,a,a],
        [a,a,a,a,a,a,a,a,a,a,a,a,a,a]


        ],
    [
        [a,a,a,a,a,a,a,a,a,a,a,a,a,a],
        [a,a,a,a,a,a,a,a,a,a,a,a,a,a],
        [a,a,a,a,a,a,a,a,a,a,a,a,a,a],
        [a,a,a,a,a,a,a,a,a,a,a,a,a,a],
        [a,a,a,a,a,a,a,b,b,b,a,a,a,a],
        [a,a,a,a,a,a,a,b,a,b,a,a,a,a],
        [a,a,a,a,a,a,b,b,a,b,b,a,a,a],
        [a,a,a,a,a,a,b,a,a,a,b,a,a,a],
        [a,a,a,a,a,b,b,a,a,a,b,b,a,a],
        [a,a,a,a,b,b,b,b,b,b,b,b,b,a]


        ],
    [
        [a,a,a,a,a,a,a,a,a,a,a,a,a,a],
        [a,a,a,a,a,a,a,a,a,a,a,a,a,a],
        [a,a,a,a,a,a,a,a,a,a,a,a,a,a],
        [a,a,a,a,a,a,a,a,a,a,a,a,a,a],
        [a,a,a,a,a,a,a,b,b,b,a,a,a,a],
        [a,a,a,a,a,a,a,b,a,b,a,a,a,a],
        [a,a,a,a,a,a,b,b,a,b,b,a,a,a],
        [a,a,a,a,a,a,b,a,a,a,b,a,a,a],
        [a,a,a,a,a,b,b,a,a,a,b,b,a,a],
        [a,a,a,a,b,b,b,b,b,b,b,b,b,a]


        ]
    ]
for letter in bigarray:
    y=pos.y
    z=pos.z
    x+=1
    for level in letter:
        z=pos.z
        for block in level:
            mc.setBlock(x+3,y+8,z-10,block)
            z+=1
        y-=1
