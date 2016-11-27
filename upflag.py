from mcpi.minecraft import Minecraft
mc = Minecraft.create()
while True:
      name= input('Who will be the owner of the platform? ')
      try:
            ID=mc.getPlayerEntityId(name)
      except:
            print('There is no such player on server :(')
      else:
            break
password = input('Enter password: ')
if password == 'sosiskavteste':
      x,y,z=135,76,388

      #platform
      mc.setBlocks(x+2,y,z-2,x+8,y,z+2,5)
      #colone
      mc.setBlocks(x+8,y+1,z,x+8,y+12,z,101)


      def flagDown():
          #erasing upper flag
          mc.setBlocks(x+13,y+12,z,x+9,y+9,z,0)
          #build flag down

          mc.setBlocks(x+9,y+1,z,x+13,y+1,z,35,6)
          mc.setBlocks(x+9,y+2,z,x+13,y+2,z,35,14)
          mc.setBlocks(x+9,y+3,z,x+13,y+3,z,35,9)

      def flagUp():
          #erasing the flag below
          mc.setBlocks(x+9,y+1,z,x+13,y+3,z,0)
          #build flag up
          mc.setBlocks(x+9,y+10,z,x+13,y+10,z,35,6)
          mc.setBlocks(x+9,y+11,z,x+13,y+11,z,35,14)
          mc.setBlocks(x+9,y+12,z,x+13,y+12,z,35,9)


      while True:
          pos1=mc.entity.getTilePos(ID)
          x1,y1,z1=pos1.x,pos1.y,pos1.z
          if x1>=x+2 and x1<=x+8 and z1>=z-2 and z1<=z+2 and y1==y+1:
              flagUp()
          else:
              flagDown()
else:
      print('Wrong password')
