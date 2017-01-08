If the text looks weird use the raw mode above if you are on github.com
The word "Bil" is car in swedish.
If you want use my program, you will have to read mostly everything of this text. If you do not it is most likely that it does not work
First install the nanpy module and the firmware(to the Arduino Uno). There is a guide on this link: https://youtube.com/watch?v=QumlhvYtRKQ.
IT IS VERY IMPORTANT to put 1 instead of 0 on #define USE_SERVO in cfg.h(3:42 in the video).
Add startFromBootGitBil.py to /etc/rc.local. Type "python [full path]" above "exit 0" (the quotes are the show what to type, do not type the quotes in rc.local). In this example, I have already typed "python  /home/pi/Desktop/Bil/startFromBootGitBil.py".
This is rc.local

#!/bin/sh -e
#
# rc.local
#
# This script is executed at the end of each multiuser runlevel.
# Make sure that the script will "exit 0" on success or any other
# value on error.
#
# In order to enable or disable this script just change the execution
# bits.

# By default this script does nothing.

# Print the IP address
_IP=$(hostname -I) || true
if [ "$_IP" ]; then
  printf "My IP address is %s\n" "$_IP"
fi
python  /home/pi/Desktop/Bil/startFromBootGitBil.py
exit 0



Connect everthing as on the diagram in the file "Diagram".
Use an USB-cable and connect the Raspberry Pi 3 and the Arduino Uno.
Edit the file startFromBootGitBil.py and change the variable GitBilPath to the path of GitBil.py
After you have booted the Raspberry Pi 3, click the button connected to pin 18 on the Raspberry Pi 3(the blue button). 
If you have done everything correctly the yellow LED should be lit. Click the red sync button on the Wii Remote. 
If the green LED is lit you have synced successfully.If the red LED was lit instead you will have to try again.
You can try three times. I you want to change that, you change the for loop in GitBil.py line number 55.
Then the yellow LED should be lit again. It should try to establish serial communication with the Arduino Uno. It will try three times.
You can change that by changing the for loop in GitBit.py line number 70.
Then the program will register the button presses from both the Wii Remote and the two buttons.

Controls:
Press the 1-button to drive at halv speed.
Press both the 1-button and the 2-button to drive at full speed.
If you want to drive backwards hold the B-button.
If you want to use the servo, use the left and right-button to turn.
If you want to exit GitBil.py press the Home-button or press the button connected to pin number 18.
If you want to shut down the Raspberry Pi 3, hold button connected to pin number 16 on the Rapsberry Pi 3(purple button).

