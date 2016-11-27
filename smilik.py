from mcpi.minecraft import Minecraft
from time import sleep
from random import randint
mc=Minecraft.create()


x,y,z=122,118,57
B=41
L=173
a=0
SMILE=[
          [
             [a,a,a,a,a,a,a,a],
             [a,a,a,a,a,a,a,a],
             [a,a,B,B,B,B,a,a],
             [a,a,B,B,B,B,a,a],
             [a,a,B,B,B,B,a,a],
             [a,a,B,B,B,B,a,a],
             [a,a,a,a,a,a,a,a],
             [a,a,a,a,a,a,a,a]
          ],
          [
             [a,a,a,a,a,a,a,a],
             [a,a,B,B,B,B,a,a],
             [a,B,B,B,B,B,B,a],
             [a,B,B,B,B,B,B,a],
             [a,B,B,B,B,B,B,a],
             [a,B,B,B,B,B,B,a],
             [a,a,B,B,B,B,a,a],
             [a,a,a,a,a,a,a,a]
          ],
          [
             [a,a,B,B,B,B,a,a],
             [a,B,B,B,B,B,B,a],
             [B,B,B,B,B,B,B,B],
             [B,B,B,B,B,B,B,B],
             [B,B,B,B,B,B,B,B],
             [B,B,B,B,B,B,B,B],
             [a,B,B,B,B,B,B,a],
             [a,a,B,B,B,B,a,a]
          ],
          [
             [a,a,B,B,B,B,a,a],
             [a,B,B,B,B,B,B,a],
             [B,B,B,B,B,B,B,B],
             [B,B,B,B,B,B,B,B],
             [B,B,B,B,B,B,B,B],
             [B,B,B,B,B,B,B,B],
             [a,B,B,B,B,B,B,a],
             [a,a,B,B,B,B,a,a]
          ],
          [
             [a,a,B,B,B,B,a,a],
             [a,B,B,B,B,B,B,a],
             [B,B,B,B,B,B,B,B],
             [B,B,B,B,B,B,B,B],
             [B,B,B,B,B,B,B,B],
             [B,B,B,B,B,B,B,B],
             [a,B,B,B,B,B,B,a],
             [a,a,B,B,B,B,a,a]
          ],
          [              
             [a,a,B,B,B,B,a,a],
             [a,B,B,B,B,B,B,a],
             [B,B,B,B,B,B,B,B],
             [B,B,B,B,B,B,B,B],
             [B,B,B,B,B,B,B,B],
             [B,B,B,B,B,B,B,B],
             [a,B,B,B,B,B,B,a],
             [a,a,B,B,B,B,a,a]
          ],
          [
             [a,a,a,a,a,a,a,a],
             [a,a,B,B,B,B,a,a],
             [a,B,B,B,B,B,B,a],
             [a,B,B,B,B,B,B,a],
             [a,B,L,B,B,B,B,a],
             [a,B,B,L,L,B,B,a],
             [a,a,B,B,B,B,a,a],
             [a,a,a,a,a,a,a,a]
          ],
          [
             [a,a,a,a,a,a,a,a],
             [a,a,a,a,a,a,a,a],
             [a,a,L,B,B,L,a,a],
             [a,a,B,B,B,B,a,a],
             [a,a,a,a,a,a,a,a],
             [a,a,a,a,a,a,a,a],
             [a,a,a,a,a,a,a,a],
             [a,a,a,a,a,a,a,a]
          ], 
             
        ]
h=0
while h<1:
    for part in SMILE:
             for line in part:
                 for block in line:
                     mc.setBlock(x+5,y+5,z,block)
                     x+=1
                 x=122
                 y-=1
             y=118
             z+=1
             sleep(1)
    h+=1
    z=z+1
