
'''
Installing PySerial
    pip install pyserial
Installing Alsaaudio
    git clone https://github.com/larsimmisch/pyalsaaudio.git 
    cd pyalsaaudio
    pip install .

'''

import serial
import alsaaudio

ser = serial.Serial('/dev/ttyACM0', 9600)
device = alsaaudio.Mixer()

while True:
    if ser.inWaiting() > 0:
        data = ser.readline()
        data = int(data.decode())
        print(data)
        device.setvolume(data)
        print(device.getvolume())

ser.close()

