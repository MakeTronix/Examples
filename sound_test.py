#!/usr/bin/python3
# sound_test.py
# beeps five times
# Author : Zachary Igielman

#import neccesary libraries (that tell python how to interact with time and the board)
import time, Alarm

#set up the connection to the board
Alarm.init()

#repeat 5 times
for n in range(5):
    #turn the buzzer on for one second and off for one second
    Alarm.sound(1)
    time.sleep(1)

#stop the script
Alarm.cleanup()
