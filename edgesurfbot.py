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
    # coordinates of the black box of the surfer
    black_box = (467, 462, 493, 488)

    # coordinates of the box around the surfer
    box_around_surfer = (243, 371, 718, 584)

    # coordinates of the box behind the surfer (to avoid monster or other surfers)
    box_behind = (431, 374, 535, 462)

    # coordinates of the left box of the surfer
    box_left = (264, 490, 435, 586)

    # coordinates of the right box of the surfer
    box_right = (426, 490, 700, 586)

    # coordinates of the box front of the surfer
    box_front = (441, 490, 516, 586)

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

def standBy():
    pyautogui.keyDown('up')
    pyautogui.keyUp('up')

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

    # front box
    image = ImageGrab.grab(boxs.box_front)
    colors_front = image.getcolors(image.size[0] * image.size[1])

    return (colors_left, colors_right, colors_behind, colors_front)

def numberToColor():
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


def decisions():
    datas = numberToColor()

    print(datas)

    if (datas[2] >= 200):
        reset()

    if (datas[2] >= 700): # [behind][black]
        energy()

    if (datas[3][2] >= 200): # [front][black]
        standBy()
        turnLeft()
        turnLeft()
        turnLeft()
    
    if (datas[0][2] >= 200 and datas[1][2] >= 200 and datas[3][2] >= 200): # [left][black] and [right][black] and [front][black]
        turnLeft()
        turnLeft()
        turnLeft()

    if (datas[0][2] >= 200): # [left][black]
        if (datas[0][2] >= 200 and datas[3][2] >= 200): # [left][black] and [front][black]
            turnRight()
            turnRight()
            turnRight()
            turnRight()
        elif (datas[0][2] >= 200 and datas[1][2] >= 200): # [left][black] and [right][black]
            reset()
        else:
            turnRight()
        
    if (datas[1][2] >= 200): # [right][black]
        if (datas[1][2] >= 200 and datas[3][2] >= 200): # [right][black] and [front][black]
            turnLeft()
            turnLeft()
            turnLeft()
            turnLeft()
        elif (datas[1][2] >= 200 and datas[0][2] >= 200): # [right][black] and [left][black]
            reset()
        else:
            turnLeft()

    if (datas[0][1] >= 200 and datas[1][1] >= 200): # [left][green] and # [right][green]
        turnLeft()
        turnLeft()
        turnLeft()

    if (datas[0][1] >= 200): # [left][green]
        turnLeft()

    if (datas[1][1] >= 200): # [right][green]
        turnRight()

    if (datas[0][2] >= 200 and datas[1][2] >= 200 and datas[3][1] >= 300): # [left][black] and # [right][black] and # [front][green]
        reset()
        reset()
        reset()

    if (datas[0][2] >= 200 and datas[0][1] >= 300): # [left][black] and # [left][green]
        turnLeft()
        turnLeft()
        reset()
    
    if (datas[1][2] >= 200 and datas[1][1] >= 300): # [right][black] and # [right][green]
        turnRight()
        turnRight()
        reset()
    
    if (datas[0][2] >= 200 and datas[3][1] >= 200): # [left][black] and # [front][green]
        turnRight()
        turnRight()
        reset()
        reset()
    
    if (datas[1][2] >= 200 and datas[3][1] >= 200): # [right][black] and # [front][green]
        turnLeft()
        turnLeft()
        reset()
        reset()
        

time.sleep(2)
restartGame()
while True:
    decisions()