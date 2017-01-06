import RPi.GPIO as GPIO
from nanpy import(ArduinoApi, SerialManager, Servo)
import time
import cwiid
import sleep
import os

GPIO.setmode(GPIO.BOARD)
#LED-pins
yPin=11
gPin=13
rPin=15
GPIO.setup(yPin, GPIO.OUT)
GPIO.setup(gPin, GPIO.OUT)
GPIO.setup(rPin, GPIO.OUT)
#button-pins
blueBPin=16
purpleBPin=18
GPIO.setup(blueBPin, GPIO.IN)
GPIO.setup(purpleBPin, GPIO.IN)

blueBInput=GPIO.input(blueBPin)
purpleBInput=GPIO.input(purpleBPin)

def RPiB():
    if blueBInput==True:
        exit()
    else:
        pass
    if purpleBInput==True:
        time.sleep(2)
        if purpleBInput==True:
            os.system("shutdown now -h")


def turnOnOffLED(colour, state):
    GPIO.output(colour, state)

def LEDOnOff(time, pin):
    turnOnOffLED(pin, True)
    time.sleep(time)
    turnOnOffLED(pin, False)



#Syncing the wii remote
turnOnOffLED(yPin, True)
print("Sync the wii remote.")
for x in range(0, 3):
    try:
        wm = cwiid.Wiimote()
        wm.rpt_mode = cwiid.RPT_BTN
        turnOnOffLED(yPin, False)
        LEDOnOff(2, gPin)
        break
    except:
        turnOnOffLED(yPin, False)
        turnOnOffLED(rPin, True)
        print("could not sync with the Wii Remote")


#start serial communication with Arduino Uno
turnOnOffLED(yPin, True)
 for x in range(0, 3)
    try:
        print('Starting serial communication')
        connection = SerialManager()
        a = ArduinoApi(connection = connection)
        turnOnOffLED(yPin, False)
        LEDOnOff(2, gPin)
        break
    except:
        turnOnOffLED(yPin, False)
        LEDOnOff(2, rPin)
        print('FAILED')



#Wii Remote buttons(horisontal, B stands for Button)
leftB=2048
upB=512
downB=256
rightB=1024
aB=8
bB=4
plusB=4096
homeB=128
minusB=16
oneB=2
twoB=1

boolLeftB=False
boolUpB=False
boolDownB=False
boolRightB=False
boolAB=False
boolBB=False
boolPlusB=False
boolHomeB=False
boolMinusB=False
boolOneB=False
boolTwoB=False

boolBList[boolTwoB, boolOneB, boolBB, boolAB, boolMinusB, boolHomeB, boolUpB, boolRightB, boolLeftB, boolPlusB]
BList[twoB, oneB, bB, aB, minusB, homeB, upB, rightB, leftB, plusB]
BPress=wm.state['buttons']

#checking which buttons are pressed
def checkBPress():
    global boolBlist, Blist, BPress, boolTwoB, boolOneB, boolBB, boolAB, boolMinusB, boolHomeB, boolUpB, boolRightB, boolLeftB, boolPlusB
    for listNumber in range(9, -1, -1):
        if BPress >= BList[listNumber]:
            boolBList[listNumber] == True
            BPress = BPress - BList[listNumber]
        else:
            pass
        listNumber = listNumber - 1

#declare servo
wheelServo=Servo(9)
#declare h-bridge-pins 1
motor1Pin=3
direction1Pin1=8
direction1Pin2=7
a.pinMode(motor1Pin, a.OUTPUT)
a.pinMode(direction1Pin1, a.OUTPUT)
a.pinMode(direction1Pin2, a.OUTPUT)
#declare h-bridge-pins 2
motor2Pin=11
direction2Pin1=13
direction2pin2=12
a.pinMode(motor2Pin, a.OUTPUT)
a.pinMode(direction2Pin1, a.OUTPUT)
a.pinMode(direction2Pin2, a.OUTPUT)

#does things after buttons pressed
def RespondToWiiRemote():
    if boolLeft==True:
        #servo left
        wheelServo.write(45)
    elif boolRight==True::
        #servo right
        wheelServo.write(135)
    else:
        #servo middle
        wheelServo.write(90)
    
    if boolBB==True:
        a.digitalWrite(direction1Pin1, a.HIGH)
        a.digitalWrite(direction1Pin2, a.LOW)
        a.digitalWrite(direction2Pin1, a.HIGH)
        a.digitalWrite(direction2Pin2, a.LOW)
    else:
        a.digitalWrite(direction1Pin1, a.LOW)
        a.digitalWrite(direction1Pin2, a.HIGH)
        a.digitalWrite(direction2Pin1, a.LOW)
        a.digitalWrite(direction2Pin2, a.HIGH)
    
    if boolOneB==True:
        if boolTwoB==True:
            #drive at full speed
            a.digitalWrite(motor1Pin, a.HIGH)
            a.digitalWrite(motor2Pin, a.HIGH)
        else:
            #drive at half speed
            a.analogWrite(motor1Pin, 127)
            a.analogWrite(motor1Pin, 127)            
    else:
        #turn off motors
        a.digitalWrite(motor1Pin, a.LOW)
        a.digitalWrite(motor2Pin, a.LOW)

    if boolHomeB==True:
        #shut down program
        quit()

def Main():
    checkBPress()
    RespondToWiiRemote()
    time.sleep(0.1)
    


    


