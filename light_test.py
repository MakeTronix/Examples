#!/usr/bin/python
# light_test.py
# blinks LED 5 times
# Author : Zachary Igielman

#import neccesary libraries (that tell python how to interact with time and RPiLarm)
import time, RPiLarm, sys

#set up the connection to RPiLarm
RPiLarm.init()

#repeat 5 times
for n in range(5):
    #turn the LED on for one second and off for one second
    RPiLarm.light(1)
    time.sleep(1)

#stop the script
RPiLarm.cleanup()
sys.exit(0)
