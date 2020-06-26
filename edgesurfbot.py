import pyautogui
import time
import numpy as np

from controls import *
from datas import boxs, avoid, earn
from convert import imageGrab, numberToColor


def decisions():
    datas = numberToColor()

    print(datas)

    if (datas[2] >= avoid):
        reset()

    if (datas[2] >= 700): # [behind][black]
        energy()

    if (datas[3][2] >= avoid): # [front][black]
        standBy()
        turnLeft()
        turnLeft()
        turnLeft()
    
    if (datas[0][2] >= avoid and datas[1][2] >= avoid and datas[3][2] >= avoid): # [left][black] and [right][black] and [front][black]
        turnLeft()
        turnLeft()
        turnLeft()

    if (datas[0][2] >= avoid): # [left][black]
        if (datas[0][2] >= avoid and datas[3][2] >= avoid): # [left][black] and [front][black]
            turnRight()
            turnRight()
            turnRight()
            turnRight()
        elif (datas[0][2] >= avoid and datas[1][2] >= avoid): # [left][black] and [right][black]
            reset()
        else:
            turnRight()
        
    if (datas[1][2] >= avoid): # [right][black]
        if (datas[1][2] >= avoid and datas[3][2] >= avoid): # [right][black] and [front][black]
            turnLeft()
            turnLeft()
            turnLeft()
            turnLeft()
        elif (datas[1][2] >= avoid and datas[0][2] >= avoid): # [right][black] and [left][black]
            reset()
        else:
            turnLeft()

    if (datas[0][1] >= avoid and datas[1][1] >= avoid): # [left][green] and # [right][green]
        turnLeft()
        turnLeft()
        turnLeft()

    if (datas[0][1] >= avoid): # [left][green]
        turnLeft()

    if (datas[1][1] >= avoid): # [right][green]
        turnRight()

    if (datas[0][2] >= avoid and datas[1][2] >= avoid and datas[3][1] >= earn): # [left][black] and # [right][black] and # [front][green]
        reset()
        reset()
        reset()

    if (datas[0][2] >= avoid and datas[0][1] >= earn): # [left][black] and # [left][green]
        turnLeft()
        turnLeft()
        reset()
    
    if (datas[1][2] >= avoid and datas[1][1] >= earn): # [right][black] and # [right][green]
        turnRight()
        turnRight()
        reset()
    
    if (datas[0][2] >= avoid and datas[3][1] >= earn): # [left][black] and # [front][green]
        turnRight()
        turnRight()
        reset()
        reset()
    
    if (datas[1][2] >= avoid and datas[3][1] >= earn): # [right][black] and # [front][green]
        turnLeft()
        turnLeft()
        reset()
        reset()
        

time.sleep(2)
restartGame()
while True:
    decisions()