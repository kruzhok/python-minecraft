from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time
import random

d = {
    "start":"Pumpkin: AAAHAHAHHHAH, Stevie! I'll kill you, man!!",
    "beat":["Pumpkin: Die!", "Steve: Aw, painful..."],
    "win":"Steve: I'll have a nice pumpkin pie today!"
    }

pumpX = x + random.randint(-10,10)#вводим переменные для координат тыквы
pumpY = y + random.randint(-10,10)
pumpZ = z + random.randint(-10,10)

mc.setBlock(pumpX,pumpY+1,pumpZ,86)#ставим тыквенную голову
mc.setBlock(pumpX,pumpY,pumpZ,81)#и тело из кактуса
mc.postToChat(d.get("start"))
while True:
    time.sleep(0.3)#пауза
    #если разбита голова, то вызод из цикла, пишем в чат win:
    if mc.getBlock(pumpX,pumpY+1,pumpZ)==0:
        mc.postToChat(d.get("win"))
        break
    pos = mc.player.getTilePos()#определяем позицию игрока
    x,y,z = pos.x,pos.y,pos.z
    
    mc.setBlocks(pumpX,pumpY,pumpZ,pumpX,pumpY+1,pumpZ,0)#удаляем старую тыкву
    
    #меняем координаты тыквы в зависимости от координат игрока:
    #по оси Y:
    if pumpY < y:#если тыква_Y больше игрок_Y, то уменьшить тыква_Y
        pumpY+=1
    elif pumpY > y:#а если тыква_Y меньше игрок_Y, то увеличить тыква_Y
        pumpY-=1
    #то же самое по оси X:
    if pumpX < x:
        pumpX+=1
    elif pumpX > x:
        pumpX-=1
    #то же самое по оси Z:
    if pumpZ < z:
        pumpZ+=1
    elif pumpZ > z:
        pumpZ-=1

    if pumpX == x and pumpY == y and pumpZ == z:#если тыква "бьёт Стива"
        mc.postToChat(d.get("beat")[0])
        mc.postToChat(d.get("beat")[1])
    #ставим новую тыкву на этих координатах
    mc.setBlock(pumpX,pumpY+1,pumpZ,86)#ставим тыквенную голову
    mc.setBlock(pumpX,pumpY,pumpZ,81)#и тело из кактуса
    

