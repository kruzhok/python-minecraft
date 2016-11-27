from mcpi.minecraft import Minecraft
from time import sleep
from random import randint
mc = Minecraft.create()

while True:
   name = input('Who will play? ')
   try:
       ID=mc.getPlayerEntityId(name)
   except:
       print('No such player server')
   else:
       break

pos = mc.entity.getTilePos(ID)
x,y,z = pos.x,pos.y,pos.z

pumX = x+randint(-10,10)
pumY = y+randint(-10,10)
pumZ = z+randint(-10,10)
mc.postToChat(3)
sleep(1)
mc.postToChat(2)
sleep(1)
mc.postToChat(1)
sleep(1)
mc.postToChat('Fight!')

mc.setBlock(pumX,pumY+1,pumZ,86)
mc.setBlock(pumX,pumY,pumZ,81)
mc.postToChat('Let\s play! I\'ll kill you, '+ name + '!')
counter = 0

while True:
   sleep(0.5)
   pos = mc.entity.getTilePos(ID)
   x,y,z = pos.x,pos.y,pos.z
   if mc.getBlock(pumX,pumY+1,pumZ)==0:
       counter+=1
       mc.postToChat('You killed'+str(counter)+'!')
       if counter==3:
           mc.postToChat('Awwww.. You Win! Or VIINNN! IM DRACULA!! BLEH BLEH BLEH!')
           break
   mc.setBlock(pumX,pumY+1,pumZ,0)
   mc.setBlock(pumX,pumY,pumZ,0)
   if x<pumX:
       pumX-=1
   elif x>pumX:
       pumX+=1
   if y<pumY:
       pumY-=1
   elif y>pumY:
       pumY+=1
   if z<pumZ:
       pumZ-=1
   elif z>pumZ:
       pumZ+=1
   mc.setBlock(pumX,pumY+1,pumZ,86)
   mc.setBlock(pumX,pumY,pumZ,81)

   if pumX==x and pumY==y and pumZ==z:
       mc.postToChat('Ouch!!!')
        
    
