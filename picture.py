from mcpi.minecraft import Minecraft
import obj as o
mc = Minecraft.create()
name = input('Yuor name: ')
ID = mc.getPlayerEntityId(name)
pos = mc.entity.getTilePos(ID)
x,y,z = pos.x,pos.y,pos.z
a = 0
w = 2
q = (159,4)
r = 89
d = 1
c = (17,1)
s = (18,1)
e = 8
bigArray = [
               [
                    [q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q],
                    [q,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,q],
                    [q,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,q],
                    [q,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,q],
                    [q,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,q],
                    [q,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,q],
                    [q,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,q],
                    [q,a,s,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,q],
                    [q,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,q],
                    [q,a,s,a,a,a,a,a,a,a,a,a,a,s,a,a,a,a,a,q],
                    [q,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,s,a,a,q],
                    [q,a,s,a,a,a,a,a,a,a,a,a,a,s,a,a,a,a,a,q],
                    [q,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,q],
                    [q,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,q],
                    [q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q],

                ],
[
                    [q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q],
                    [q,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,q],
                    [q,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,q],
                    [q,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,q],
                    [q,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,q],
                    [q,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,q],
                    [q,a,s,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,q],
                    [q,s,c,s,a,a,a,a,a,a,a,a,s,a,a,a,a,a,a,q],
                    [q,a,c,a,a,a,a,a,a,a,a,a,a,s,a,s,a,a,a,q],
                    [q,s,c,s,s,a,a,a,a,a,a,a,s,c,s,a,s,a,a,q],
                    [q,a,c,a,a,a,a,a,a,a,a,a,a,c,a,s,c,s,a,q],
                    [q,s,c,s,s,s,a,a,a,a,a,s,s,c,s,s,c,s,s,q],
                    [q,a,c,a,a,a,a,a,a,a,a,a,a,c,a,a,c,a,a,q],
                    [q,w,c,w,w,w,e,e,e,e,e,e,w,c,s,s,c,s,s,q],
                    [q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q],

                ],
                [
                    [r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r],
                    [q,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,q],
                    [q,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,q],
                    [q,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,q],
                    [q,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,q],
                    [q,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,q],
                    [q,a,a,a,a,a,a,a,a,a,a,a,s,a,a,a,a,a,a,q],
                    [q,a,s,a,a,a,a,a,a,a,a,s,c,s,a,s,a,a,a,q],
                    [q,a,a,a,a,a,a,a,a,a,a,a,c,a,a,c,a,a,a,q],
                    [q,a,s,a,a,a,a,a,a,a,s,s,c,s,s,c,s,a,a,q],
                    [q,a,a,a,a,a,a,a,a,s,s,s,c,s,s,c,a,a,a,q],
                    [q,a,s,a,a,a,a,a,a,a,a,a,c,s,s,c,s,s,a,q],
                    [q,a,a,a,a,a,a,a,a,a,a,a,c,a,a,c,a,a,a,q],
                    [q,w,w,w,w,w,e,e,e,e,e,e,w,w,w,w,w,w,w,q],
                    [q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q],
               ],
[
                    [q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q],
                    [q,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,q],
                    [q,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,q],
                    [q,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,q],
                    [q,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,q],
                    [q,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,q],
                    [q,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,q],
                    [q,a,a,a,a,a,a,d,a,a,a,a,a,a,a,a,a,a,a,q],
                    [q,a,a,a,a,a,d,d,d,a,a,a,a,a,a,a,a,a,a,q],
                    [q,a,a,a,a,d,d,d,d,a,a,a,a,a,a,a,a,a,a,q],
                    [q,a,a,a,d,d,d,d,d,d,a,a,a,a,a,a,a,a,a,q],
                    [q,a,a,d,d,d,d,d,d,d,d,a,a,a,a,a,a,a,a,q],
                    [q,a,d,d,d,d,d,d,d,d,d,d,a,a,a,a,a,a,a,q],
                    [q,w,w,w,w,w,e,e,e,e,e,e,w,w,w,w,w,w,w,q],
                    [q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q],
                ],
                [
                    [q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q],
                    [q,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,q],
                    [q,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,q],
                    [q,a,a,a,a,a,a,a,a,d,a,a,a,a,a,a,a,a,a,q],
                    [q,a,a,a,a,a,a,a,d,d,d,a,a,a,a,a,a,a,a,q],
                    [q,a,a,a,a,a,a,d,d,d,d,a,a,a,a,a,a,a,a,q],
                    [q,a,a,a,a,a,a,d,d,d,d,d,a,a,a,a,a,a,a,q],
                    [q,a,a,a,a,a,d,d,d,d,d,d,a,a,a,a,a,a,a,q],
                    [q,a,a,a,d,d,d,d,d,d,d,d,d,a,a,a,a,a,a,q],
                    [q,a,a,d,d,d,d,d,d,d,d,d,d,a,a,a,a,a,a,q],
                    [q,a,d,d,d,d,d,d,d,d,d,d,d,d,a,a,a,a,a,q],
                    [q,a,d,d,d,d,d,d,d,d,d,d,d,d,a,a,a,a,a,q],
                    [q,d,d,d,d,d,d,d,d,d,d,d,d,d,d,a,a,a,a,q],
                    [q,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,q],
                    [q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q],
                ],
                [
                    [q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q],
                    [q,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,q],
                    [q,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,q],
                    [q,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,q],
                    [q,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,q],
                    [q,a,a,a,a,a,a,a,a,a,a,a,a,a,a,d,a,a,a,q],
                    [q,a,a,a,a,a,a,a,a,a,a,a,a,a,d,d,d,a,a,q],
                    [q,a,a,a,a,a,a,a,a,a,a,a,a,d,d,d,d,d,a,q],
                    [q,a,a,a,a,a,a,a,a,a,a,a,d,d,d,d,d,d,d,q],
                    [q,a,a,a,a,a,a,a,a,a,a,a,d,d,d,d,d,d,d,q],
                    [q,a,a,a,a,a,a,a,a,a,a,d,d,d,d,d,d,d,d,q],
                    [q,a,a,a,a,a,a,a,a,a,d,d,d,d,d,d,d,d,d,q],
                    [q,a,a,a,a,a,a,a,d,d,d,d,d,d,d,d,d,d,d,q],
                    [q,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,q],
                    [q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q],
               ],
[
                    [q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q],
                    [q,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,q],
                    [q,a,a,a,a,a,a,a,a,a,a,a,a,a,a,d,a,a,a,q],
                    [q,a,a,a,a,a,a,a,a,a,a,a,a,a,d,d,d,a,a,q],
                    [q,a,a,a,a,a,a,a,a,a,a,a,a,d,d,d,d,a,a,q],
                    [q,a,a,a,a,a,a,a,a,a,a,a,d,d,d,d,d,d,a,q],
                    [q,a,a,a,a,a,a,a,a,a,a,d,d,d,d,d,d,d,a,q],
                    [q,a,a,a,a,a,a,a,a,a,d,d,d,d,d,d,d,d,d,q],
                    [q,a,a,a,a,a,a,a,a,a,d,d,d,d,d,d,d,d,d,q],
                    [q,a,a,a,a,a,a,a,a,d,d,d,d,d,d,d,d,d,d,q],
                    [q,a,a,a,a,a,a,a,d,d,d,d,d,d,d,d,d,d,d,q],
                    [q,a,a,a,a,a,a,d,d,d,d,d,d,d,d,d,d,d,d,q],
                    [q,a,a,a,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,q],
                    [q,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,q],
                    [q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q],

              ]
    ]
for letter in bigArray:
    y=pos.y
    z=pos.z
    x+=1
    for level in letter:
        z=pos.z
        for block in level:
            mc.setBlock(x+3, y+5, z-3, block)
            z+=1
        y-=1
