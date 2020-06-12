# This program is expected to take screenshot after every given interval of time
# This program can be stopped by pressing a key combination
# This can be used to make a timelapse while you code something
# Also a basic version of it can be used to take screenshot of you code if you want!
# Applications are endles!

import os
import time
import keyboard
import pyautogui

print("Enter destination for storing Screenshots in format C:/Users/XYZ/Downloads.. (Windows) ")
dir = input("Destination : ")

#++++++++++++++++++++
#----------TO ADD---------
# Fix - Exiting program
# Add - option to given user defined key combinations or else user pre defined key combinations
# Add - cutom time interval

#+++++++++++++++++++++++

#***********************
#-------------FEATURES------------

# 1. Can take screenshot at given interval of time
# 2. Can take Single Shots and save directly instead explicitly opening another app to save it
# 3. Can store data in user defined directory
# 4. Name of file is current Date-Time to easily sort data for editing purpose
# 5. 

# - THE PYTHON SCRIPT SHOULD BE RUNNING IN BACKGROUND TO DO IT'S WORK PEACEFULLY!

# FOR TIMELAPSE PURPOSE
def timelapse():
    while True:
        if keyboard.is_pressed("shift + space"): #The keycombination should be such that you don't press it by mistake!
            while True:
                #if keyboard.is_pressed("shift + q"):
                #break
                ss = pyautogui.screenshot()
                currTime = time.asctime(time.localtime().replace(" ","-").replace(":","+"))
                #Replacing ' : ' with ' + ' as ' : ' is invalid char in file name 
                dest = dir + currTime + '.png'
                ss.save(dest)
                dest = ""
                time.sleep(5)
            break
        quit()

# FOR TAKING SNAPSHOTS IF REQ
#The above part takes screenshot at given interval of Time
#Now, if you want to take ss of anything on your screen, you have to press PrintScreen button and then paste that image in MSPAINT in Windows!
# So to avoid this, we can make the usage more Dynamic

def singleShots():
    while True:
        if keyboard.is_pressed("shift + alt"): # To trigger single shots
            ss = pyautogui.screenshot()
            currTime = time.asctime(time.localtime()).replace(" ","-").replace(":","+")
            dest = dir + currTime + '.png'
            ss.save(dest)
            dest = ""
        elif keyboard.is_pressed("shift + `"):
            break

while True:
    print("1. Time Lapse\n2. Single Shots\n3. Exit\n")
    choice = int(input("Enter Choice : "))

    if(choice == 1):
        timelapse()
        #quit()
    elif(choice == 2):
        singleShots()
    elif(choice == 3):
        quit()
    else:
        print("Invalid Choice!\n")


