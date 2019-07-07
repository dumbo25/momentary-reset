#!/usr/bin/env python

#########################
#
# onOff.py controls Adafruit's Rugged Metal Of/Off Switch with Blue
# LED Ring. The script turns on the led when a Raspberry Pi is running, and it
# will reboot the Raspberry Pi if the button is pushed in and out in less than
# 5 seconds, or shutdown if more than 5 seconds.
#
# Adafruit's on/off rugged blue led  button has five pins:
#   +   = power, which attaches to GPIO_LED pin
#   -   = ground, which attaches to ground
#   NO1 = Normally Open, which is attached to GPIO_IN pin
#   NC1 = Normally Closed, which is attached to GPIO_OUT pin
#   C1  = This is not used

# I use three question (???) marks to indicate features that are not quite
# finished
#   ??? nothing to do right now
#
# onOff.py was tested on a Raspberry Pi 3 model B+ running raspbian
# stretch and osmc
#
# Run the script using the command:
#   $ sudo python onOff.py
#
# onOff.py requires:
#   $ sudo apt-get install python-pip python-dev gcc
#   $ sudo pip install rpi.gpio
#
# Previous versions of this script used the "run pins" on the Raspberry Pi.
# This approach had two drawbacks: 1) shorting the run pins can allow the
# microSD card to become corrupt and require it to be reflashed, 2) the run
# pins required soldering headers on the Raspberry Pi.
#
# This script either reboots the Raspberry Pi or does a proper shutdown.
#
# onOff.py runs with a systemd seervice:
#   $ wget https://raw.githubusercontent.com/dumbo25/momentary-reset/master/onOff.service
#
# Copy the systemd service file using:
#   $ sudo cp onOff.service /lib/systemd/system/.
#
# After any changes to /lib/systemd/system/onOff.service:
#    sudo systemctl daemon-reload
#    sudo systemctl enable onOff.service
#    sudo reboot
#
# Ensure the run-fan.service in systemd is enabled and running:
#    systemctl list-unit-files | grep enabled
#    systemctl | grep running | grep onOff
#    systemctl status onOff.service -l
#
# If there are any issues with starting the script using systemd,
# then examine the journal using:
#    sudo journalctl -u onOff.service


#########################
import RPi.GPIO as GPIO
import subprocess
import time
import datetime

#########################
# Global Constants
HOME = "/home/osmc"
# Don't use run pins or GPIO 4
GPIO_IN = 23  # normally open
GPIO_LED = 24
GPIO_OUT = 25 # normally closed

#########################
# Global Variables
fileLog = open(HOME + '/onOff.log', 'w+')
LEDon = True
Debug = True
# assume the button i sin the out position
ButtonOut = True
StartTime = 0.0

#########################
# Log messages should be time stamped
def timeStamp():
    t = time.time()
    s = datetime.datetime.fromtimestamp(t).strftime('%Y/%m/%d %H:%M:%S - ')
    return s

# Write messages in a standard format
def printMsg(s):
    fileLog.write(timeStamp() + s + "\n")
    if Debug:
        print(timeStamp() + s)
    fileLog.flush()

# normally open
def inFalling(channel):
    global ButtonOut
    global StartTime

    printMsg("inFalling = " + str(channel))

    # button pushed in
    StartTime = time.time()
    printMsg("   Falling edge detected, start time = " + str(StartTime))
    ButtonOut = False

# normally closed
def outFalling(channel):
    global ButtonOut
    global StartTime

    printMsg("outInterrupt = " + str(channel))

    # the button must start in an out state
    # however, the button could be in an instate after power on
    # if the button was in, then ignore the first out push
    if ButtonOut:
        printMsg("   ignore first push out")
        ButtonOut = False
        return

    # button was pushed in, it was pushed again and now pops out
    buttonOut = True
    printMsg("   Rising edge detected")

    # need to determine how long between button pushes
    if StartTime > 0.0:
        newStartTime = time.time()
        buttonTime = newStartTime - StartTime
        StartTime = newStartTime
    else:
        buttonTime = 0.0
    printMsg("   button time = " + str(buttonTime))

    # a long button press causes a shutdown, but too long
    # and it is probably the kids playing with it
    if buttonTime >= 10.0 and buttonTime < 60.0:
        printMsg("Shutting down")
        cmd = "sudo shutdown -h 0"
        subprocess.call(cmd, shell=True)
    elif buttonTime >= 0.5 and buttonTime <= 5.0:
        printMsg("Rebooting")
        cmd = "sudo reboot"
        subprocess.call(cmd, shell=True)
    else:
        printMsg("ignoringing outInterrupt")


#########################
# start of main
printMsg("onOff started")

# Disable warnings
GPIO.setwarnings(False)

# turn on gpio pins
GPIO.setmode(GPIO.BCM)

GPIO.setup(GPIO_IN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(GPIO_IN, GPIO.FALLING, callback=inFalling, bouncetime=200)

GPIO.setup(GPIO_OUT, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(GPIO_OUT, GPIO.FALLING, callback=outFalling, bouncetime=200)

GPIO.setup(GPIO_LED, GPIO.OUT)

# turn on LED
if LEDon:
    printMsg("Push Button LED on")
    GPIO.output(GPIO_LED,True)
else:
    printMsg("Push Button Ring LED off")
    GPIO.output(GPIO_LED,False)

try:
    while True:
        # there is no point in running all the time
        # because the GPIO will cause an interrupt
        time.sleep(1)

except KeyboardInterrupt: # trap a CTRL+C keyboard interrupt
    printMsg("keyboard exception occurred")

except Exception as ex:
    printMsg("ERROR: an unhandled exception occurred: " + str(ex))

finally:
    GPIO.cleanup()
    printMsg("onOff terminated")
    fileLog.close()
