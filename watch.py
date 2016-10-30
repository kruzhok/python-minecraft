from mcpi.minecraft import Minecraft
import time
import math
mc = Minecraft.create()
angle = 90
angleM = 90
angleH = 90
centerX = -94
centerY = 103
centerZ = 91
radius = 10
while True:
    time.sleep(0.1)
    mc.setBlocks(centerX - radius,centerY - radius,centerZ,centerX + radius,centerY + radius,centerZ,0)
    a = 0
    while a<=360:
        mc.setBlock(int(centerX+radius*math.cos(math.radians(a))),int(centerY+radius*math.sin(math.radians(a))),centerZ,57)
        a = a + 2
    r = 0
    while r<radius:
        mc.setBlock(int(centerX+r*math.cos(math.radians(angle))),int(centerY+r*math.sin(math.radians(angle))),centerZ,35,14)
        r = r + 1
    angle = angle + 6
    rM = 0
    while rM<radius-5:
        mc.setBlock(int(centerX+rM*math.cos(math.radians(angleM))),int(centerY+rM*math.sin(math.radians(angleM))),centerZ,35,15)
        rM = rM + 1
    rH = 0
    while rH<radius-10:
        mc.setBlock(int(centerX+rH*math.cos(math.radians(angleH))),int(centerY+rH*math.sin(math.radians(angleH))),centerZ,35,5)
        rH = rH + 1
    if angle == 450:
        angle = 90
        angleM = angleM + 6
        if angleM == 450:
            angleM = 90
            angleH = angleH + 6
            if angleH == 450:
                angleH = 90
