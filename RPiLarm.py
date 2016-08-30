#!/usr/bin/python
#
# This is the MakeTronix.co.uk Alarm Library
#
# This is a means of talking to the components of MakeTronix.co.uk Alarm
#
# Created by Zachary Igielman, December 2015
# Copyright Zachary Igielman & Jake Blumenow, MakeTronix (Alarm)
#
# This code is in the public domain and may be freely copied and used
# No warranty is provided or implied
#

#======================================================================
# General Functions
# (Both versions)
#
# init(). Initialises GPIO pins
# cleanup(). Turns all components off and sets GPIO to standard values
#======================================================================
#======================================================================
# Alarm Functions
#
# getMotion(): returns the state of the motion sensor
# getKey(): waits for user to press and returns the number
# digit(): waits to recieve one keypress and returns number
# getCode(): waits for user to enter four numbers and returns code
# sound(secs): makes buzzer sound for time duration of seconds
# soundOn(): turns buzzer on permenantly
# soundOff(): turns buzzer off permenantly
# light(secs): makes LED sound for time duration of seconds
# lightOn(): turns LED on permenantly
# lightOff(): turns LED off permenantly

# Import all necessary libraries
import RPi.GPIO as GPIO, time

# Define pin numbers for keys
KEYPAD_NUMBERS = {1: 5, 2: 13, 3: 26, 4: 7, 5: 15, 6: 24, 7: 11, 8: 19, 9: 22, 0: 21, 'DEL': 23};

# Pins for LEDs, buzzer and PIR
LED = 12
BUZZER = 10
PIR = 8

# General Functions
#
# init(). Initialises GPIO pins
def init():
    #use physical pin numbering
    GPIO.setmode(GPIO.BOARD)
    GPIO.set_warnings(False)

    #set up LED, buzzer, PIR and keys
    GPIO.setup(LED, GPIO.OUT)
    GPIO.setup(BUZZER, GPIO.OUT)
    GPIO.setup(PIR, GPIO.IN)
    for k, v in KEYPAD_NUMBERS.iteritems():
        GPIO.setup(v, GPIO.IN, pull_up_down=GPIO.PUD_UP)


# cleanup(). Turns all components off and sets GPIO to standard values
def cleanup():
    GPIO.output(BUZZER, 0)
    GPIO.output(LED, 0)
    GPIO.cleanup()


# End of General Functions
#======================================================================






#======================================================================
# Alarm Functions

# getMotion(): returns the state of the motion sensor
def getMotion():
    return GPIO.input(PIR)


# getKey(): waits for user to press and returns the number
def getKey():
    s = None
    while s==None:
        for k, v in KEYPAD_NUMBERS.iteritems():
            if GPIO.input(k):
                s=v
    return s


# digit(): waits to recieve one keypress and returns number
def digit():
    # Loop while waiting for a keypress
    r = None
    while r == None:
        r = kp.getKey()
    return r


# getCode(): waits for user to enter four numbers and returns code
def getCode():
    # Getting digit 1, printing it, then sleep to allow the next digit press.
    d1 = digit()
    sleep(1)
    d2 = digit()
    sleep(1)
    d3 = digit()
    sleep(1)
    d4 = digit()
    return BLAH


# sound(secs): makes buzzer sound for time duration of seconds
def sound(secs):
    GPIO.output(BUZZER, 1)
    time.sleep(secs)
    GPIO.output(BUZZER, 0)


# soundOn(): turns buzzer on permenantly
def soundOn():
    GPIO.output(BUZZER, 1)


# soundOff(): turns buzzer off permenantly
def soundOff():
    GPIO.output(BUZZER, 0)


# light(secs): makes LED sound for time duration of seconds
def light(secs):
    GPIO.output(LED, 1)
    time.sleep(secs)
    GPIO.output(LED, 0)


# lightOn(): turns LED on permenantly
def lightOn():
    GPIO.output(LED, 1)


# lightOff(): turns LED off permenantly
def lightOff():
    GPIO.output(LED, 0)
