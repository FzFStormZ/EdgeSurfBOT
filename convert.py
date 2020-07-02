from PIL import ImageGrab, ImageOps

from datas import boxs
from datas import colors as c

def imageGrab():  

    # grabbing all the avoid values in form of RGB tupples
    # box behind  
    image = ImageGrab.grab(boxs.box_behind)
    colors_behind = image.getcolors(image.size[0] * image.size[1])

    # left box
    image = ImageGrab.grab(boxs.box_left)
    colors_left = image.getcolors(image.size[0] * image.size[1])

    # right box
    image = ImageGrab.grab(boxs.box_right)
    colors_right = image.getcolors(image.size[0] * image.size[1])

    # front box
    image = ImageGrab.grab(boxs.box_front)
    colors_front = image.getcolors(image.size[0] * image.size[1])

    # snipe box
    image = ImageGrab.grab(boxs.box_snipe)
    colors_snipe = image.getcolors(image.size[0] * image.size[1])
    
    # energy box
    image = ImageGrab.grab(boxs.box_energy)
    colors_energy = image.getcolors(image.size[0] * image.size[1])

    return (colors_left, colors_right, colors_behind, colors_front, colors_snipe, colors_energy)

def numberToColor():

    # use RGB pixels to know the dominant color of each box
    red = 0
    green = 0
    black = 0
    sand = 0
    energyColor = 0

    left = ()
    right = ()
    behind = ()
    front = ()
    snipe = ()
    energy = ()

    colors = imageGrab()

    for i in range(6):
        for color in colors[i]:
            #print(color)
            if (color[1][0] == 255 and color[1][1] == 0 and color[1][2] == 0):
                red += color[0]
            elif (color[1][0] == 0 and color[1][1] == 255 and color[1][2] == 0):
                green += color[0]
            elif (color[1][0] == 0 and color[1][1] == 0 and color[1][2] == 0):
                black += color[0]
            elif (color[1][0] == 211 and color[1][1] == 230 and color[1][2] == 201):
                sand += color[0]
            elif (color[1][1] == 255):
                energyColor += color[0]

        if (i == 0):
            left = (red, green, black)
        elif (i == 1):
            right = (red, green, black)
        elif (i == 2):
            behind = black
        elif (i == 3):
            front = (red, green, black)
        elif (i == 4):
            snipe = (sand, black)
        elif (i == 5):
            energy = energyColor

        
        red = 0
        green = 0
        black = 0
        sand = 0
        energyColor = 0

    # print("RED:" + str(red) + " " + "GREEN:" + str(green) + " " + "BLACK:" + str(black) + " " + "SAND:" + str(sandcolor))

    return (left, right, behind, front, snipe, energy)