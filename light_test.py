#!/usr/bin/python
# light_test.py
# blinks LED 5 times
# Author : Zachary Igielman

#import neccesary libraries (that tell python how to interact with time and the board)
import time, Alarm, sys

#set up the connection to the board
Alarm.init()

#repeat 5 times
for n in range(5):
    #turn the LED on for one second and off for one second
    Alarm.light(1)
    time.sleep(1)

#stop the script
Alarm.cleanup()
sys.exit(0)
