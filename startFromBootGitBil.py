#make this file start at boot
#guide how to do it
#https://www.raspberrypi.org/documentation/linux/usage/rc-local.md

import RPi.GPIO as GPIO
import os

#button-pins
blueBPin=16
purpleBPin=18
GPIO.setup(blueBPin, GPIO.IN)
GPIO.setup(purpleBPin, GPIO.IN)

blueBInput=GPIO.input(blueBPin)
purpleBInput=GPIO.input(purpleBPin)

def RPiB():
    if blueBInput==True:
        os.system("python GitBil.py")
    else:
        pass
    if purpleBInput==True:
        time.sleep(2)
        if purpleBInput==True:
            os.system("shutdown now -h")
