from mcpi.minecraft import Minecraft    
def Image(ImageName,X0,Y0,Z0,basewidth,horisontal):
    from PIL import Image
    import math
    mc = Minecraft.create()
    white = [221,221,221,0]#rgb, id
    orange = [219,125,62,1]#rgb, id
    magneta = [179,80,188,2]#rgb, id
    lightBlue = [107,138,201,3]#rgb, id
    yellow = [177,166,39,4]#rgb, id
    lime = [65,174,56,5]#rgb, id
    pink = [208,132,153,6]#rgb, id
    gray = [64,64,64,7]#rgb, id
    lightGray = [154,161,161,8]#rgb, id
    cyan = [46,110,137,9]#rgb, id
    purple = [126,61,181,10]#rgb, id
    blue = [46,56,141,11]#rgb, id
    brown = [79,50,31,12]#rgb, id
    green = [53,70,27,13]#rgb, id
    red = [150,52,48,14]#rgb, id
    black = [25,22,22,15]#rgb, id
    colors = [white,orange,magneta,lightBlue,yellow,lime,pink,gray,lightGray,cyan,purple,blue,brown,green,red,black]
    img = Image.open(ImageName)
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((basewidth,hsize), Image.ANTIALIAS)
    #place
    if img.width*img.height > 750*750:
        mc.postToChat("wanted Image is too big!")
    else:
        data = img.load()
        x = 0
        while x < img.width:
            y = 0
            while y < img.height:
                res = 255*3
                pixel = data[x,y]
                for color in colors:
                    r = pixel[0]-color[0]
                    g = pixel[1]-color[1]
                    b = pixel[2]-color[2]
                    if math.fabs(r)+math.fabs(g)+math.fabs(b) < res:
                        res = math.fabs(r)+math.fabs(g)+math.fabs(b)
                        block = 35,color[3]
                if horisontal:
                    mc.setBlock(X0+x,Y0,Z0+y,block)
                else:
                    mc.setBlock(X0+x,Y0-y,Z0,block)
                y = y + 1
            mc.postToChat(str(int(x / img.width * 100))+"%")
            x = x + 1
        mc.postToChat("done.")

password = input("enter password: ")
if password == "codestuding":
    ImageName = input("enter image name: ")
    horisontalAnswer = input("for horizontal image type 'true', for vertical image type any other: ")
    if horisontalAnswer == "true":
        horisontal = True
    else:
        horisontal = False
    print("enter coordinates for left top edge")
    X0 = int(input("X coordinate: "))
    Y0 = int(input("Y coordinate: "))
    Z0 = int(input("Z coordinate: "))
    basewidth = int(input("enter wanted image width (height will be calculated automaticly): "))
    Image(ImageName,X0,Y0,Z0,basewidth,horisontal)
else:
    print("permission denied!")
