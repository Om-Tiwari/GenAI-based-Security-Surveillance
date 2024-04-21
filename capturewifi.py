import serial
import requests
import numpy as np
import cv2

# Establish serial connection with Arduino``
ser = serial.Serial('COM7', 9600)

url = "http://192.0.0.4:8080/shot.jpg"

def captureMobileCam():
    img_resp = requests.get(url) 
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8) 
    img = cv2.imdecode(img_arr, -1)
    return img


while True:
    print("Started Working")
    while True: 
        # Check for signal from Arduino
        if ser.in_waiting > 0:
            message = ser.readline().decode('utf-8').rstrip()
            if message == "DoorbellPressed":
                print("Doorbell pressed detected!")

                # Capture an image from the webcam
                frame = captureMobileCam()

                # Save the captured frame as an image
                cv2.imwrite("cap.jpg", frame)