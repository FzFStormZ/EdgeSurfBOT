import pyautogui
import time
import numpy as np

from controls import restartGame, reset, energy, turnLeft, turnRight, standBy, control, lastControl
from datas import boxs, avoid, earn, timeToAvoidMonster
from convert import imageGrab, numberToColor



def decisions():
    avoidMonster = 300
    datas = numberToColor()

    print(datas)


    ### BEHIND TO AVOID MONSTER
    if (datas[2] < 250 and datas[2] >= avoidMonster): # 320 > [behind][black] >= (300 or 50)
        reset()
        time.sleep(0.2) # to avoid to reset() a lot of times and run "speed bonus"

        if(time.time() - timeStart >= timeToAvoidMonster):
            avoidMonster = 50

    if (datas[2] >= 250): # [behind][black]
        if (datas[5] > 0):
            energy()
            time.sleep(2)


    ### FRONT
    if (datas[3][2] >= 100): # [front][black]
        if (datas[0][2] > datas[1][2]): # [left][black] > [right][black]
            while(datas[3][2] >= 50): # [front][black] != 50
                turnRight()
                turnRight()
                turnRight()

                datas = numberToColor() # recalcul
        elif (datas[0][2] < datas[1][2]): # [left][black] < [right][black]
            while(datas[3][2] >= 50): # [front][black] != 50
                turnLeft()
                turnLeft()
                turnLeft()

                datas = numberToColor() # recalcul
        elif (datas[0][2] == datas[1][2]): # [left][black] == [right][black]
            if (lastControl != "down"):
                while(datas[3][2] >= 50): # [front][black] != 50
                    pyautogui.keyDown(lastControl)
                    pyautogui.keyUp(lastControl)
                    pyautogui.keyDown(lastControl)
                    pyautogui.keyUp(lastControl)

                    datas = numberToColor() # recalcul
            else:
                while (datas[0][2] != datas[1][2]):
                    turnLeft()
                    turnLeft()
                

    ### LEFT AND RIGHT BLACK
    if (datas[0][2] >= avoid): # [left][black]
        if (datas[0][2] >= avoid and datas[3][2] >= 200): # [left][black] and [front][black]
            turnRight()
            turnRight()
            turnRight()
            turnRight()
        elif (datas[0][2] >= avoid and datas[1][2] >= 200): # [left][black] and [right][black]
            reset()
            time.sleep(0.2) # to avoid to reset() a lot of times and run "speed bonus"
        else:
            turnRight()
        
    if (datas[1][2] >= avoid): # [right][black]
        if (datas[1][2] >= avoid and datas[3][2] >= 200): # [right][black] and [front][black]
            turnLeft()
            turnLeft()
            turnLeft()
            turnLeft()
        elif (datas[1][2] >= avoid and datas[0][2] >= 200): # [right][black] and [left][black]
            reset()
            time.sleep(0.2) # to avoid to reset() a lot of times and run "speed bonus"
        else:
            turnLeft()
            turnLeft()


    ### GREEN 
    if (datas[0][1] >= avoid and datas[1][1] >= avoid): # [left][green] and # [right][green]
        turnLeft()
        turnLeft()
        turnLeft()

    if (datas[0][1] >= avoid): # [left][green]
        turnLeft()

    if (datas[1][1] >= avoid): # [right][green]
        turnRight()
    
    if (datas[3][1] >= avoid): # [front][green]
        reset()

    if (datas[0][2] >= avoid and datas[1][2] >= avoid and datas[3][1] >= earn): # [left][black] and # [right][black] and # [front][green]
        reset()
        time.sleep(0.2) # to avoid to reset() a lot of times and run "speed bonus"


    ### COMBO BLACK AND GREEN
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
    
    if (datas[1][2] >= avoid and datas[3][1] >= earn): # [right][black] and # [front][green]
        turnLeft()
        turnLeft()
        reset()


    ### SNIPE BLACK AND SAND:
        ## SAND
    if (datas[4][0] >= 50): # [snipe][sand]
        if (datas[0][2] > datas[1][2]): # [left][black] > [right][black]
            while(datas[4][0] >= 50): # [snipe][sand] != 50
                turnRight()
                turnRight()

                datas = numberToColor() # recalcul
        elif (datas[0][2] < datas[1][2]): # [left][black] < [right][black]
            while(datas[4][0] >= 50): # [snipe][sand] != 50
                turnLeft()
                turnLeft()

                datas = numberToColor() # recalcul
        elif (datas[0][2] == datas[1][2]): # [left][black] == [right][black]
            if (lastControl != "down"):
                while(datas[4][0] >= 50): # [snipe][sand] != 50
                    pyautogui.keyDown(lastControl)
                    pyautogui.keyUp(lastControl)
                    pyautogui.keyDown(lastControl)
                    pyautogui.keyUp(lastControl)

                    datas = numberToColor() # recalcul
            else:
                while (datas[0][2] != datas[1][2]):
                    turnLeft()
                    turnLeft()

    if (datas[4][0] >= 50 and datas[3][2] >= avoid): # [snipe][sand] and [front][black]
        if (datas[0][2] >= avoid): # [left][black]
            turnRight()
            turnRight()
            time.sleep(0.2)
        elif (datas[1][2] >= avoid): # [right][black]
            turnLeft()
            turnLeft()
            time.sleep(0.2)

        ## BLACK
    if (datas[4][1] >= 50): # [snipe][black]
        if (datas[0][2] > datas[1][2]): # [left][black] > [right][black]
            while(datas[4][1] >= 50): # [snipe][black] != 50
                turnRight()
                turnRight()

                datas = numberToColor() # recalcul
        elif (datas[0][2] < datas[1][2]): # [left][black] < [right][black]
            while(datas[4][1] >= 50): # [snipe][black] != 50
                turnLeft()
                turnLeft()

                datas = numberToColor() # recalcul
        elif (datas[0][2] == datas[1][2]): # [left][black] == [right][black]
            if (lastControl != "down"):
                while(datas[4][1] >= 50): # [snipe][black] != 50
                    pyautogui.keyDown(lastControl)
                    pyautogui.keyUp(lastControl)
                    pyautogui.keyDown(lastControl)
                    pyautogui.keyUp(lastControl)

                    datas = numberToColor() # recalcul
            else:
                while (datas[0][2] != datas[1][2]):
                    turnLeft()
                    turnLeft()

    if (datas[4][1] >= avoid and datas[3][2] >= 100): # [snipe][black] and [front][black]
        if (datas[0][2] >= avoid): # [left][black]
            turnRight()
            turnRight()
            time.sleep(0.2)
        elif (datas[1][2] >= avoid): # [right][black]
            turnLeft()
            turnLeft()
            time.sleep(0.2)
    
        
time.sleep(2)
restartGame()
timeStart = time.time()

while True:
    decisions()