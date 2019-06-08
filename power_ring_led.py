#!/usr/bin/env python

import RPi.GPIO as GPIO 
import subprocess 
import argparse  

parser = argparse.ArgumentParser()  
group = parser.add_mutually_exclusive_group() 
group.add_argument("-l", "--light", action="store_true") 
group.add_argument("-o", "--off", action="store_true")  

# Disable warnings 
GPIO.setwarnings(False)  

# turn on gpio pin 24 
GPIO.setmode(GPIO.BCM) 
GPIO.setup(24, GPIO.OUT)  

args = parser.parse_args() 
if args.light:  
    GPIO.output(24,True) 
elif args.off:
    GPIO.output(24,False)
