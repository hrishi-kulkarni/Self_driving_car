from skimage import io
import numpy as np
from sklearn.externals import joblib
from serial import Serial
import time
import cv2
import urllib
import requests
from io import BytesIO
from PIL import Image
import numpy as np
from sklearn.externals import joblib

arduino = Serial('COM3', 250000)
time.sleep(2)
'''
arduino.write(b'forward_on\n')
time.sleep(0.1)
arduino.write(b'forward_off\n')
time.sleep(0.1)
arduino.write(b'backward_on\n')
time.sleep(0.1)
arduino.write(b'backward_off\n')
time.sleep(0.1)
arduino.write(b'left_on\n')
time.sleep(0.1)
arduino.write(b'left_off\n')
time.sleep(0.1)
arduino.write(b'right_on\n')
time.sleep(0.1)
arduino.write(b'right_off\n')
TESTING OF CAR
'''
CAMERA_URL = 'http://192.168.225.35:8080/live.jpg'
ARDUINO_SERVER = 'http://localhost:5000'

clf = joblib.load('model.pkl')
'''
scaler = joblib.load('scaler.pkl')
scaler_stop = joblib.load('stop/scaler.pkl')
is_stop = joblib.load('stop/model.pkl')
'''
print('model loaded')

def send_command(result):
    if result == '0':
        arduino.write(b'5\n')
        time.sleep(0.1)
        arduino.write(b'9\n')
        return
    elif result == '1':
        arduino.write(b'2\n') #lo
        time.sleep(0.5)
        arduino.write(b'5\n') #fo
        time.sleep(0.1)
        arduino.write(b'9\n') #fof
        time.sleep(0.5)
        arduino.write(b'6\n')   #lof
        return
    elif result == '2':
        arduino.write(b'3\n') #ro
        time.sleep(0.5)
        arduino.write(b'5\n') 
        time.sleep(0.1)
        arduino.write(b'9\n')
        time.sleep(0.5)
        arduino.write(b'7\n') #rof
        return
    else:
        arduino.write()

def drive():
    response = requests.get(CAMERA_URL)
    img = Image.open(BytesIO(response.content)).convert('L')
    img_as_array = np.ndarray.flatten(np.array(img))
    result = clf.predict([img_as_array])[0]
    # print(result)
    send_command(result)
    time.sleep(0.5)
    drive()
print('start driving')
drive()