#!/usr/bin/python3
# keypad_test.py
# waits for a key to be pressed and prints the numerical value
# Author : Zachary Igielman

#import neccesary libraries (that tell python how to interact with time and the board)
import time, Alarm, sys

#set up the connection to the board
Alarm.init()

#call the getCode() function from the library that waits for a key and returns its value
k=Alarm.getCode()
#print the value
print(k)

#stop the script
Alarm.cleanup()
sys.exit(0)
