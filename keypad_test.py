#!/usr/bin/python
# keypad_test.py
# waits for a key to be pressed and prints the numerical value
# Author : Zachary Igielman

#import neccesary libraries (that tell python how to interact with time and RPiLarm)
import time, Alarm, sys

#set up the connection to RPiLarm
RPiLarm.init()

#call the getCode() function from the library that waits for a key and returns its value
k=RPiLarm.getCode()
#print the value
print k

#stop the script
RPiLarm.cleanup()
sys.exit(0)
