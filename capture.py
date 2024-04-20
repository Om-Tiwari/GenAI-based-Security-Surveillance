import serial
import cv2

# Establish serial connection with Arduino
ser = serial.Serial('COM7', 9600)  # Replace 'COM7' with the appropriate port for your Arduino

# Open webcam
cap = cv2.VideoCapture(0)

frames = []
current_frame = 0

while True:
    doorbell_pressed = False
    print("Started Working")
    while True:
        cap = cv2.VideoCapture(0)
        # Check for signal from Arduino
        if ser.in_waiting > 0:
            message = ser.readline().decode('utf-8').rstrip()
            if message == "DoorbellPressed":
                print("Doorbell pressed detected!")
                doorbell_pressed = True

                # Capture an image from the webcam
                ret, frame = cap.read()

                # Save the captured frame as an image
                name = f'frame{current_frame}.jpg'
                name = "cap.jpg"
                print(f"Creating file... {name}", end="\n\n")
                cv2.imwrite(name, frame)
                frames.append(name)
                current_frame += 1
                cap.release()

print("Work Ended")