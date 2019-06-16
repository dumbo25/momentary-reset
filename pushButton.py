#!/usr/bin/env python

#########################
#
# pushButton.py controls Adafruit's Momentary Rugged Metal Pushbutton with Blue
# LED Ring. The script turns on the led when a Raspberry Pi is running, and it
# will shutdown the Raspberry Pi if the button is pushed twice within 3 seconds
# or reboot if pushed twice more than 10 seconds and less than 20 seconds apart.
#
# The choice of a momentary push button was the wrong choice.
#
# Adafruit's momentary rugged blue led  button has five pins:
#   +   = power, which attaches to GPIO_LED pin
#   -   = ground, which attaches to ground
#   NO1 = Normally open, which is attached to GPIO_RESET pin
#   NC1 = Normally Closed, which is not used
#   C1  = This is not used

# I use three question (???) marks to indicate features that are not quite
# finished
#   ??? add logfile - nothing is being written to the logfile
#   ??? move from init.d to systemd
#
# pushButton.py was tested on a Raspberry Pi 3 model B+ running raspbian
# stretch and osmc
#
# Run the script using the command:
#   $ sudo python pushButton.py --light
#
# pushButton.py requires:
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
# pushButton.py runs with a systemd seervice:
#   $ wget https://raw.githubusercontent.com/dumbo25/momentary-reset/master/pushButton.service
#
# Copy the systemd service file using:
#   $ sudo cp pushButton.service /lib/systemd/system/.                 
#
# After any changes to /lib/systemd/system/pushButton.service:
#    sudo systemctl daemon-reload
#    sudo systemctl enable pushButton.service
#    sudo reboot
#
# Ensure the run-fan.service in systemd is enabled and running:
#    systemctl list-unit-files | grep enabled | grep pushButton
#    systemctl | grep running | grep pushButton
#    systemctl status pushButton.service -l
#
# If there are any issues with starting the script using systemd,
# then examine the journal using:
#    sudo journalctl -u pushButton.service
#
#########################

#########################
import RPi.GPIO as GPIO
import subprocess
import argparse
import time
import datetime

#########################
# Global Constants
HOME = "/home/osmc"
# Don't use run pins or GPIO 4
GPIO_RESET = 23
GPIO_LED = 24

#########################
# Global Variables
fileLog = open(HOME + '/pushButton.log', 'w+')
firstPush = True
lastTime = 0
nextTime = 0
LEDon = True

#########################
# Log messages should be time stamped
def timeStamp():
    t = time.time()
    s = datetime.datetime.fromtimestamp(t).strftime('%Y/%m/%d %H:%M:%S - ')
    return s

# Write messages in a standard format
def printMsg(s):
    fileLog.write(timeStamp() + s + "\n")

# from https://raspberrypi.stackexchange.com/questions/63512/how-can-i-detect-how-long-a-button-is-press$
def resetInterrupt(channel):
    global lastTime
    global nextTime
    global firstPush

    # print("in interrupt, channel = " + str(channel))
    if firstPush:
        lastTime = time.time()
        firstPush = False
        # print("last time = " + str(lastTime))
        return
    else:
        nextTime = time.time()
        # print("next time = " + str(nextTime))

    buttonTime = nextTime - lastTime

    # print("button time = " + str(buttonTime))

    if buttonTime >= 10 and buttonTime <= 20:
        # print("Shutting down")
        printMsg("Shutting down")
        cmd = "sudo shutdown -h 0"
        subprocess.call(cmd, shell=True)
    elif buttonTime >= 0.5 and buttonTime <= 3:
        # print("rebooting")
        printMsg("Rebooting")
        cmd = "sudo reboot"
        subprocess.call(cmd, shell=True)
    elif buttonTime > 20:
        # print("resetting last time = " + str(lastTime))
        lastTime = nextTime

#########################
# start of main
parser = argparse.ArgumentParser()

# Disable warnings
GPIO.setwarnings(False)

# turn on gpio pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_RESET, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(GPIO_RESET, GPIO.FALLING, callback=resetInterrupt)

GPIO.setup(GPIO_LED, GPIO.OUT)

# turn on LED
if LEDon:
    # print("Push Button LED on")
    GPIO.output(GPIO_LED,True)
else:
    # print("Push Button Ring LED off")
    GPIO.output(GPIO_LED,False)

    try:
    while True:
        # there is no point in running all the time
        time.sleep(10000)

except KeyboardInterrupt: # trap a CTRL+C keyboard interrupt
    printMsg("keyboard exception occurred")

except Exception as ex:
    printMsg("ERROR: an unhandled exception occurred: " + str(ex))

finally:
    GPIO.cleanup()
    printMsg("pushButton terminated")
    fileLog.close()
