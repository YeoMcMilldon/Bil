import RPi as GPIO 
from nanpy import(ArduinoApi, SerialManager, Servo)
import time
import cwiid

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
noB=0

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
boolNoB=False

boolBList[boolTwoB, boolOneB, boolBB, boolAB, boolMinusB, boolHomeB, boolUpB, boolRightB, boolLeftB, boolPlusB]
BList[twoB, oneB, bB, aB, minusB, homeB, upB, rightB, leftB, plusB]
BPress=wm.state['buttons']

for listNumber in range(9, -1, -1)
    if BPress >= BList[listNumber]:
        boolBList[listNumber] == True
        BPress = BPress - BList[listNumber]
    else:
        pass
    listNumber = listNumber - 1



    


