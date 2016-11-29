#!/usr/bin/python3
# alarm_test.py
# this is a basic alarm
# Author : Zachary Igielman

#import neccesary libraries (that tell python how to interact with time and the board)
import time, Alarm, sys, _thread

#set secret code to 1 2 3 4
KEY=[1, 2, 3, 4]

#create a global variable that stores whether the code has been enetered the key correctly
#this is used to communicate between threads
global correct
correct=0

#set up the connection to the board
Alarm.init()

global running_flag
running_flag = True

#this function checks if the code is entered correctly in a seperate thread (in the background)
def codeThread():
    global running_flag
    #repeat forever
    while running_flag:
        #grab the global variable
        global correct
        #read the keypad (wait for a code to be pressed)
        a=Alarm.getCode()
        #check of the code is correct
        if a==KEY:
            #change the global variable, informing the other thread (background task) that the code has been entered correctly
            correct=1
        else:
            print("Incorrect, try again")

#flash for thirty seconds giving the person a minute to leave the room
for n in range(30):
    Alarm.light(0.5)
    time.sleep(0.5)

#wait for motion
while not Alarm.getMotion():
    time.sleep(1)

#when there is motion, start the code thread that checks if the correct code is entered
_thread.start_new_thread(codeThread, ())

#beep until the code is entered correctly or one minute is up
n=0
while n<30 and not correct:
    Alarm.light(0.5)
    time.sleep(0.5)
    n=n+1

#sound the alarm until the code is entered correctly
while not correct:
    Alarm.sound(1)

#stop the script when the code is entered correctly
Alarm.cleanup()
running_flag=False
