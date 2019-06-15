# REST API to control the car
# each endpoint move the car toward a direction for a short time
from serial import Serial
import requests
from PIL import Image
from io import BytesIO
import time
import uuid
arduino = Serial("COM3", 250000)
# wait for the serial port to be ready
time.sleep(2)

from flask import Flask
from flask_cors import CORS

time.sleep(1)
arduino.write(b'left_on\n')
time.sleep(0.1)
arduino.write(b'forward_on\n')
time.sleep(1)
arduino.write(b'forward_off\n')
time.sleep(0.1)
arduino.write(b'left_off\n')
time.sleep(1)
'''
arduino.write(b'forward_on\n')
time.sleep(1)
arduino.write(b'forward_off\n')
time.sleep(1)

arduino.write(b'backward_on\n')
time.sleep(1)
arduino.write(b'backward_off\n')
time.sleep(1)
arduino.write(b'left_on\n')
time.sleep(1)
arduino.write(b'left_off\n')
time.sleep(1)
arduino.write(b'right_on\n')
time.sleep(1)
arduino.write(b'right_off\n')
time.sleep(1)

# check if everything is working

time.sleep(2)
arduino.write(b'forward_off\n')
time.sleep(2)
time.sleep(2)
arduino.write(b'backward_off\n')
time.sleep(2)
time.sleep(2)
arduino.write(b'right_off\n')
time.sleep(2)
arduino.write(b'left_off\n')
time.sleep(2)
'''

'''
arduino.write(b'forward_on\n')
time.sleep(0.05)
arduino.write(b'forward_off\n')
time.sleep(0.05)

arduino.write(b'backward_on\n')
time.sleep(0.05)
arduino.write(b'backward_off\n')
time.sleep(0.05)
arduino.write(b'left_on\n')
time.sleep(0.05)
arduino.write(b'left_off\n')
time.sleep(0.05)
arduino.write(b'right_on\n')
time.sleep(0.05)
arduino.write(b'right_off\n')

'''