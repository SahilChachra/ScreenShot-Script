# This program is expected to take screenshot after every given interval of time
# This program can be stopped by pressing a key combination
# This can be used to make a timelapse while you code something
# Also a basic version of it can be used to take screenshot of you code if you want!
# Applications are endles!

import os
import time
import keyboard
import pyautogui

def setDestination():
    print("Enter destination for storing Screenshots in format C:/Users/XYZ/Downloads.. (Windows) ")
    while True:
        try: 
            dir = input("Destination : ")
            os.chdir(dir)
            return
        except:
            print("Enter valid Destination")


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
# 7. Checks given destination is valid or not

# - THE PYTHON SCRIPT SHOULD BE RUNNING IN BACKGROUND TO DO IT'S WORK PEACEFULLY!


# Creating settings (default/user defined)
def setKeyCombination():
    global keyToStartTimelapse, keyToEndTimelapse, keyToTakeSingleShot, keyToEndSingleShot
    print("Do you want to use Default key combinations or Set your own?")
    keyChoice = int(input("Enter 0 for DEFAULT and 1 for CUSTOM : "))
    while True:
        if(keyChoice == 0):
            keyToStartTimelapse =  "shift + space"
            keyToEndTimelapse = "shift + ctrl" #NOT IMPLEMENTED YET
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
    timelapseDelay = int(input("Enter delay between two Screenshot : "))
    while True:
        #timelapseDelay = 4
        if keyboard.is_pressed(keyToStartTimelapse): #The keycombination should be such that you don't press it by mistake!
            while True:
                #if keyboard.is_pressed("shift + q"):
                #break
                ss = pyautogui.screenshot()
                currTime = time.asctime(time.localtime()).replace(" ","-").replace(":","+")
                #Replacing ' : ' with ' + ' as ' : ' is invalid char in file name 
                dest = dir + currTime + '.png'
                ss.save(dest)
                dest = "" #Clearning dest variable
                time.sleep(timelapseDelay) #creating delay between two shots
            break
        #quit()

#For single shots
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

#Driving Function calls
while True:
    global dir
    setDestination()
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