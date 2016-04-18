# mini-game which build pumpkin in random place as far as you entered,
# you've got to crush pumpkin block to win or you will die in lava

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random
import time
pos = mc.player.getTilePos()
x,y,z = pos.x,pos.y,pos.z
aw = int(input("How many blocks?-->"))#количество блоков - сложность игры
qwerty = int(input("How many seconds?-->"))
poinsToWin = int(input("How many pumpkins?-->"))
mc.setBlocks(x-aw,y,z-aw,x+aw,y+aw,z+aw,89)#светящийся куб
mc.setBlocks(x-aw+1,y+1,z-aw+1,x+aw-1,y+aw-1,z+aw-1,0)#полость куба
pumX = x + random.randint(-aw+1,aw-1)#даём тыкве случайные координаты
pumY = y + random.randint(1,aw-1)
pumZ = z + random.randint(-aw+1,aw-1)
mc.setBlock(pumX,pumY,pumZ,86)#ставим тыкву
mc.setting('world_immutable',False)
timer = 5
while timer>0:
   time.sleep(1)
   mc.postToChat("You have "+str(timer)+" seconds to start")
   timer-=1
mc.postToChat("Find the pumpkin! Kill him!")
score = 0
while True:
   timer = qwerty
   while timer>0:
       time.sleep(1)
       mc.postToChat("You have "+str(timer)+" seconds left...")
       timer-=1
   if mc.getBlock(pumX,pumY,pumZ)!=86:
       mc.postToChat("Pumkin breaked! Well played! Go on!..")
       score+=1
       mc.postToChat("Yor score is "+str(score)+"/"+str(poinsToWin))
       if score>=poinsToWin:
           mc.postToChat("Winner!")
           break
       pumX = x + random.randint(-aw+1,aw-1)#даём тыкве случайные координаты
       pumY = y + random.randint(1,aw-1)
       pumZ = z + random.randint(-aw+1,aw-1)
       mc.setBlock(pumX,pumY,pumZ,86)#ставим тыкву
   else:
       mc.postToChat("You lost!!!!!")
       mc.setting('world_immutable',True)
       lavaLayer = 1
       while lavaLayer<aw-1:
           time.sleep(1)
           mc.setBlocks(x-aw+1,y+1+lavaLayer,z-aw+1,x+aw-1,y+1+lavaLayer,z+aw-1,11)
           lavaLayer+=1
       break