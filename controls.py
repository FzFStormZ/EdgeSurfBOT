import pyautogui
import time

def energy():
    # take a energy boost to avoid monster for example
    pyautogui.keyDown('down')
    pyautogui.keyUp('down')
    time.sleep(0.1)
    pyautogui.keyDown('down')
    pyautogui.keyUp('down')

def turnLeft():

    # turn left
    pyautogui.keyDown('left')
    pyautogui.keyUp('left')

def turnRight():

    # turn right
    pyautogui.keyDown('right')
    pyautogui.keyUp('right')

def reset():

    # go back to the initial position of the surfer
    pyautogui.keyDown('down')
    pyautogui.keyUp('down')

def standBy():

    # take a pause
    pyautogui.keyDown('up')
    pyautogui.keyUp('up')

def restartGame():

    # press spacebar to restart game 
    pyautogui.keyDown('space')
    time.sleep(0.5)
    pyautogui.keyUp('space')