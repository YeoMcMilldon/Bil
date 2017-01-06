import RPi.GPIO as GPIO
from nanpy import(ArduinoApi, SerialManager, Servo)
import time
import cwiid
import sleep

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

def _1():
    if boolLeft==True:
        #servo left
    elif boolRigth==True::
        #servo right
    else:
        #servo middle
    
    if boolBB==True:
        #backwardspin on
    else:
        #backwardspin off
    
    if boolOneB==True:
        if boolTwoB==True:
            #drive at full speed
        else:
            #drive at half speed

    if boolHomeB==True


    


