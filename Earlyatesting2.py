from serial import Serial
import requests
from PIL import Image
from io import BytesIO
import time
import uuid
arduino = Serial('COM3', 9600)
time.sleep(5)
print("value1")
arduino.write(b'forward_on\n')
time.sleep(2)
print("value1")
arduino.write(b'forward_off\n')
time.sleep(2)
print("value1")
arduino.write(b'forward_off\n')
time.sleep(2)
arduino.write(b'forward_off\n')
time.sleep(2)