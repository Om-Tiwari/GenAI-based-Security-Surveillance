import serial
import cv2

# Establish serial connection with Arduino
ser = serial.Serial('COM7', 9600)


while True:
    print("Started Working")
    while True:
        cap = cv2.VideoCapture(0)
        # Check for signal from Arduino
        if ser.in_waiting > 0:
            message = ser.readline().decode('utf-8').rstrip()
            if message == "DoorbellPressed":
                print("Doorbell pressed detected!")

                # Capture an image from the webcam
                ret, frame = cap.read()

                # Save the captured frame as an image
                cv2.imwrite("cap.jpg", frame)
                cap.release()