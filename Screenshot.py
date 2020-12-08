import os
import time
import keyboard
import pyautogui


def setDestination():
    print("Enter destination for storing Screenshots in format C:/Users/XYZ/Downloads.. (Windows)"
          "(Create folder before hand) ")
    while True:
        try:
            desti = input("Destination : ")
            os.chdir(desti)
            return desti
        except:
            print("Enter valid Destination")


# Creating settings (default/user defined)
def setKeyCombinationTimeLapse():
    global keyToStartTimelapse, keyToEndTimelapse
    print("Do you want to use Default key combinations or Set your own?")
    keyChoice = int(input("Enter 0 for DEFAULT and 1 for CUSTOM : "))
    while True:
        if keyChoice == 0:
            keyToStartTimelapse = "shift + space"
            keyToEndTimelapse = "shift + ctrl"  # NOT IMPLEMENTED YET

            print("To start timelapse, Press : Shift + space\n")
            print("To end timelapse, Press : Shift + ctrl\n")
            break
        elif keyChoice == 1:
            keyToStartTimelapse = input("Enter key combination to START Timelapse Shots : ")
            keyToEndTimelapse = input("Enter key combination to END Timelapse Shots (YET TO BE IMPLEMENTED): ")
            break
        else:
            print("Enter valid choice!")


def setKeyCombinationSingleShots():
    global keyToTakeSingleShot
    print("Do you want to use Default key combinations or Set your own?")
    keyChoice = int(input("Enter 0 for DEFAULT and 1 for CUSTOM : "))
    while True:
        if keyChoice == 0:
            keyToTakeSingleShot = "shift + alt"

            print("To Take Single Shot, Press : Shift + alt\n")
            break

        elif keyChoice == 1:

            keyToTakeSingleShot = input("Enter key combination to Take Single Shots : ")
            break

        else:
            print("Enter valid choice!")


# FOR TIMELAPSE PURPOSE
def timelapse():
    print("WARNING --- TO EXIT TIMELAPSE PRESS CTRL + C IN TERMINAL. KEY COMBINATION TO QUIT IS BEING FIXED")
    timelapseDelay = int(input("Enter delay between two Screenshot : "))
    while True:
        # timelapseDelay = 4
        if keyboard.is_pressed(
                keyToStartTimelapse):  # The key combination should be such that you don't press it by mistake!
            while True:
                ss = pyautogui.screenshot()
                currTime = time.asctime(time.localtime()).replace(" ", "-").replace(":", "+")
                # Replacing ' : ' with ' + ' as ' : ' is invalid char in file name
                dest = desti + currTime + '.png'
                ss.save(dest)

                # if keyboard.is_pressed(keyToEndTimelapse):
                #    quit()
                time.sleep(timelapseDelay)  # creating delay between two shots
        break
        # quit()


# For single shots
def singleShots():
    global keyToTakeSingleShot
    while True:
        if keyboard.is_pressed(keyToTakeSingleShot):  # To trigger single shots
            ss = pyautogui.screenshot()
            currTime = time.asctime(time.localtime()).replace(" ", "-").replace(":", "+")
            dest = desti + currTime + '.png'
            ss.save(dest)
        #elif keyboard.is_pressed(keyToEndSingleShot):
          #  break


if __name__ == '__main__':
    # Driving Function calls
    desti = setDestination()
    while True:

        print("1. Time Lapse\n2. Single Shots\n3. Exit\n")
        choice = int(input("Enter Choice : "))

        if choice == 1:
            setKeyCombinationTimeLapse()
            timelapse()
            # quit()
        elif choice == 2:
            setKeyCombinationSingleShots()
            singleShots()
            quit()
        elif choice == 3:
            quit()
        else:
            print("Invalid Choice!\n")
