from PIL import ImageGrab, ImageOps
import pyautogui 
import time 
import numpy as np   



class colors():
    red = (255, 0, 0)
    green = (0, 255, 0)
    black = (0, 0, 0)
    blue = (0, 0, 255)

class boxs():
    # coordinates of black box of surfer
    black_box = (467, 462, 493, 488)

    # coordinates of box around surfer
    box_around_surfer = (243, 371, 718, 584)

    # coordinates of box behind surfer (to avoid monster or other surfers)
    box_behind = (389, 374, 574, 462)

    # coordinates of left box of the surfer
    box_left = (244, 489, 467, 586)

    # coordinates ofright box of the surfer
    box_right = (495, 489, 718, 586)

def restartGame(): 
    # press spacebar to restart game 
    pyautogui.keyDown('space')
    time.sleep(0.5)
    pyautogui.keyUp('space')

def energy():
    pyautogui.keyDown('down')
    pyautogui.keyUp('down')
    time.sleep(0.1)
    pyautogui.keyDown('down')
    pyautogui.keyUp('down')

def turnLeft():
    pyautogui.keyDown('left')
    pyautogui.keyUp('left')

def turnRight():
    pyautogui.keyDown('right')
    pyautogui.keyUp('right')

def reset():
    pyautogui.keyDown('down')
    pyautogui.keyUp('down')

def imageGrab():  
    # grabbing all the pixels values in form of RGB tupples
    # box behind  
    image = ImageGrab.grab(boxs.box_behind)
    colors_behind = image.getcolors(image.size[0] * image.size[1])

    # left box
    image = ImageGrab.grab(boxs.box_left)
    colors_left = image.getcolors(image.size[0] * image.size[1])

    # right box
    image = ImageGrab.grab(boxs.box_right)
    colors_right = image.getcolors(image.size[0] * image.size[1])

    return (colors_left, colors_right, colors_behind)

def numberToColor():
    red = 0
    green = 0
    black = 0

    left = ()
    right = ()
    behind = ()

    colors = imageGrab()

    for i in range(3):
        for color in colors[i]:
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
        else:
            behind = (red, green, black)
        
        red = 0
        green = 0
        black = 0


    #print("RED:" + str(red) + " " + "GREEN:" + str(green) + " " + "BLUE:" + str(blue) + " " + "BLACK:" + str(black))

    return (left, right, behind)


def decisions():
    datas = numberToColor()

    print(datas)

    if (datas[2][2] >= 700 and datas[2][2] <= 800): # [behind][black]
        energy()

    if (datas[0][2] >= 200): # [left][black]
        turnRight()

    if (datas[1][2] >= 200): # [right][black]
        turnLeft()
    

time.sleep(2)
restartGame()
while True:
    decisions()
    time.sleep(0.1)