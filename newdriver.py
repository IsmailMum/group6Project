import bluetooth
import sys
import re
import pyautogui
import time
re.compile('<title>(.*)</title>')

target_name = "HC-05"
target_address = "00:20:10:09:10:F6"

nearby_devices = bluetooth.discover_devices()

for bdaddr in nearby_devices:
    if target_name == bluetooth.lookup_name( bdaddr ):
        target_address = bdaddr
        break

if target_address is not None:
    print("found target bluetooth device with address "), target_address
else:
    print("could not find target bluetooth device nearby")
    

bd_addr = "00:20:10:09:10:F6"

port = 1
sock = bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((bd_addr, port))
pyautogui.keyDown('alt')
time.sleep(.2)
pyautogui.press('tab')
time.sleep(.2)
pyautogui.keyUp('alt')
time.sleep(.2)
pyautogui.press('1')
time.sleep(.2)
pyautogui.press('2')
time.sleep(.2)
pyautogui.press('3')
time.sleep(.2)
pyautogui.press('4')

print ('Connected')
current_key = 'x'
while(True):
    input_data = sock.recv(12)
    decoded_input_data = input_data.decode()
    x = list (map (int, re.findall(r'\d+', decoded_input_data)))
    if (len (x) == 2):
        
        if x[0] <= 500 and x[1] <= 500 and current_key != 'w':
            current_key = 'w'
            pyautogui.keyDown(current_key)
            	
        if x[0] >= 3500 and x[1] >= 3500 and current_key != 's':
            current_key = 's'
            pyautogui.keyDown(current_key)

        if x[0] <= 500 and x[1] >= 3500 and current_key != 'a':
            current_key = 'a'
            pyautogui.keyDown(current_key)
            
        if x[0] >= 3500 and x[1] <= 500 and current_key != 'd':
            current_key = 'd'
            pyautogui.keyDown(current_key)
            		
        if x[0] >= 2000 and x[0] <= 3000 and x[1] >= 2000 and x[1] <= 3000:
        	pyautogui.keyUp(current_key)

        if x[0] >= 2000  and x[0] <= 3000 and x[1] >= 2000 and x[1] <= 3000:
            current_key = 'x'
            


	


sock.close()