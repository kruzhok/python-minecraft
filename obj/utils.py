# utils for building minecraft objects in multiplayer mode

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
import random

def coordsFromName(playerName):
    mc = Minecraft.create()
    pos = mc.getPlayerEntityId(playerName)
    x, y, z = pos.x, pos.y, pos.z
    position = {
        'x': x,
        'y': y,
        'z': z
    }
    return position
