import bluetooth
import sys
import re
import pyautogui
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
   

print("address:", bdaddr)


import subprocess

name = target_name      # Device name
addr = target_address      # Device Address
port = 1         # RFCOMM port
passkey = "1234" # passkey of the device you want to connect

# kill any "bluetooth-agent" process that is already running
subprocess.call("kill -9 `pidof bluetooth-agent`",shell=True)

# Start a new "bluetooth-agent" process where XXXX is the passkey
status = subprocess.call("bluetooth-agent " + passkey + " &",shell=True)

# Now, connect in the same way as always with PyBlueZ
try:
    s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    s.connect((addr,port))
except bluetooth.btcommon.BluetoothError as err:
    print('error')
    exit(0)
    pass
s.disconnect((addr,port))