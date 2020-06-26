from PIL import ImageGrab, ImageOps

from datas import boxs, colors

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

    return (colors_left, colors_right, colors_behind, colors_front)

def numberToColor():

    # use RGB pixels to know the dominant color of each box
    red = 0
    green = 0
    black = 0

    left = ()
    right = ()
    behind = ()
    front = ()

    colors = imageGrab()

    for i in range(4):
        for color in colors[i]:
            #print(color)
            if (color[1][0] == 255 and color[1][1] == 0 and color[1][2] == 0):
                red += color[0]
            elif (color[1][0] == 0 and color[1][1] == 255 and color[1][2] == 0):
                green += color[0]
            elif (color[1][0] == 0 and color[1][1] == 0 and color[1][2] == 0):
                black += color[0]

        if (i == 0):
            left = (red, green, black)
        elif (i == 1):
            right = (red, green, black)
        elif (i == 2):
            behind = black
        elif (i == 3):
            front = (red, green, black)
        
        red = 0
        green = 0
        black = 0

    #print("RED:" + str(red) + " " + "GREEN:" + str(green) + " " + "BLUE:" + str(blue) + " " + "BLACK:" + str(black))

    return (left, right, behind, front)