from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time
import random
IDS = mc.getPlayerEntityIds()
x,y,z = [],[],[]
pumpX,pumpY,pumpZ = [],[],[]
print(IDS)
i = 0
while i < len(IDS):
    pos = mc.entity.getTilePos(IDS[i])#определяем позицию игрока
    x.append(pos.x)
    y.append(pos.y)
    z.append(pos.z)
    d = {
        "start":"Pumpkin: AAAHAHAHHHAH, Stevie! I'll kill you all!!",
        "beat":["Pumpkin: Die!", "Aw, painful..."],
        "win":"We'll have a nice pumpkin pie today!"
        }

    pumpX.append(x[i] + random.randint(-10,10))#вводим переменные для координат тыквы
    pumpY.append(y[i] + random.randint(-10,10))
    pumpZ.append(z[i] + random.randint(-10,10))

    mc.setBlock(pumpX[i],pumpY[i]+1,pumpZ[i],86)#ставим тыквенную голову
    mc.setBlock(pumpX[i],pumpY[i],pumpZ[i],81)#и тело из кактуса

    i = i + 1
mc.postToChat(d.get("start"))
n = 0
while n<len(IDS):
    n = 0
    time.sleep(0.2)#пауза
    i = 0
    IDS = mc.getPlayerEntityIds()
    while i < len(IDS):
        #если разбита голова, то вызод из цикла, пишем в чат win:
        if mc.getBlock(pumpX[i],pumpY[i]+1,pumpZ[i])==0:
            mc.postToChat(d.get("win"))
            n = n + 1
            break
        pos = mc.entity.getTilePos(IDS[i])#определяем позицию игрока
        x[i],y[i],z[i] = pos.x,pos.y,pos.z
        
        mc.setBlocks(pumpX[i],pumpY[i],pumpZ[i],pumpX[i],pumpY[i]+1,pumpZ[i],0)#удаляем старую тыкву
        
        #меняем координаты тыквы в зависимости от координат игрока:
        #по оси Y:
        if pumpY[i] < y[i]:#если тыква_Y больше игрок_Y, то уменьшить тыква_Y
            pumpY[i]+=1
        elif pumpY[i] > y[i]:#а если тыква_Y меньше игрок_Y, то увеличить тыква_Y
            pumpY[i]-=1
        #то же самое по оси X:
        if pumpX[i] < x[i]:
            pumpX[i]+=1
        elif pumpX[i] > x[i]:
            pumpX[i]-=1
        #то же самое по оси Z:
        if pumpZ[i] < z[i]:
            pumpZ[i]+=1
        elif pumpZ[i] > z[i]:
            pumpZ[i]-=1

        if pumpX[i] == x[i] and pumpY[i] == y[i] and pumpZ[i] == z[i]:#если тыква "бьёт Стива"
            mc.postToChat(d.get("beat")[0])
            mc.postToChat(d.get("beat")[1])
        #ставим новую тыкву на этих координатах
        mc.setBlock(pumpX[i],pumpY[i]+1,pumpZ[i],86)#ставим тыквенную голову
        mc.setBlock(pumpX[i],pumpY[i],pumpZ[i],81)#и тело из кактуса
    
        i = i + 1
