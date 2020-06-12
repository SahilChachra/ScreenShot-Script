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

#+++++++++++++++++++++++

#***********************
#-------------FEATURES------------

# 1. Can take screenshot at given interval of time
# 2. Can take Single Shots and save directly instead explicitly opening another app to save it
# 3. Can store data in user defined directory
# 4. Name of file is current Date-Time to easily sort data for editing purpose
# 5. User has the option to either use their own settings or default settings
# 6. User can set custom time interval for taking timelapse

# - THE PYTHON SCRIPT SHOULD BE RUNNING IN BACKGROUND TO DO IT'S WORK PEACEFULLY!

# Creating settings (default/user defined)

def setKeyCombination():
    global keyToStartTimelapse, keyToEndTimelapse, keyToTakeSingleShot, keyToEndSingleShot
    print("Do you want to use Default key combinations or Set your own?")
    keyChoice = int(input("Enter 0 for DEFAULT and 1 for CUSTOM : "))
    while True:
        if(keyChoice == 0):
            keyToStartTimelapse =  "shift + space"
            keyToEndTimelapse = "" #NOT IMPLEMENTED YET
            keyToTakeSingleShot = "shift + alt"
            keyToEndSingleShot = "shift + `"
            break
        elif(keyChoice == 1):
            keyToStartTimelapse = input("Enter key combination to START Timelapse Shots : ")
            keyToEndTimelapse = input("Enter key combination to END Timelapse Shots (YET TO BE IMPLEMENTED): ")
            keyToTakeSingleShot = input("Enter key combination to START Single Shots : ")
            keyToEndSingleShot = input("Enter key combination to END Single Shots : ")
            break
        else:
            print("Enter valid choice!")


# FOR TIMELAPSE PURPOSE
def timelapse():
    while True:
        timelapseDelay = int(input("Enter delay between two Screenshot : "))
        if keyboard.is_pressed(keyToStartTimelapse): #The keycombination should be such that you don't press it by mistake!
            while True:
                #if keyboard.is_pressed("shift + q"):
                #break
                ss = pyautogui.screenshot()
                currTime = time.asctime(time.localtime().replace(" ","-").replace(":","+"))
                #Replacing ' : ' with ' + ' as ' : ' is invalid char in file name 
                dest = dir + currTime + '.png'
                ss.save(dest)
                dest = ""
                time.sleep(timelapseDelay)
            break
        quit()

# FOR TAKING SNAPSHOTS IF REQ
#The above part takes screenshot at given interval of Time
#Now, if you want to take ss of anything on your screen, you have to press PrintScreen button and then paste that image in MSPAINT in Windows!
# So to avoid this, we can make the usage more Dynamic

def singleShots():
    while True:
        if keyboard.is_pressed(keyToTakeSingleShot): # To trigger single shots
            ss = pyautogui.screenshot()
            currTime = time.asctime(time.localtime()).replace(" ","-").replace(":","+")
            dest = dir + currTime + '.png'
            ss.save(dest)
            dest = ""
        elif keyboard.is_pressed(keyToEndSingleShot):
            break

while True:
    
    print("1. Time Lapse\n2. Single Shots\n3. Exit\n")
    choice = int(input("Enter Choice : "))

    if(choice == 1):
        setKeyCombination()
        timelapse()
        #quit()
    elif(choice == 2):
        setKeyCombination()
        singleShots()
    elif(choice == 3):
        quit()
    else:
        print("Invalid Choice!\n")



