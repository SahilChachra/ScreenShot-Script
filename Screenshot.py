# This program is expected to take screenshot after every given interval of time
# This program can be stopped by pressing a key combination
# This can be used to make a timelapse while you code something
# Also a basic version of it can be used to take screenshot of you code if you want!
# Applications are endles!

import os
import time
import keyboard
import pyautogui

#dir = input("Enter location to save the pictures : ")

while True:
    if keyboard.is_pressed("shift + space"): #The keycombination should be such that you don't press it by mistake!
        while True:
            #if keyboard.is_pressed("shift + q"):
            #    break
            ss = pyautogui.screenshot()
            currTime = time.asctime(time.localtime())
            currTime = currTime.replace(" ","-").replace(":","+")
            currTime = currTime + '.png'
            ss.save(currTime)
            time.sleep(5)
        break