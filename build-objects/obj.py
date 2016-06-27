# minecraft cool objects library for Minecraft
# made during Alexander Patlukh's course in Moscow Coding School

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
import random

# butterfly

def butterfly(x,y,z):
    
    #body
    mc.setBlocks(x+5,y+5,z,x+8,y+5,z+1,35,14)
    mc.setBlocks(x+9,y+5,z-1,x+10,y+5,z-1,35,14)
    mc.setBlocks(x+9,y+5,z+2,x+10,y+5,z+2,35,14)
    mc.setBlock(x+11,y+5,z-2,35,14)
    mc.setBlock(x+11,y+5,z+3,35,14)
    mc.setBlocks(x+12,y+5,z-3,x+12,y+5,z-4,35,14)
    mc.setBlocks(x+12,y+5,z+4,x+12,y+5,z+5,35,14)
    mc.setBlock(x+13,y+5,z-4,35,14)
    mc.setBlock(x+13,y+5,z+5,35,14)
    #wings
    mc.setBlock(x+2,y+5,z-4,35,3)
    mc.setBlock(x+2,y+5,z+5,35,3)
    mc.setBlocks(x+3,y+5,z-1,x+4,y+5,z-3, 35,3)
    mc.setBlock(x+3,y+5,z-1,0)
    mc.setBlocks(x+3,y+5,z+2,x+4,y+5,z+4, 35,3)
    mc.setBlock(x+3,y+5,z+2,0)
    mc.setBlocks(x+5,y+5,z-2,x+8,y+5,z-2, 35,3)
    mc.setBlocks(x+5,y+5,z+3,x+8,y+5,z+3, 35,3)
    mc.setBlocks(x+6,y+5,z-3,x+9,y+5,z-3, 35,3)
    mc.setBlock(x+7,y+5,z-3,0)
    mc.setBlocks(x+6,y+5,z+4,x+9,y+5,z+4, 35,3)
    mc.setBlock(x+7,y+5,z+4,0)
    mc.setBlocks(x+7,y+5,z-4,x+10,y+5,z-4, 35,3)
    mc.setBlock(x+8,y+5,z-4,0)
    mc.setBlocks(x+7,y+5,z+5,x+10,y+5,z+5, 35,3)
    mc.setBlock(x+8,y+5,z+5,0)
    mc.setBlocks(x+8,y+5,z-5,x+11,y+5,z-5, 35,3)
    mc.setBlock(x+9,y+5,z-5,0)
    mc.setBlocks(x+8,y+5,z+6,x+11,y+5,z+6, 35,3)
    mc.setBlock(x+9,y+5,z+6,0)
    mc.setBlocks(x+9,y+5,z-6,x+12,y+5,z-6, 35,3)
    mc.setBlocks(x+9,y+5,z+7,x+12,y+5,z+7, 35,3)
    mc.setBlock(x+12,y+5,z-7,35,3)
    mc.setBlock(x+12,y+5,z+8,35,3)
    
#house with 2 stained-glass window
def stainGlassHouse(x,y,z):
    #коробка из кирпича
    mc.setBlocks(x-5,y,z-5,x+5,y+12,z+5,45)
    #коробка из воздуха
    mc.setBlocks(x-4,y,z-4,x+4,y+11,z+4,0)
    #сделать пол
    mc.setBlocks(x-5,y-1,z-5,x+5,y-1,z+5,1)
    #сделать дверь 1 в ширину 2 в высоту с калиткой из акации id 187
    mc.setBlocks(x,y,z+5,x,y+2,z+5,0)
    mc.setBlock(x,y+1,z+5,187)
    #сделаем витраж
    mc.setBlocks(x-3,y+4,z+5,x+3,y+10,z+5,95,5)
    mc.setBlocks(x+3,y+4,z-5,x-3,y+10,z-5,95,5)
    
#house with 7 windows, door, roof
def fourWindowsHouse(x,y,z):
    #пол
    mc.setBlocks(x+5,y-1,z+5,x-5,y-1,z-5,17)
    #стены
    mc.setBlocks(x+5,y,z+5,x-5,y+10,z-5,45)
    mc.setBlocks(x+4,y,z+4,x-4,y+9,z-4,0)
    #окна
    mc.setBlocks(x-1,y+1,z+5,x-4,y+4,z+5,95,2)
    mc.setBlocks(x+1,y+6,z+5,x+4,y+9,z+5,95,2)
    mc.setBlocks(x-1,y+6,z+5,x-4,y+9,z+5,95,2)
    mc.setBlocks(x-1,y+1,z-5,x-4,y+4,z-5,95,2)
    mc.setBlocks(x+1,y+6,z-5,x+4,y+9,z-5,95,2)
    mc.setBlocks(x-1,y+6,z-5,x-4,y+9,z-5,95,2)
    mc.setBlocks(x+1,y+1,z-5,x+4,y+4,z-5,95,2)
    #дверь
    mc.setBlocks(x+1,y,z+5,x+1,y+1,z+5,0)
    mc.setBlock(x+1,y,z+5,187)
    #крыша
    mc.setBlocks(x-6,y+11,z-6,x+6,y+11,z+6,41)

#house with traingle roof from lighter blocks
def traingleRoofHouse(x,y,z):
    #grass

    mc.setBlocks(x-10, y-1,z-10,x+10, y-1, z+10, 2)

    #road
    mc.setBlocks(x-10,y-1,z+11,x+10,y-1,z+14,1)

    #house

    mc.setBlocks(x-5,y,z-5,x+5,y+10,z+5,168)
    mc.setBlocks(x-4,y,z-4,x+4,y+9,z+4,0)

    #windows

    mc.setBlocks(x-5,y+2,z-1,x-5,y+3,z-2,20)
    mc.setBlocks(x-5,y+2,z+1,x-5,y+3,z+2,20)
    mc.setBlocks(x-5,y+5,z-1,x-5,y+6,z-2,20)
    mc.setBlocks(x-5,y+5,z+1,x-5,y+6,z+2,20)

    mc.setBlocks(x+5,y+2,z-1,x+5,y+3,z-2,20)
    mc.setBlocks(x+5,y+2,z+1,x+5,y+3,z+2,20)
    mc.setBlocks(x+5,y+5,z-1,x+5,y+6,z-2,20)
    mc.setBlocks(x+5,y+5,z+1,x+5,y+6,z+2,20)

    mc.setBlocks(x+1,y+5,z+5,x-1,y+7,z+5,20)

    #door
    mc.setBlocks(x+1,y,z+5,x-1,y+2,z+5,0)
    mc.setBlocks(x+1,y+1,z+5,x-1,y+1,z+5,184)

    #roof
    a=2
    while a>=-5:
        mc.setBlocks(x-5-a,y+10,z-5-a,x+5+a,y+10,z+5+a,89)
        a-=1
        y+=1

# Car which moves permanently and Stieve inside

def car(x,y,z):
    while True:
        mc.setBlocks(x+2,y-1,z-20,x+9,y-1,z+20,35,15)
         #красная шерсть — корпус машины 35.14
         #x — расстоние до тачки и её ширина
         #y — высота
         #z — длина
        mc.setBlocks(x+5,y+1,z,x+7,y+2,z+7,35,14)
         #стекло
        mc.setBlocks(x+5,y+3,z+2,x+7,y+4,z+5,20)

         #колеса — из черной шерсти 35,15
        mc.setBlocks(x+4,y,z+1,x+5,y+1,z+2,35,15)
        mc.setBlocks(x+4,y,z+5,x+5,y+1,z+6,35,15)
        mc.setBlocks(x+7,y,z+1,x+8,y+1,z+2,35,15)
        mc.setBlocks(x+7,y,z+5,x+8,y+1,z+6,35,15)
        #Стив внутри
        mc.player.setTilePos(x+6,y+3,z+4)
        z = z - 1
        time.sleep(0.5)
        mc.setBlocks(x,y,z,x+10,y+10,z+10,0)

# house with road, grass and tree

def houseWithRoad(x,y,z):
        #газон
    mc.setBlocks(x-10,y-1,z-10,x+10,y-1,z+10,2)
    #построим коробку
    mc.setBlocks(x-5,y-1,z-5,x+4,y+9,z+4,5)
    mc.setBlocks(x-4,y,z-4,x+3,y+8,z+3,0)
    #построим окна и вход
    mc.setBlocks(x-4,y+6,z+4,x-2,y+7,z+4,20)
    mc.setBlocks(x-4,y+3,z+4,x-2,y+4,z+4,20)
    mc.setBlocks(x+1,y+6,z+4,x+3,y+7,z+4,20)
    mc.setBlocks(x+1,y,z+4,x+2,y+2,z+4,0)
    #тротуар и дорога
    mc.setBlocks(x-10,y,z+6,x+10,y,z+9,44)
    mc.setBlocks(x-10,y-1,z+10,x+10,y-1,z+16,35,15)
    mc.setBlocks(x-10,y,z+17,x+10,y,z+19,44)
    #дерево
    mc.setBlocks(x+6,y+2,z-1,x+8,y+5,z+1,18)
    mc.setBlocks(x+7,y-1,z,x+7,y+4,z,5,1)

def musicPlayer(x,y,z):
    while True:
        time.sleep(0.2)
        mc.setBlocks(x+5,y,z-3,x+5,y+5,z+3,0)
        mc.setBlocks(x+5,y,z-3,x+5,y+random.randint(0,5),z-3,35,1)
        mc.setBlocks(x+5,y,z-2,x+5,y+random.randint(0,5),z-2,35,2)
        mc.setBlocks(x+5,y,z-1,x+5,y+random.randint(0,5),z-1,35,3)
        mc.setBlocks(x+5,y,z,x+5,y+random.randint(0,5),z,35,4)
        mc.setBlocks(x+5,y,z+1,x+5,y+random.randint(0,5),z+1,35,5)
        mc.setBlocks(x+5,y,z+2,x+5,y+random.randint(0,5),z+2,35,6)
        mc.setBlocks(x+5,y,z+3,x+5,x+random.randint(0,5),z+3,35,7)

# Airplane which moves 190 steps forvard and up. After it disappears
def airplane(x,y,z):
    while y<=190:
       x=x+1
       y=y+1
       #корпус
       mc.setBlocks(x+2,y,z-2,x+14,y+4,z+2, 35,14)
       #кабина
       mc.setBlocks(x+10,y+1,z-2,x+14,y+4,z+2,20)
       #воздух
       mc.setBlocks(x+11,y+2,z-1,x+13,y+3,z+1,0)
       #нос
       mc.setBlocks(x+15,y+1,z-1,x+15,y+3,z+1,20)
       mc.setBlock(x+16,y+2,z,20)
       #крылья
       a=8
       b=3
       while a>=3:
           mc.setBlocks(x+3,y+1,z+b,x+a,y+1,z+b,35)
           mc.setBlocks(x+3,y+1,z-b,x+a,y+1,z-b,35)
           a=a-1
           b=b+1
       c=6
       d=5
       while c>=3:
           mc.setBlocks(x+3,y+d,z,x+c,y+d,z,35)
           c-=1
           d+=1
       #турбины
           mc.setBlocks(x+1,y+1,z-2,x+1,y+3,z-2,138)
           mc.setBlocks(x+1,y+1,z+2,x+1,y+3,z+2,138)
       t.sleep(0.4)
       #kill
       mc.setBlocks(x+1,y,z-8,x+16,y+8,z+8,0)
# Add rocket
def setRocket(x,y,z):
    #определяю переменные материалов
    corpus = 152
    window = 20
    gold = 41
    zakrilki = 89
    #обод из прутьев
    mc.setBlocks(x+5,y+10,z-3,x+11,y+10,z+3,101)
    #строю корпус
    mc.setBlocks(x+6,y+4,z-2,x+10,y+19,z+2,corpus)
    #строю кабину
    mc.setBlocks(x+7,y+12,z-1,x+9,y+18,z+1,0)
    #строю окна
    mc.setBlocks(x+7,y+12,z-2,x+9,y+14,z-2,window)
    mc.setBlocks(x+7,y+16,z-2,x+9,y+18,z-2,window)
    mc.setBlocks(x+7,y+12,z+2,x+9,y+14,z+2,window)
    mc.setBlocks(x+7,y+16,z+2,x+9,y+18,z+2,window)
    #шпиль
    mc.setBlocks(x+7,y+20,z-1,x+9,y+20,z+1,gold)
    mc.setBlock(x+8,y+21,z,139,0)
    mc.setBlocks(x+8,y+22,z,x+8,y+23,z,101)
    #дверь
    mc.setBlocks(x+6,y+12,z,x+6,y+13,z,0)
    mc.setBlock(x+6,y+13,z,96)
    #закрылки
    mc.setBlocks(x+3,y,z,x+3,y+3,z,zakrilki)
    mc.setBlocks(x+4,y+2,z,x+4,y+5,z,zakrilki)
    mc.setBlocks(x+5,y+4,z,x+5,y+7,z,zakrilki)
    mc.setBlocks(x+11,y+4,z,x+11,y+7,z,zakrilki)
    mc.setBlocks(x+12,y+2,z,x+12,y+5,z,zakrilki)
    mc.setBlocks(x+13,y,z,x+13,y+3,z,zakrilki)
    mc.setBlocks(x+8,y,z-5,x+8,y+3,z-5,zakrilki)
    mc.setBlocks(x+8,y+2,z-4,x+8,y+5,z-4,zakrilki)
    mc.setBlocks(x+8,y+4,z-3,x+8,y+7,z-3,zakrilki)
    mc.setBlocks(x+8,y,z+5,x+8,y+3,z+5,zakrilki)
    mc.setBlocks(x+8,y+2,z+4,x+8,y+5,z+4,zakrilki)
    mc.setBlocks(x+8,y+4,z+3,x+8,y+7,z+3,zakrilki)
    #огонь
    mc.setBlocks(x+7,y+3,z-1,x+9,y+3,z+1,10)

#different kind of ships by #vikings team
def LODKA(x,y,z):
#каркас    
    mc.setBlocks(x-5,y-2,z,x+5,y-2,z,5,2)
    mc.setBlocks(x-5,y-1,z+1,x+5,y-1,z+1,5,2)
    mc.setBlocks(x-5,y-1,z-1,x+5,y-1,z-1,5,2)
    mc.setBlock(x-6,y-1,z,5,2)
    mc.setBlock(x+6,y-1,z,5,2)
    mc.setBlocks(x-5,y+2,z+2,x+5,y,z+2,5,2)
    mc.setBlocks(x-5,y+2,z-2,x+5,y,z-2,5,2)
    mc.setBlocks(x-6,y,z-1,x-6,y+2,z-1,5,2)
    mc.setBlocks(x-6,y,z+1,x-6,y+2,z+1,5,2)
    mc.setBlocks(x+6,y,z+1,x+6,y+2,z+1,5,2)
    mc.setBlocks(x+6,y,z-1,x+6,y+2,z-1,5,2)
    mc.setBlocks(x-7,y,z,x-7,y+2,z,5,2)
    mc.setBlocks(x-6,y+1,z,x+6,y+1,z,5,2)
    mc.setBlocks(x-5,y+1,z-1,x+5,y+1,z-1,5,2)
    mc.setBlocks(x-5,y+1,z+1,x+5,y+1,z+1,5,2)
    mc.setBlock(x+6,y,z,5,2)
#щитки
    mc.setBlock(x-4,y+3,z+2,42)
    mc.setBlock(x-4,y+3,z-2,42)
    mc.setBlock(x-1,y+3,z+2,42)
    mc.setBlock(x-1,y+3,z-2,42)
    mc.setBlock(x+2,y+3,z+2,42)
    mc.setBlock(x+2,y+3,z-2,42)
    mc.setBlock(x+5,y+3,z+2,42)
    mc.setBlock(x+5,y+3,z-2,42)
#задняя часть
    mc.setBlock(x-7,y+2,z-1,5,2)
    mc.setBlock(x-7,y+2,z+1,5,2)
    mc.setBlock(x-6,y+3,z-1,85)
    mc.setBlock(x-6,y+3,z+1,85)
    mc.setBlocks(x-7,y+3,z+1,x-7,y+3,z-1,85)
#спуск в трюм
    mc.setBlock(x+4,y+1,z,96,9)
    mc.setBlock(x+4,y,z-1,5,2)
    mc.setBlocks(x+4,y,z,x+4,y-1,z,65,3)
#таран
    mc.setBlocks(x+7,y+1,z-1,x+7,y+2,z+1,41)
    mc.setBlock(x+7,y+2,z,5,2)
    mc.setBlock(x+7,y+3,z,41)
    mc.setBlocks(x+8,y+2,z,x+8,y+4,z,41)
    mc.setBlocks(x+9,y+3,z,x+9,y+4,z,41)
    mc.setBlock(x+10,y+4,z,41)
#мачта
    mc.setBlocks(x,y+2,z,x,y+14,z,85)
    mc.setBlocks(x+1,y+5,z-3,x+1,y+5,z+3,35,0)
    mc.setBlocks(x+1,y+14,z-3,x+1,y+14,z+3,35,0)
    mc.setBlocks(x+2,y+13,z-3,x+2,y+6,z+3,35,0)
    mc.setBlocks(x+3,y+12,z-2,x+3,y+7,z+2,35,0)
    mc.setBlocks(x+2,y+12,z-2,x+2,y+7,z+2,0)
    mc.setBlocks(x+3,y+8,z,x+3,y+11,z,35,14)
    mc.setBlocks(x+3,y+11,z-1,x+3,y+11,z+1,35,14)
#трюм
    mc.setBlocks(x+1,y,z-1,x+2,y,z-1,54,2)
    mc.setBlocks(x+1,y,z+1,x+2,y,z+1,54,3)
    mc.setBlocks(x-1,y,z-1,x-2,y,z-1,54,2)
    mc.setBlocks(x-1,y,z+1,x-2,y,z+1,54,3)
    mc.setBlocks(x-4,y-1,z,x-4,y,z,101)
    mc.setBlock(x-4,y,z-1,5,2)
    mc.setBlock(x-4,y,z+1,5,2)
    mc.setBlock(x,y,z-2,85)
    mc.setBlock(x,y,z+2,85)
    mc.setBlock(x-3,y,z-2,85)
    mc.setBlock(x-3,y,z+2,85)
    mc.setBlock(x+3,y,z-2,85)
    mc.setBlock(x+3,y,z+2,85)

def setShip1(x,y,z):
    #дно
    mc.setBlocks(x-9,y,z-3,x+9,y,z+3,5,5)
    #борты
    mc.setBlocks(x-10,y+1,z-4,x+9,y+1,z-4,5,5)
    mc.setBlocks(x+10,y+1,z-3,x+10,y+1,z+3,5,5)
    mc.setBlocks(x-10,y+1,z+4,x+9,y+1,z+4,5,5)
    mc.setBlocks(x-10,y+1,z-4,x-10,y+1,z+4,5,5)
    #Парус
    mc.setBlocks(x+2,y+9,z-4,x+2,y+5,z+4,35)
    #мачта
    mc.setBlocks(x+1,y+10,z,x+1,y,z,162,1)
    mc.setBlocks(x+1,y+9,z-4,x+1,y+9,z+4,162,1)
    #рубка
    mc.setBlocks(x-10,y+3,z-4,x-7,y+1,z+4,5,5)
    mc.setBlocks(x-10,y+1,z-4,x-10,y+1,z+4,0)
    #рубка/лестница
    mc.setBlocks(x-4,y+1,z+3,x-4,y+1,z+4,5,5)
    mc.setBlocks(x-4,y+1,z-3,x-4,y+1,z-4,5,5)
    mc.setBlocks(x-5,y+1,z+3,x-5,y+2,z+4,5,5)
    mc.setBlocks(x-5,y+1,z-3,x-5,y+2,z-4,5,5)
    mc.setBlocks(x-6,y+1,z+3,x-6,y+3,z+4,5,5)
    mc.setBlocks(x-6,y+1,z-3,x-6,y+3,z-4,5,5)
    #рубка/борты
    mc.setBlocks(x-6,y+4,z-4,x-10,y+4,z-4,5,5)
    mc.setBlocks(x-6,y+4,z+4,x-10,y+4,z+4,5,5)
    mc.setBlocks(x-10,y+4,z-3,x-10,y+4,z+3,5,5)
    #рубка/штурвал
    mc.setBlocks(x-7,y+4,z,x-7,y+4,z,85)
    mc.setBlocks(x-7,y+5,z,x-7,y+5,z,5,3)
def setShip2(x,y,z):
   n = 10
   m = 35,8
   mc.setBlocks(x+2,y-1,z+4,x-2,y-1,z-4-n,5,5)
   mc.setBlocks(x+3,y,z+4,x-3,y,z-4-n,5,5)
   mc.setBlocks(x+3,y+1,z+5,x-3,y+1,z-5-n,5,5)
   mc.setBlocks(x+3,y+2,z+5,x-3,y+2,z-6-n,5,5)
   mc.setBlocks(x+3,y+3,z+6,x-3,y+3,z-7-n,5,5)
   mc.setBlocks(x+3,y+4,z+6,x-3,y+4,z-8-n,5,5)
   mc.setBlocks(x,y+4,z-7,x,y+4,z-10-n,5,5)
   mc.setBlocks(x+2,y+4,z+5,x-2,y+4,z-7-n,0)
   mc.setBlocks(x+2,y+3,z+5,x-2,y+3,z-5-n,0)
   mc.setBlocks(x+4,y+3,z+6,x-4,y+4,z-4-n,0)
   mc.setBlocks(x-3,y+3,z+2,x+3,y+5,z+6,5,5)
   mc.setBlocks(x-2,y+3,z+1,x+2,y+4,z+5,0)
   mc.setBlocks(x-2,y+4,z+6,x+2,y+4,z+6,102)
   mc.setBlocks(x+2,y+4,z+2,x-1,y+3,z+2,5,5)
   mc.setBlocks(x-2,y+3,z+2,x-2,y+3,z+2,183)
   mc.setBlocks(x+4,y+3,z+1,x+4,y+3,z-4-n,190)
   mc.setBlocks(x-4,y+3,z+1,x-4,y+3,z-4-n,190)
   mc.setBlocks(x-3,y+4,z-4-n,x-3,y+4,z-7-n,190)
   mc.setBlocks(x+3,y+4,z-4-n,x+3,y+4,z-7-n,190)
   mc.setBlocks(x+2,y+1,z+4,x-2,y+1,z-4-n,0)
   mc.setBlocks(x+2,y,z+3,x-2,y,z-3-n,0)
   mc.setBlocks(x+4,y+2,z+1,x-4,y+2,z-14,5,5)
   mc.setBlocks(x+4,y+1,z-13,x+4,y+1,z,5,5)
   mc.setBlocks(x-4,y+1,z-13,x-4,y+1,z,5,5)
   mc.setBlocks(x+3,y+3,z-14,x+3,y+3,z-14,190)
   mc.setBlocks(x-3,y+3,z-14,x-3,y+3,z-14,190)
   mc.setBlocks(x+3,y+3,z-14,x+3,y+4,z-14,190)
   mc.setBlocks(x,y+3,z-4,x,y+20,z-4,5,5)
   mc.setBlocks(x+5,y+17,z-5,x-5,y+17,z-5,5,5)
   mc.setBlocks(x+4,y+8,z-5,x-4,y+8,z-5,5,5)
   mc.setBlocks(x,y+3,z-12,x,y+13,z-12,5,5)
   mc.setBlocks(x-3,y+6,z-12,x+3,y+6,z-12,5,5)
   mc.setBlocks(x-4,y+11,z-13,x+4,y+11,z-13,5,5)
   mc.setBlocks(x-5,y+15,z-6,x+5,y+17,z-6,m)
   mc.setBlocks(x-4,y+11,z-7,x+4,y+14,z-7,m)
   mc.setBlocks(x-3,y+8,z-6,x+3,y+10,z-6,m)
   mc.setBlocks(x-4,y+8,z-14,x+4,y+10,z-14,m)
   mc.setBlocks(x-3,y+6,z-13,x+3,y+7,z-13,m)
   mc.setBlocks(x+3,y+3,z-17,x+3,y+5,z-18,0)
   mc.setBlocks(x-3,y+3,z-17,x-3,y+5,z-18,0)
   mc.setBlocks(x+2,y+4,z-18,x+2,y+5,z-18,0)
   mc.setBlocks(x-2,y+4,z-18,x-2,y+5,z-18,0)
   mc.setBlocks(x+2,y+4,z-17,x+2,y+4,z-17,5,5)
   mc.setBlocks(x-2,y+4,z-17,x-2,y+4,z-17,5,5)
   mc.setBlocks(x,y+5,z-20,x,y+5,z-22,5,5)
   mc.setBlocks(x,y+6,z+3,x,y+6,z+3,192)
   mc.setBlocks(x,y+7,z+3,x,y+7,z+3,96)
   mc.setBlocks(x+3,y+6,z+2,x+3,y+6,z+6,190)
   mc.setBlocks(x+3,y+6,z+6,x-3,y+6,z+6,190)
   mc.setBlocks(x-3,y+6,z+2,x-3,y+6,z+6,190)
   mc.setBlocks(x+1,y,z+1,x+1,y,z+1,5,5)
   mc.setBlocks(x,y,z+1,x,y+2,z+1,5,5)
   mc.setBlocks(x+2,y,z+3,x+1,y,z+3,54)
   mc.setBlocks(x-2,y,z+3,x-1,y,z+3,54)
   mc.setBlocks(x-2,y,z-11,x-1,y,z-2,171,14)
   mc.setBlocks(x-1,y,z-11,x-1,y,z-2,171)
   mc.setBlocks(x-3,y+1,z-7,x-3,y+1,z-2,50)
   mc.setBlocks(x+3,y+1,z-7,x+3,y+1,z-7,50)
   mc.setBlocks(x+1,y+3,z+4,x+0,y+3,z+4,171,14)
   mc.setBlocks(x+1,y+3,z+5,x+0,y+3,z+5,171)
   mc.setBlocks(x-1,y+3,z+5,x-2,y+3,z+5,54)
   mc.setBlocks(x,y+2,z+1,x+3,y+2,z+1,0)
   mc.setBlocks(x+1,y+3,z-1,x+2,y+3,z-1,5,5)
   mc.setBlocks(x+1,y+4,z,x+2,y+4,z,5,5)
   mc.setBlocks(x+1,y+5,z+1,x+2,y+5,z+1,5,5)
   mc.setBlocks(x+2,y+3,z+5,x+2,y+3,z+5,47)
def setShip3(x,y,z):
    mc.setBlocks(x+10,y-1,z-10,x-10,y+20,z+10,0)
    mc.setBlocks(x+20,y-1,z-20,x-20,y-10,z+20,9)
    mc.setBlocks(x+20,y-1,z-20,x+20,y-10,z+20,1)
    mc.setBlocks(x-20,y-1,z-20,x-20,y-10,z+20,1)
    mc.setBlocks(x+20,y-1,z-20,x-20,y-10,z-20,1)
    mc.setBlocks(x+20,y-1,z+20,x-20,y-10,z+20,1)
    mc.setBlocks(x+20,y-10,z-20,x-20,y-10,z+20,1)
    mc.setBlock(x+11,y+1,z,5,3)
    mc.setBlocks(x+10,y+1,z+1,x+9,y+1,z+1,5,3)
    mc.setBlocks(x+10,y+1,z-1,x+9,y+1,z-1,5,3)
    mc.setBlocks(x+8,y+1,z+2,x+6,y+1,z+2,5,3)
    mc.setBlocks(x+8,y+1,z-2,x+6,y+1,z-2,5,3)
    mc.setBlocks(x+5,y+1,z+3,x+3,y+1,z+3,5,3)
    mc.setBlocks(x+5,y+1,z-3,x+3,y+1,z-3,5,3)
    mc.setBlocks(x+2,y+1,z+4,x,y+1,z+4,5,3)
    mc.setBlocks(x+2,y+1,z-4,x,y+1,z-4,5,3)
    mc.setBlocks(x-1,y+1,z-5,x-5,y+1,z-5,5,3)
    mc.setBlocks(x-1,y+1,z+5,x-5,y+1,z+5,5,3)
    mc.setBlocks(x-6,y+1,z-4,x-8,y+1,z-4,5,3)
    mc.setBlocks(x-6,y+1,z+4,x-8,y+1,z+4,5,3)
    mc.setBlocks(x-9,y+1,z-3,x-9,y+1,z-2,5,3)
    mc.setBlocks(x-9,y+1,z+3,x-9,y+1,z+2,5,3)
    mc.setBlocks(x-10,y+1,z+1,x-10,y+1,z-1,5,3)
    mc.setBlock(x-10,y,z,5,3)
    mc.setBlocks(x-9,y,z+1,x-9,y,z-1,5,3)
    mc.setBlocks(x-8,y,z+3,x-6,y,z+2,5,3)
    mc.setBlocks(x-8,y,z-3,x-6,y,z-2,5,3)
    mc.setBlocks(x-5,y,z+4,x-1,y,z+3,5,3)
    mc.setBlocks(x-5,y,z-4,x-1,y,z-3,5,3)
    mc.setBlocks(x,y,z+3,x+2,y,z+2,5,3)
    mc.setBlocks(x,y,z-3,x+2,y,z-2,5,3)
    mc.setBlocks(x+3,y,z+2,x+5,y,z+1,5,3)
    mc.setBlocks(x+3,y,z-2,x+5,y,z-1,5,3)
    mc.setBlocks(x+6,y,z+1,x+8,y,z-1,5,3)
    mc.setBlocks(x+9,y,z,x+10,y,z,5,3)
    mc.setBlocks(x+4,y-1,z,x+6,y-1,z,5,3)
    mc.setBlocks(x+3,y-1,z,x+3,y-1,z,5,3)
    mc.setBlocks(x,y-1,z-1,x+2,y-1,z+1,5,3)
    mc.setBlocks(x-1,y-1,z-2,x-5,y-1,z+2,5,3)
    mc.setBlocks(x-6,y-1,z-1,x-8,y-1,z+1,5,3)
    mc.setBlock(x+11,y+2,z,50)
    mc.setBlock(x-3,y+2,z-5,50)
    mc.setBlock(x-3,y+2,z+5,50)
    mc.setBlock(x-9,y+2,z-3,76)
    mc.setBlock(x-9,y+2,z+3,76)
    mc.setBlocks(x-1,y,z,x-1,y+10,z,192)
    mc.setBlocks(x-1,y+10,z-4,x-1,y+10,z+4,192)
    mc.setBlocks(x,y+10,z-4,x,y+10,z+4,35,11)
    mc.setBlocks(x,y+5,z-4,x,y+5,z+4,35,11)
    mc.setBlocks(x+1,y+6,z-4,x+1,y+9,z+4,35,11)
    mc.setBlock(x-6,y+1,z-3,58)
    mc.setBlock(x-7,y+1,z-3,61)
    mc.setBlock(x-8,y+1,z-3,116)
    mc.setBlock(x-6,y+1,z+3,130)
    mc.setBlock(x-7,y+1,z+3,54)
    mc.setBlock(x-8,y+1,z+3,54)
    mc.setBlocks(x-9,y+1,z-1,x-9,y+1,z+1,47)
def setShip4(x,y,z):
   mc.setBlocks(x+7,y-1,z,x+14,y-1,z+15,8)
   mc.setBlocks(x+8,y,z+1,x+13,y+3,z+14,5)
   mc.setBlocks(x+9,y+1,z+2,x+12,y+2,z+13,0)
   mc.setBlocks(x+9,y+1,z,x+12,y+3,z,5)
   mc.setBlocks(x+9,y+1,z+15,x+12,y+3,z+15 ,5)
   mc.setBlocks(x+10,y+2,z-1,x+11,y+3,z+16 ,5)
   mc.setBlocks(x+10,y+4,z-5,x+11,y+4,z+20 ,5)
   mc.setBlocks(x+10,y+4,z,x+12,y+4,z+15 ,0)
   mc.setBlocks(x+10,y+4,z+3,x+11,y+11,z+4 ,5)
   mc.setBlocks(x+10,y+4,z+10,x+11,y+11,z+11 ,5)
   mc.setBlocks(x+6,y+12,z+3,x+15,y+12,z+4 ,5)
   mc.setBlocks(x+6,y+12,z+10,x+15,y+12,z+11 ,5)
   mc.setBlocks(x+6,y+11,z+2,x+15,y+11,z+2 ,35)
   mc.setBlocks(x+6,y+7,z+1,x+15,y+10,z+1 ,35)
   mc.setBlocks(x+6,y+6,z+2,x+15,y+6,z+2 ,35)
   mc.setBlocks(x+6,y+11,z+9,x+15,y+11,z+9,35)
   mc.setBlocks(x+6,y+7,z+8,x+15,y+10,z+8,35)
   mc.setBlocks(x+6,y+6,z+9,x+15,y+6,z+9,35)
   mc.setBlocks(x+10,y+3,z+5,x+11,y+3,z+7,0)
   mc.setBlocks(x+9,y+1,z+2,x+12,y+2,z+13,0)
   mc.setBlocks(x+10,y+2,z+7,x+11,y+2,z+7,5)
   mc.setBlocks(x+10,y+1,z+6,x+11,y+1,z+6,5)
   mc.setBlocks(x+8,y,z+1,x+8,y,z+14,0)
   mc.setBlocks(x+13,y,z+1,x+13,y,z+14,0)
   mc.setBlocks(x+7,y+2,z+4,x+6,y+2,z+4,1,6)
   mc.setBlocks(x+7,y+2,z+7,x+6,y+2,z+7,1,6)
   mc.setBlocks(x+7,y+2,z+10,x+6,y+2,z+10,1,6)
   mc.setBlocks(x+7,y+2,z+13,x+6,y+2,z+13,1,6)
   mc.setBlocks(x+14,y+2,z+4,x+15,y+2,z+4,1,6)
   mc.setBlocks(x+14,y+2,z+7,x+15,y+2,z+7,1,6)
   mc.setBlocks(x+14,y+2,z+10,x+15,y+2,z+10,1,6)
   mc.setBlocks(x+14,y+2,z+13,x+15,y+2,z+13,1,6)
   mc.setBlocks(x+8,y+2,z+4,x+8,y+2,z+4,126)
   mc.setBlocks(x+8,y+2,z+7,x+8,y+2,z+7,126)
   mc.setBlocks(x+8,y+2,z+10,x+8,y+2,z+10,126)
   mc.setBlocks(x+8,y+2,z+13,x+8,y+2,z+13,126)
   mc.setBlocks(x+13,y+2,z+4,x+13,y+2,z+4,126)
   mc.setBlocks(x+13,y+2,z+7,x+13,y+2,z+7,126)
   mc.setBlocks(x+13,y+2,z+10,x+13,y+2,z+10,126)
   mc.setBlocks(x+13,y+2,z+13,x+13,y+2,z+13,126)
   mc.setBlocks(x+10,y+2,z,x+11,y+2,z,169)
   mc.setBlocks(x+10,y+2,z+1,x+11,y+2,z+1,20)
   mc.setBlocks(x+10,y+2,z+15,x+11,y+2,z+14,20)
   mc.setBlocks(x+10,y+2,z+15,x+11,y+2,z+15,169)
   mc.setBlock(x+7,y+11,z+4,85)
   mc.setBlock(x+7,y+10,z+4,169)
   mc.setBlock(x+15,y+11,z+4,85)
   mc.setBlock(x+15,y+10,z+4,169)
   mc.setBlock(x+8,y+11,z+11,85)
   mc.setBlock(x+8,y+10,z+11,169)
   mc.setBlock(x+15,y+11,z+11,85)
   mc.setBlock(x+15,y+10,z+11,169)

#soccer court
def setPitch(x,y,z):
    a=0
    c=35
    d=2
    b=41
    fieldArray=[
            [
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [b,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,b],
                [b,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,b],
                [b,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,b],
                [b,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,b],
                [b,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,b],
                [b,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,b],
                [b,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,b],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
            ],
            [
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [b,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,b],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [b,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,b],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
            ],
            [
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [b,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,b],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [b,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,b],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
            ],
            [
                [c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c],
                [c,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,c,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,c],
                [c,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,c,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,c],
                [c,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,c,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,c],
                [c,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,c,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,c],
                [c,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,c,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,c],
                [c,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,c,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,c],
                [c,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,c,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,c],
                [c,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,c,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,c],
                [c,c,c,c,c,c,c,c,c,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,c,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,c,c,c,c,c,c,c,c,c],
                [c,d,d,d,d,d,d,d,c,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,c,c,c,c,c,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,c,d,d,d,d,d,d,d,c],
                [c,d,d,d,d,d,d,d,c,c,c,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,c,c,d,d,d,d,d,c,c,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,c,c,c,d,d,d,d,d,d,d,c],
                [c,c,c,d,d,d,d,d,c,d,c,c,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,c,c,d,d,d,d,d,d,d,c,c,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,c,c,d,c,d,d,d,d,c,c,c,c],
                [c,d,c,d,d,d,d,d,c,d,d,c,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,c,d,d,d,d,d,d,d,d,d,c,d,d,d,d,d,d,d,d,d,d,d,d,d,d,c,c,d,d,c,d,d,d,d,c,d,d,c],
                [c,d,c,d,d,d,d,d,c,d,d,d,c,d,d,d,d,d,d,d,d,d,d,d,d,d,c,d,d,d,d,d,d,d,d,d,d,d,c,d,d,d,d,d,d,d,d,d,d,d,d,d,c,d,d,d,c,d,d,d,d,c,d,d,c],
                [c,d,c,d,d,d,d,d,c,d,d,d,c,d,d,d,d,d,d,d,d,d,d,d,d,d,c,d,d,d,d,d,d,d,d,d,d,d,c,d,d,d,d,d,d,d,d,d,d,d,d,d,c,d,d,d,c,d,d,d,d,c,d,d,c],
                [c,d,c,d,d,d,c,d,c,d,d,d,c,d,d,d,d,d,d,d,d,d,d,d,d,d,c,d,d,d,d,d,c,d,d,d,d,d,c,d,d,d,d,d,d,d,d,d,d,d,d,d,c,d,d,d,c,d,c,d,d,c,d,d,c],
                [c,d,c,d,d,d,d,d,c,d,d,d,c,d,d,d,d,d,d,d,d,d,d,d,d,d,c,d,d,d,d,d,d,d,d,d,d,d,c,d,d,d,d,d,d,d,d,d,d,d,d,d,c,d,d,d,c,d,d,d,d,c,d,d,c],
                [c,d,c,d,d,d,d,d,c,d,d,d,c,d,d,d,d,d,d,d,d,d,d,d,d,d,c,d,d,d,d,d,d,d,d,d,d,d,c,d,d,d,d,d,d,d,d,d,d,d,d,d,d,c,d,d,c,d,d,d,d,c,d,d,c],
                [c,d,c,d,d,d,d,d,c,d,d,c,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,c,d,d,d,d,d,d,d,d,d,c,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,c,c,d,c,d,d,d,d,c,d,d,c],
                [c,c,c,d,d,d,d,d,c,d,c,c,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,c,c,d,d,d,d,d,d,d,c,c,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,c,c,c,d,d,d,d,c,c,c,c],
                [c,d,d,d,d,d,d,d,c,c,c,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,c,c,d,d,d,d,d,c,c,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,c,d,d,d,d,d,d,d,c],
                [c,d,d,d,d,d,d,d,c,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,c,c,c,c,c,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,c,d,d,d,d,d,d,d,c],
                [c,c,c,c,c,c,c,c,c,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,c,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,c,c,c,c,c,c,c,c,c],
                [c,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,c,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,c],
                [c,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,c,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,c],
                [c,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,c,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,c],
                [c,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,c,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,c],
                [c,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,c,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,c],
                [c,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,c,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,c],
                [c,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,c,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,c],
                [c,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,c,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,d,c],
                [c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c],
            ]
        ]
    while True: 
        for pattern in fieldArray:
            y=pos.y
            z=pos.z
            x=pos.x
            for level in pattern:
                z=pos.z
                for block in level:
                    mc.setBlock(x+3, y+3, z-3, block)
                    z+=1
                x+=1
            y-=1
        break

#treasure house
def setSkyscraper(x,y,z):
    a = 0
    b = (95,15)
    c = 42
    d = 89
    e = (159,7)
    f = 41
    g = 57
    h = (1,6)
    bigArray = [                                 
                    [
                         [c,c,c,c,c,c,c],
                         [d,d,d,d,d,d,d],
                         [c,b,b,b,b,b,c],
                         [c,b,b,b,b,b,c],
                         [c,b,b,b,b,b,c],
                         [c,c,c,c,c,c,c],
                         [c,b,b,b,b,b,c],
                         [c,b,b,b,b,b,c],
                         [c,b,b,b,b,b,c],
                         [c,c,c,c,c,c,c],
                         [c,b,b,b,b,b,c],
                         [c,b,b,b,b,b,c],
                         [c,b,b,b,b,b,c],
                         [c,c,c,c,c,c,c],
                         [c,b,b,b,b,b,c],
                         [c,b,b,b,b,b,c],
                         [c,b,b,b,b,b,c],
                         [c,c,c,c,c,c,c],
                         [c,b,b,b,b,b,c],
                         [c,b,b,b,b,b,c],
                         [c,b,b,b,b,b,c],
                         [c,c,c,c,c,c,c],
                         [c,b,b,b,b,b,c],
                         [c,b,b,b,b,b,c],
                         [c,b,b,b,b,b,c],
                         [c,c,c,c,c,c,c],
                         [e,a,e,a,e,a,e],
                         [e,a,e,a,e,a,e],
                         [e,a,e,a,e,a,e],
                         [e,a,e,a,e,a,e],
                         [h,h,h,h,h,h,h]
                    ],
                    [
                         [c,c,c,c,c,c,c],
                         [d,d,d,d,d,d,d],
                         [b,a,a,a,a,a,b],
                         [b,a,a,a,a,a,b],
                         [c,a,a,a,a,a,b],
                         [c,c,c,c,c,c,c],
                         [b,a,a,a,a,a,b],
                         [b,a,a,a,a,a,b],
                         [b,a,a,a,a,a,b],
                         [c,c,c,c,c,c,c],
                         [b,a,a,a,a,a,b],
                         [b,a,a,a,a,a,b],
                         [b,a,a,a,a,a,b],
                         [c,c,c,c,c,c,c],
                         [b,a,a,a,a,a,b],
                         [b,a,a,a,a,a,b],
                         [b,a,a,a,a,a,b],
                         [b,c,c,c,c,c,c],
                         [b,a,a,a,a,a,b],
                         [b,a,a,a,a,a,b],
                         [b,a,a,a,a,a,b],
                         [c,c,c,c,c,c,c],
                         [b,a,a,a,a,a,b],
                         [b,a,a,a,a,a,b],
                         [b,a,a,a,a,a,b],
                         [c,c,c,c,c,c,c],
                         [a,e,a,e,a,e,a],
                         [a,e,a,e,a,e,a],
                         [a,e,a,e,a,e,a],
                         [a,e,a,e,a,e,a],
                         [h,h,h,h,h,h,h]
                    ],
                    [
                         
                         [c,c,c,c,c,c,c],
                         [d,d,d,d,d,d,d],
                         [b,a,g,g,g,a,b],
                         [b,a,g,g,g,a,b],
                         [c,a,g,g,g,a,b],
                         [c,c,c,c,c,c,c],
                         [b,a,f,f,f,a,b],
                         [b,a,f,f,f,a,b],
                         [b,a,f,f,f,a,b],
                         [c,c,c,c,c,c,c],
                         [b,a,g,g,g,a,b],
                         [b,a,g,g,g,a,b],
                         [b,a,g,g,g,a,b],
                         [c,c,c,c,c,c,c],
                         [b,a,f,f,f,a,b],
                         [b,a,f,f,f,a,b],
                         [b,a,f,f,f,a,b],
                         [b,c,c,c,c,c,c],
                         [b,a,g,g,g,a,b],
                         [b,a,g,g,g,a,b],
                         [b,a,g,g,g,a,b],
                         [c,c,c,c,c,c,c],
                         [b,a,f,f,f,a,b],
                         [b,a,f,f,f,a,b],
                         [b,a,f,f,f,a,b],
                         [c,c,c,c,c,c,c],
                         [e,a,e,a,e,a,e],
                         [e,a,e,a,e,a,e],
                         [e,a,e,a,e,a,e],
                         [e,a,e,a,e,a,e],
                         [h,h,h,h,h,h,h]
                    ],
                    [
                         [c,c,c,c,c,c,c],
                         [d,d,d,d,d,d,d],
                         [b,a,g,g,g,a,b],
                         [b,a,g,g,g,a,b],
                         [c,a,g,g,g,a,b],
                         [c,c,c,c,c,c,c],
                         [b,a,f,f,f,a,b],
                         [b,a,f,f,f,a,b],
                         [b,a,f,f,f,a,b],
                         [c,c,c,c,c,c,c],
                         [b,a,g,g,g,a,b],
                         [b,a,g,g,g,a,b],
                         [b,a,g,g,g,a,b],
                         [c,c,c,c,c,c,c],
                         [b,a,f,f,f,a,b],
                         [b,a,f,f,f,a,b],
                         [b,a,f,f,f,a,b],
                         [b,c,c,c,c,c,c],
                         [b,a,g,g,g,a,b],
                         [b,a,g,g,g,a,b],
                         [b,a,g,g,g,a,b],
                         [c,c,c,c,c,c,c],
                         [b,a,f,f,f,a,b],
                         [b,a,f,f,f,a,b],
                         [b,a,f,f,f,a,b],
                         [c,c,c,c,c,c,c],
                         [a,e,a,e,a,e,a],
                         [a,e,a,e,a,e,a],
                         [a,e,a,e,a,e,a],
                         [a,e,a,e,a,e,a],
                         [h,h,h,h,h,h,h]
                    ],
                    [
                         [c,c,c,c,c,c,c],
                         [d,d,d,d,d,d,d],
                         [b,a,g,g,g,a,b],
                         [b,a,g,g,g,a,b],
                         [c,a,g,g,g,a,b],
                         [c,c,c,c,c,c,c],
                         [b,a,f,f,f,a,b],
                         [b,a,f,f,f,a,b],
                         [b,a,f,f,f,a,b],
                         [c,c,c,c,c,c,c],
                         [b,a,g,g,g,a,b],
                         [b,a,g,g,g,a,b],
                         [b,a,g,g,g,a,b],
                         [c,c,c,c,c,c,c],
                         [b,a,f,f,f,a,b],
                         [b,a,f,f,f,a,b],
                         [b,a,f,f,f,a,b],
                         [b,c,c,c,c,c,c],
                         [b,a,g,g,g,a,b],
                         [b,a,g,g,g,a,b],
                         [b,a,g,g,g,a,b],
                         [c,c,c,c,c,c,c],
                         [b,a,f,f,f,a,b],
                         [b,a,f,f,f,a,b],
                         [b,a,f,f,f,a,b],
                         [c,c,c,c,c,c,c],
                         [e,a,e,a,e,a,e],
                         [e,a,e,a,e,a,e],
                         [e,a,e,a,e,a,e],
                         [e,a,e,a,e,a,e],
                         [h,h,h,h,h,h,h]
                    ],
                    [
                         
                         [c,c,c,c,c,c,c],
                         [d,d,d,d,d,d,d],
                         [b,a,a,a,a,a,b],
                         [b,a,a,a,a,a,b],
                         [c,a,a,a,a,a,b],
                         [c,c,c,c,c,c,c],
                         [b,a,a,a,a,a,b],
                         [b,a,a,a,a,a,b],
                         [b,a,a,a,a,a,b],
                         [c,c,c,c,c,c,c],
                         [b,a,a,a,a,a,b],
                         [b,a,a,a,a,a,b],
                         [b,a,a,a,a,a,b],
                         [c,c,c,c,c,c,c],
                         [b,a,a,a,a,a,b],
                         [b,a,a,a,a,a,b],
                         [b,a,a,a,a,a,b],
                         [b,c,c,c,c,c,c],
                         [b,a,a,a,a,a,b],
                         [b,a,a,a,a,a,b],
                         [b,a,a,a,a,a,b],
                         [c,c,c,c,c,c,c],
                         [b,a,a,a,a,a,b],
                         [b,a,a,a,a,a,b],
                         [b,a,a,a,a,a,b],
                         [c,c,c,c,c,c,c],
                         [a,e,a,e,a,e,a],
                         [a,e,a,e,a,e,a],
                         [a,e,a,e,a,e,a],
                         [a,e,a,e,a,e,a],
                         [h,h,h,h,h,h,h]
                    ],
                    [
                         [c,c,c,c,c,c,c],
                         [d,d,d,d,d,d,d],
                         [c,b,b,b,b,b,c],
                         [c,b,b,b,b,b,c],
                         [c,b,b,b,b,b,c],
                         [c,c,c,c,c,c,c],
                         [c,b,b,b,b,b,c],
                         [c,b,b,b,b,b,c],
                         [c,b,b,b,b,b,c],
                         [c,c,c,c,c,c,c],
                         [c,b,b,b,b,b,c],
                         [c,b,b,b,b,b,c],
                         [c,b,b,b,b,b,c],
                         [c,c,c,c,c,c,c],
                         [c,b,b,b,b,b,c],
                         [c,b,b,b,b,b,c],
                         [c,b,b,b,b,b,c],
                         [c,c,c,c,c,c,c],
                         [c,b,b,b,b,b,c],
                         [c,b,b,b,b,b,c],
                         [c,b,b,b,b,b,c],
                         [c,c,c,c,c,c,c],
                         [c,b,b,b,b,b,c],
                         [c,b,b,b,b,b,c],
                         [c,b,b,b,b,b,c],
                         [c,c,c,c,c,c,c],
                         [e,a,e,a,e,a,e],
                         [e,a,e,a,e,a,e],
                         [e,a,e,a,e,a,e],
                         [e,a,e,a,e,a,e],
                         [h,h,h,h,h,h,h]
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

#the beautiful picture
def setPicture(x,y,z):
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

#trololo face
def trololo(tx,ty,tz):
    a=1
    c=(1,6)
    b=155
    f=0
    k=5
    bigArray = [
                  [
               [f,f,f,f,f,f,f,f,f,f,f,c,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
               [f,f,f,f,f,f,f,f,f,c,a,a,a,a,a,c,c,c,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,a,a],
               [f,f,f,f,f,f,f,c,a,a,c,b,b,b,b,b,b,b,c,c,c,c,b,b,b,b,b,b,c,c,c,b,b,b,b,b,a,a],
               [f,f,f,f,f,c,a,a,b,b,b,b,b,b,c,c,b,b,b,b,b,b,b,b,b,c,c,c,c,c,c,c,c,b,b,b,b,a,c],
               [f,f,f,f,f,c,a,b,b,b,b,c,c,b,b,b,c,b,b,b,b,b,c,c,b,b,b,b,b,b,c,c,c,c,b,b,b,c,a],
               [f,f,f,f,c,a,c,b,b,b,c,b,b,b,b,b,c,b,b,b,b,b,c,b,b,b,b,b,b,b,b,b,c,b,b,b,b,b,a,c],
               [f,f,f,f,c,a,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,c,a,a,a,a,c,b,b,b,b,b,b,b,b,c,a],
               [f,f,f,c,a,a,b,b,b,b,b,a,a,a,a,c,b,b,b,b,b,b,c,a,a,b,a,a,a,a,a,c,b,b,b,b,b,b,b,a,a],
               [f,f,c,a,a,b,c,b,c,b,a,a,a,a,a,a,a,b,c,b,b,b,a,b,b,c,a,a,a,a,a,a,c,c,c,b,b,b,b,c,a,a],
               [f,f,c,a,b,c,b,b,b,b,b,b,b,b,c,c,a,a,c,b,b,b,a,a,a,c,b,b,c,b,b,b,b,b,c,a,a,a,c,b,b,c,a],
               [f,c,a,c,b,b,c,a,a,c,b,b,b,b,b,b,c,c,b,b,b,b,b,c,b,b,b,b,a,a,b,b,c,a,a,c,b,b,a,a,b,b,c,a],
               [f,c,a,c,b,b,c,c,c,a,a,a,a,b,b,b,a,c,b,b,b,b,b,b,b,b,b,b,b,c,a,a,c,b,b,b,a,b,b,a,c,b,b,a],
               [f,c,a,c,b,b,b,b,c,b,c,c,b,b,b,a,a,b,b,b,b,b,c,a,c,b,b,b,b,b,b,b,b,b,a,a,a,c,b,b,a,b,b,a],
               [f,f,c,a,b,c,b,b,a,b,b,b,b,c,a,a,b,b,b,b,b,b,c,c,a,c,b,b,b,b,b,c,a,a,c,b,a,a,a,c,a,b,b,a],
               [f,f,c,a,c,b,b,a,a,b,b,b,c,c,a,a,b,b,b,b,a,a,a,b,a,b,b,b,c,a,a,a,c,b,b,b,a,b,b,a,b,b,b,a],
               [f,f,c,a,a,b,b,a,a,a,c,b,b,b,b,b,a,a,c,b,b,b,b,b,c,c,a,a,a,c,b,a,b,b,c,a,a,b,b,b,b,b,a],
               [f,f,f,c,a,b,b,a,a,c,a,a,a,c,b,b,b,a,b,b,b,c,a,a,a,a,c,b,b,b,b,a,a,a,a,a,b,b,b,b,b,a,a],
               [f,f,f,c,a,b,b,a,b,c,b,b,a,a,a,a,a,a,a,a,a,c,c,b,b,a,b,b,c,a,a,a,c,b,a,b,b,b,b,b,a,a],
               [f,f,f,c,a,c,b,a,a,a,b,b,c,b,b,b,a,b,b,b,c,b,b,b,b,a,a,a,a,a,c,a,b,a,a,b,b,b,b,a,a],
               [f,f,f,c,a,c,b,a,a,a,a,a,a,a,c,a,a,c,c,a,a,c,a,a,a,a,a,c,b,b,b,c,a,a,b,b,b,b,b,a],
               [f,f,f,c,a,c,b,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,c,b,a,b,b,b,b,a,a,b,b,b,b,b,a,a],
               [f,f,f,c,a,c,b,a,a,a,a,a,a,a,a,a,a,a,a,c,a,c,b,b,b,b,a,b,b,c,a,a,b,b,b,b,b,b,a],
               [f,f,f,c,a,b,b,c,a,a,b,a,b,a,b,b,a,b,b,b,c,c,b,b,b,b,c,a,a,a,b,b,b,b,b,b,c,a],
               [f,f,f,c,a,b,b,b,a,a,c,a,b,c,c,b,c,c,b,b,c,a,b,b,c,a,a,a,c,b,b,b,c,c,b,c,a],
               [f,f,f,c,a,b,b,b,b,b,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,c,b,b,b,c,c,c,c,c,a,a],
               [f,f,f,c,a,b,b,b,b,b,b,b,b,b,b,c,c,c,c,c,b,b,b,b,b,b,b,c,c,c,b,c,a,a],
               [f,f,f,c,a,b,c,b,b,c,c,b,b,b,b,b,b,b,b,b,b,b,b,c,c,c,c,b,b,c,a,a],
               [f,f,f,c,a,b,b,c,c,b,b,c,b,b,b,b,b,b,b,b,c,c,c,c,b,b,b,c,a,a],
               [f,f,f,c,a,b,b,b,c,c,c,c,b,b,b,b,b,b,b,b,b,b,b,b,b,c,a,a],
               [f,f,f,c,a,a,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,c,c,a,a,a],
               [f,f,f,f,c,a,a,b,b,b,b,b,b,b,b,b,b,c,a,a,a,a,a],
               [f,f,f,f,f,f,c,a,a,a,a,a,a,a,a,a,a,a],
           ]
    ]
                  
    for letter in bigArray:
       ty=pos.y
       tz=pos.z
       for level in letter:
           tz=pos.z
           for block in level:
               mc.setBlock(tx+30, ty, tz-25, block)
               tz+=1
           ty-=1

# the cannon
def setCannon(x,y,z):
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
