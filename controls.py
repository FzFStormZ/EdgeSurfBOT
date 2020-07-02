import pyautogui
import time

from datas import timeToEnergy, lastControl

timeStart = time.time()

def energy():

    # take a energy boost to avoid monster for example
    if (time.time() - timeStart > timeToEnergy):
        print("TURBO !!")
        pyautogui.keyDown('down')
        pyautogui.keyUp('down')
        pyautogui.keyDown('down')
        pyautogui.keyUp('down')

        lastControl = 'down'

def turnLeft():

    # turn left
    pyautogui.keyDown('left')
    pyautogui.keyUp('left')

    lastControl = 'left'

def turnRight():

    # turn right
    pyautogui.keyDown('right')
    pyautogui.keyUp('right')

    lastControl = 'right'

def reset():

    # go back to the initial position of the surfer
    pyautogui.keyDown('down')
    pyautogui.keyUp('down')

    lastControl = 'down'

def standBy():

    # take a pause
    pyautogui.keyDown('up')
    pyautogui.keyUp('up')

    lastControl = 'up'

def restartGame():

    # press spacebar to restart game 
    pyautogui.keyDown('space')
    time.sleep(0.5)
    pyautogui.keyUp('space')

def control():

    # use the last control
    pyautogui.keyDown(lastControl)
    pyautogui.keyUp(lastControl)