from serial import Serial
import requests
import io
from PIL import Image
from io import BytesIO
import time
import uuid
import os
import numpy as np
import cv2
import urllib
arduino = Serial('COM3', 250000)
# wait for the serial port to be ready
time.sleep(2)

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def save_data(command):
    # request the image many times
    # for some reasons the app doesn't always return
    # the latest image if you request it only once ¯\_(ツ)_/¯
    
    url1='http://192.168.43.164:8080/live.jpg'
    #imgResp=urllib.urlopen(url)
    for _ in range(0,3):
        try:
            imgResp=urllib.request.urlopen(url1)
            #imgResp = url.read()
            #print(type(imgResp))
            imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
            img=cv2.imdecode(imgNp,-1)
            cv2.imwrite('{}_{}.jpg'.format(uuid.uuid1(), command),img)
            #break
        except:
            pass

@app.route("/forward")
def forward():
    save_data(0)
    arduino.write(b'5\n')
    time.sleep(0.2)
    arduino.write(b'9\n')
    return 'forward'

#forward=>0, backward=>3, left=>1, right=>2
@app.route("/backward")
def backward():
    save_data(3)
    #arduino.write(b'4\n') #backward on
    #time.sleep(0.15)
    arduino.write(b'8\n') #backward off
    return 'backward'


@app.route("/left")
def left():
    save_data(1)
    arduino.write(b'2\n') #lo
    time.sleep(0.3)
    '''arduino.write(b'5\n') #fo
    time.sleep(0.2)
    arduino.write(b'9\n') #fof
    time.sleep(0.05)'''
    arduino.write(b'6\n')   #lof
    return 'left'

@app.route("/right")
def right():
    save_data(2)
    arduino.write(b'3\n') #ro
    time.sleep(0.3)
    '''arduino.write(b'5\n') 
    time.sleep(0.2)
    arduino.write(b'9\n')
    time.sleep(0.05)'''
    arduino.write(b'7\n') #rof
    return 'right'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)