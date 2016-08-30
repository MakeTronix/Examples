#!/usr/bin/python
# sound_test.py
# beeps five times
# Author : Zachary Igielman

#import neccesary libraries (that tell python how to interact with time and RPiLarm)
import time, Alarm, sys

#set up the connection to RPiLarm
RPiLarm.init()

#repeat 5 times
for n in range(5):
    #turn the buzzer on for one second and off for one second
    RPiLarm.sound(1)
    time.sleep(1)

#stop the script
RPiLarm.cleanup()
sys.exit(0)
