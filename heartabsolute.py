from mcpi.minecraft import Minecraft
from time import sleep
mc=Minecraft.create()
x=-65
y=141
z=1
q=z

a = 159,14
b = 155
c = 159,15
heart1 = [
  [0,0,0,c,c,0,0,0,0,0,c,c,0,0,0],
  [0,c,c,a,a,c,0,0,0,c,a,a,c,c,0],
  [c,a,a,a,a,a,c,0,c,a,a,a,a,a,c],
  [c,a,a,b,b,a,a,c,a,a,a,a,a,a,c],
  [c,a,a,b,b,a,a,a,a,a,a,a,a,a,c],
  [c,a,a,a,a,a,a,a,a,a,a,a,a,a,c],
  [0,c,a,a,a,a,a,a,a,a,a,a,a,c,0],
  [0,c,a,a,a,a,a,a,a,a,a,a,a,c,0],
  [0,0,c,a,a,a,a,a,a,a,a,a,c,0,0],
  [0,0,0,c,a,a,a,a,a,a,a,c,0,0,0],
  [0,0,0,0,c,a,a,a,a,a,c,0,0,0,0],
  [0,0,0,0,0,c,a,a,a,c,0,0,0,0,0],
  [0,0,0,0,0,0,c,a,c,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,c,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]

heart2 = [
  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
  [0,0,c,c,0,0,0,0,0,c,c,0,0,0,0],
  [0,c,a,a,c,0,0,0,c,a,a,c,0,0,0],
  [c,a,a,a,a,c,0,c,a,a,a,a,c,0,0],
  [c,a,a,b,a,a,c,a,a,a,a,a,c,0,0],
  [c,a,a,a,a,a,a,a,a,a,a,a,c,0,0],
  [0,c,a,a,a,a,a,a,a,a,a,c,0,0,0],
  [0,c,a,a,a,a,a,a,a,a,a,c,0,0,0],
  [0,0,c,a,a,a,a,a,a,a,c,0,0,0,0],
  [0,0,0,c,a,a,a,a,a,c,0,0,0,0,0],
  [0,0,0,0,c,a,a,a,c,0,0,0,0,0,0],
  [0,0,0,0,0,c,a,c,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,c,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]
def setHeart(x,y,z,heart):
  for line in heart:
      z = q
      for block in line:
          mc.setBlock(x,y,z,block)
          z = z + 1
      y = y - 1

while True:
    setHeart(x-1,y,z,heart1)
    setHeart(x,y,z,heart1)
    setHeart(x+1,y,z,heart1)
    sleep(0.5)

    setHeart(x-1,y,z,heart2)
    setHeart(x,y,z,heart2)
    setHeart(x+1,y,z,heart2)
    sleep(0.5)

    setHeart(x-1,y,z,heart1)
    setHeart(x,y,z,heart1)
    setHeart(x+1,y,z,heart1)
    setHeart(x+1,y,z,heart1)
    sleep(0.5)
