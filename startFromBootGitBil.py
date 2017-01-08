#make this file start at boot
#guide how to do it
#https://www.raspberrypi.org/documentation/linux/usage/rc-local.md

import RPi.GPIO as GPIO
import os
GPIO.setmode(GPIO.BOARD)
#button-pins
blueBPin=18
purpleBPin=16
GPIO.setup(blueBPin, GPIO.IN)
GPIO.setup(purpleBPin, GPIO.IN)


def RPiB():
    blueBInput=GPIO.input(blueBPin)
    purpleBInput=GPIO.input(purpleBPin)
    
    if blueBInput==True:
        print("hello!!!")
        os.system("sudo python /home/pi/Desktop/Bil/GitBil.py")
    else:
        pass
    if purpleBInput==True:
        print("asdkfjasd;fldjas")
        time.sleep(2)
        if purpleBInput==True:
            os.system("shutdown now -h")

while True:
    RPiB()
