#!/usr/bin/python3
# motion_test.py
# waits for 10 seconds and then waits until motion, when motion detected, prints 'alarm'
# Author : Zachary Igielman

#import neccesary libraries (that tell python how to interact with time and the board)
import time, Alarm, sys

#set up the connection to the board
Alarm.init()

#wait for 5 seconds
time.sleep(5)

#wait for motion
while Alarm.getMotion()==0:
    #check for motion every second
    time.sleep(1)
#inform the user that motion has been detected
print("alarm")

#stop the script
Alarm.cleanup()
sys.exit(0)
