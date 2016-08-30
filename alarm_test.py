#!/usr/bin/python
# alarm_test.py
# this is a basic alarm
# Author : Zachary Igielman

#import neccesary libraries (that tell python how to interact with time and RPiLarm)
import time, RPiLarm, sys, thread

#set secret code to 1 2 3 4
KEY=[1, 2, 3, 4]

#create a global variable that stores whether the code has been enetered the key correctly
#this is used to communicate between threads
global correct
correct=0

#set up the connection to RPiLarm
RPiLarm.init()

#this function checks if the code is entered correctly in a seperate thread (in the background)
def codeThread():
    #repeat forever
    while True:
        #grab the global variable
        global correct
        #read the keypad (wait for a code to be pressed)
        a=RPiLarm.getCode()
        #check of the code is correct
        if a==KEY:
            #change the global variable, informing the other thread (background task) that the code has been entered correctly
            correct=1

#beep for thirty seconds giving the person a minute to leave the room
for n in range(30):
    RPiLarm.sound(1)
    time.sleep(1)

#wait for motion
while not RPiLarm.getMotion():
    time.sleep(1)

#when there is motion, start the code thread that checks if the correct code is entered
thread.start_new_thread(codeThread, ())

#beep until the code is entered correctly or one minute is up
n=0
while n<30 and not correct:
    RPiLarm.sound(1)
    time.sleep(1)
    n=n+1

#sound the alarm until the code is entered correctly
while not correct:
    RPiLarm.sound(1)

#stop the script when the code is entered correctly
RPiLarm.cleanup()
sys.exit(0)