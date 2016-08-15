# mini-game in which you should guess random block from 3 variants and put it on another block
# if you guess right in 10 seconds - secret hall will open, othervise - you'll burn in lava
# attention!!! this game makes world immutable

from mcpi.minecraft import Minecraft
import time
import random
mc = Minecraft.create()

pos = mc.player.getTilePos()
x,y,z = pos.x,pos.y,pos.z

mc.setBlocks(x-10,y,z-10,x+10,y+10,z+10,89)
mc.setBlocks(x-10,y-1,z-10,x+10,y-1,z+10,2)
mc.setBlocks(x-5,y,z-5,x+5,y+5,z+5,0)
mc.setBlock(x+3,y,z,35,14)
mc.setting("world_immutable",True)
gold = 41
diamond = 57
glass = 20
blocks = [gold, diamond, glass]
k = random.randint(0,len(blocks))
b = blocks[k]

talks = {
        'hi': "Ha-Ha-Ha! Let's check, how lucky you are!",
        'guess': "Guess what? Gold, Diamond or Glass?",
        'instruct':"Put the block you choose on the red block!",
        'time':"You've got 10 seconds to choose",
        'success' : "You are so lucky! Run away!",
        'dead': "Burn, Looser!"
    }

mc.postToChat(talks.get('hi'))
time.sleep(2)
mc.postToChat(talks.get('guess'))
time.sleep(2)
mc.postToChat(talks.get('instruct'))
time.sleep(2)
mc.postToChat(talks.get('time'))
time.sleep(1)
mc.postToChat('3')
time.sleep(1)
mc.postToChat('2')
time.sleep(1)
mc.postToChat('1')
time.sleep(1)
mc.postToChat('Go!')
time.sleep(1)
mc.setting("world_immutable", False)
time.sleep(10)

if mc.getBlock(x+3,y+1,z)==b:
    mc.postToChat(talks.get('success'))
    mc.setBlocks(x+5,y,z-1,x+10,y+3,z+1,0)
else:
    mc.postToChat(talks.get('dead'))
    mc.postToChat('The correct block ID was ' + str(b))
    mc.setting("world_immutable",True)
    time.sleep(2)
    for i in range(0,5):
        mc.setBlocks(x-10,y-1,z-10,x+10,y+i,z+10,11)
        time.sleep(1)
    
