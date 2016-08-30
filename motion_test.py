#!/usr/bin/python
# motion_test.py
# waits for 10 seconds and then waits until motion, when motion detected, prints 'alarm'
# Author : Zachary Igielman

#import neccesary libraries (that tell python how to interact with time and RPiLarm)
import time, Alarm, sys

#set up the connection to RPiLarm
RPiLarm.init()

#wait for 10 seconds
time.sleep(10)

#wait for motion
while not RPiLarm.getMotion():
    #check for motion every second
    time.sleep(1)
#inform the user that motion has been detected
print 'alarm'

#stop the script
RPiLarm.cleanup()
sys.exit(0)
