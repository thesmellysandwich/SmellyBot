import pyautogui, time
from stringcolor import *
import sys

time.sleep(5)
print()
print(cs('Welcome to SmellyBot, your shitty solution to being a lazy fuck JUST LIKE SMELLY!', "red"))

second_point = input(cs('Would you like to add a second firing point?\nA second point will fire a round in to each point repeating y/n: ', 'yellow'))
print()
print(cs('When the timer hits 0, make sure your mouse is on the desired location to shoot.', 'yellow'))
print()
timer = "10 9 8 7 6 5 4 3 2 1"
for char in timer:
    time.sleep(.4)
    sys.stdout.write(char)
    sys.stdout.flush()

position = pyautogui.position()
time.sleep(1)
print()


if second_point == 'y':
    print('Second point will be ready in 10 seconds.')
    print()
    
    timer = "10 9 8 7 6 5 4 3 2 1"
    for char in timer:
        time.sleep(.4)
        sys.stdout.write(char)
        sys.stdout.flush()

position2 = pyautogui.position()

print()
print(cs('The program will run in 10 seconds. you can press control + c in terminal to close it.', 'yellow'))
print()
print(cs('Enjoy you lazy asshole!', 'yellow'))
time.sleep(10)
print(cs('Program is running', 'red'))

# bazooka position for bottom of desert... fire!!!!
while True:
    # Fire RPG
    if second_point == 'n':
        pyautogui.moveTo(position)
        pyautogui.mouseDown()
        time.sleep(10)
        pyautogui.mouseUp()
        time.sleep(0.5)
    else:
        for i in range(7):
            pyautogui.moveTo(position)
            time.sleep(0.3)
            pyautogui.mouseDown()
            time.sleep(0.3)
            pyautogui.mouseUp()
            time.sleep(0.3)
            pyautogui.moveTo(position2)
            time.sleep(0.3)
            pyautogui.mouseDown()
            time.sleep(0.3)
            pyautogui.mouseUp()
            time.sleep(0.3)

    # Reload
    pyautogui.moveTo(754, 77)
    time.sleep(0.5)
    pyautogui.mouseDown()
    time.sleep(0.5)
    pyautogui.mouseUp()
    time.sleep(0.5)
    pyautogui.mouseDown()
    time.sleep(0.5)
    pyautogui.mouseDown()

    time.sleep(0.5)
    pyautogui.moveTo(845, 421)
    time.sleep(0.5)
    pyautogui.mouseDown()
    time.sleep(0.5)
    pyautogui.mouseUp()
    time.sleep(0.5)
    pyautogui.mouseDown()
    time.sleep(0.5)
    pyautogui.mouseDown()
    pyautogui.mouseUp()

    pyautogui.moveTo(1006, 428)
    time.sleep(0.5)
    pyautogui.mouseDown()
    time.sleep(0.5)
    pyautogui.mouseUp()
    time.sleep(0.5)
    pyautogui.mouseDown()
    time.sleep(0.5)
    pyautogui.mouseDown()
    pyautogui.mouseUp()

    pyautogui.moveTo(1230, 296)
    pyautogui.mouseDown()
    pyautogui.mouseUp()
    pyautogui.mouseDown()
    pyautogui.mouseUp()
    pyautogui.mouseDown()
    pyautogui.mouseUp()
    pyautogui.mouseDown()
    pyautogui.mouseUp()
    pyautogui.mouseDown()
    pyautogui.mouseUp()

    