import cwiid
import time
from nanpy import (ArduinoApi, SerialManager)

try:
    ('Starting serial communication')
    connection = SerialManager()
    a = ArduinoApi(connection = connection)
except:
    print('FAILED')


a = ArduinoApi(connection = connection)
mpin = 16
spin = 9
s2pin = 10
bpin = 8
lpin = 3
l2pin = 4
l3pin = 5
a.pinMode(mpin, a.OUTPUT)
a.pinMode(spin, a.OUTPUT)
a.pinMode(s2pin, a.OUTPUT)
a.pinMode(bpin, a.OUTPUT)
a.pinMode(lpin, a.OUTPUT)
a.pinMode(l2pin, a.OUTPUT)
a.pinMode(l3pin, a.OUTPUT)
a.pinMode(mpin + 1, a.INPUT)


print('sync')

wm = cwiid.Wiimote()
wm.rpt_mode = cwiid.RPT_BTN
endo=False
wmstate = 14

print

def backo(backol):
    if backol == 1:
        a.digitalWrite(bpin, a.HIGH)
    else:
        a.digitalWrite(bpin, a.LOW)
        

def forwardo(speedo):
    if speedo == 0:
        a.analogWrite(mpin, 500)
    elif speedo == 1:
        a.analogWrite(mpin, 1023)
    elif speedo == 2:
        a.analogWrite(mpin, 0)
    elif speedo == 3:
        #servothing 2 brake
        print()

def directiono(directionol):
    #90 or 180 or 270
    print('function not done')

#def drive(direction, speed, back):
#    if direction == 0:
#        #servothing midle
#        if speed == 0:
#            forwardo(0)
#        else:
#            forwardo(1)
#        if back == 0:
#            backo(0)
#        else:
#            backo(1)
#            
#    elif direction == 1:
#        #servothing left
#        if speed == 0:
#            forwardo(0)
#        else:
#            forwardo(1)
#        if back == 0:
#            backo(0)
#        else:
#            backo(1)
#            
#    elif direction == 2:
#        #servothing right
#        if speed == 0:
#            forwardo(0)
#        else:
#            forwardo(1)
#        if back == 0:
#            backo(0)
#       else:
#            backo(1)
#    elif speed == 2:
#        forwardo(2)
#    elif speed == 3:
#        forwardo(3)

def drive(direction, speed, back):
    forwardo(speed)
    backo(back)
    directiono(direction)
    

def ReadWm():
    global wmstate
    if wm.state['buttons'] == 2:
        print('drive forward')
        wmstate = 0
        forwardo(0)
        
    elif wm.state['buttons'] == 3:
        print('drive forward(turbo)')
        wmstate = 1
        drive(0, 1, 0)
        
    elif wm.state['buttons'] ==2050:
        print('drive left')
        wmstate = 2
        drive(1, 0, 0)
        
    elif wm.state['buttons'] ==2051:
        print('drive left(turbo)')
        wmstate = 3
        drive(1, 1, 0)
        
    elif wm.state['buttons'] ==1026:
        print('drive right')
        wmstate = 4
        drive(2, 0, 0)
        
    elif wm.state['buttons'] ==1027:
        print('drive right(turbo)')
        wmstate = 5
        drive(2, 1, 0)
        
    elif wm.state['buttons'] ==6:
        print('drive backwards')
        wmstate = 6
        drive(0, 0, 1)
        
    elif wm.state['buttons'] ==7:
        print('drive backwards(turbo)')
        wmstate = 7
        drive(0, 1, 1)
        
    elif wm.state['buttons'] ==2054:
        print('drive backwards and right')
        wmstate = 8
        drive(1, 0, 1)
        
    elif wm.state['buttons'] ==2055:
        print('drive backwards and right(turbo)')
        wmstate = 9
        drive(1, 1, 1)
        
    elif wm.state['buttons'] ==1030:
        print('drive backwards and left')
        wmstate = 10
        drive(2, 0, 1)
        
    elif wm.state['buttons'] ==1031:
        print('drive backwards and left(turbo)')
        wmstate = 11
        drive(2, 1, 1)
        
    elif wm.state['buttons'] ==8:
        wmstate = 12
        print('brake')
        drive(0, 3, 0)
        
    elif wm.state['buttons'] ==128:
        wmstate = 13
        print('Bye')
        time.sleep(1)
        ard.write(wmstate)
        endo = True
        
    else:
        print('baow')
        wmstate = 14
        forwardo(2)
        
    time.sleep(0.075)
    print(wmstate,   a.analogRead(mpin + 1))
    

    
while not endo:
    ReadWm()
    

