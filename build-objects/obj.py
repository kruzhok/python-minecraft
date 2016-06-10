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