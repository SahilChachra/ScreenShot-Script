import os
import time
import keyboard
import pyautogui


def setDestination():
    print("Enter destination for storing Screenshots in format C:/Users/XYZ/Downloads.. (Windows) ")
    while True:
        try: 
            desti = input("Destination : ")
            os.chdir(desti)
            return desti
        except:
            print("Enter valid Destination")

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

            print("To start timelapse, Press : Shift + space\n")
            print("To end timelapse, Press : Shift + ctrl\n")
            print("To start Single Shot, Press : Shift + alt\n")
            print("To end Single Shot, Press : Shift + `\n")
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
    print("WARNING --- TO EXIT TIMELAPSE PRESS CTRL + C IN TERMINAL. KEY COMBINATION TO QUIT IS BEING FIXED")
    timelapseDelay = int(input("Enter delay between two Screenshot : "))
    while True:
        #timelapseDelay = 4
        if keyboard.is_pressed(keyToStartTimelapse): #The keycombination should be such that you don't press it by mistake!
            while True:
                ss = pyautogui.screenshot()
                currTime = time.asctime(time.localtime()).replace(" ","-").replace(":","+")
                #Replacing ' : ' with ' + ' as ' : ' is invalid char in file name 
                dest = desti + currTime + '.png'
                ss.save(dest)
                dest = "" #Clearning dest variable
               #if keyboard.is_pressed(keyToEndTimelapse):
               #    quit()
                time.sleep(timelapseDelay) #creating delay between two shots
            break
        #quit()

#For single shots
def singleShots():
    while True:
        if keyboard.is_pressed(keyToTakeSingleShot): # To trigger single shots
            ss = pyautogui.screenshot()
            currTime = time.asctime(time.localtime()).replace(" ","-").replace(":","+")
            dest = desti + currTime + '.png'
            ss.save(dest)
            dest = ""
        elif keyboard.is_pressed(keyToEndSingleShot):
            break

#Driving Function calls
desti = setDestination()
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
        quit()
    elif(choice == 3):
        quit()
    else:
        print("Invalid Choice!\n")