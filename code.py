import os
import serial
import time
import cv2
import threading
from threading import Thread

# Serial port settings
serial_port = '/dev/ttyACM0'  # Modify this if your Arduino is connected to a different port
baud_rate = 9600

# Initialize serial communication
ser = serial.Serial(serial_port, baud_rate, timeout=1)

# Destination directory for storing images
image_directory = "/home/mahanivetha/camera"  # Modify this with the desired directory path

# Create the destination directory if it doesn't exist
os.makedirs(image_directory, exist_ok=True)

# Initialize the webcam
video_capture = cv2.VideoCapture(0)  # Use the appropriate index if you have multiple webcams

# Create a lock for thread synchronization
lock = threading.Lock()

# Flag to indicate if an RFID tag is scanned
tag_scanned = False

# UID of the scanned RFID tag
uid = None

# Access Rules (example)
access_rules = {
    "2271848952": "allow",
    "1954571157": "allow",
    "5114816326": "deny"
}

# Function to capture an image from the webcam
def capture_image():
    global tag_scanned
    global uid
    
    while True:
        with lock:
            if tag_scanned:
                ret, frame = video_capture.read()
                if ret:
                    # Generate a unique filename using timestamp
                    timestamp = int(time.time())
                    image_filename = f"image_{timestamp}.jpg"
                    image_path = os.path.join(image_directory, image_filename)
                    
                    # Check if the UID is in the access_rules and its permission is "deny"
                    if uid in access_rules and access_rules[uid] == "deny":
                        cv2.imwrite(image_path, frame)
                        print(f"Image captured: {image_path}")
                    
                    tag_scanned = False  # Reset the tag scanned flag
        time.sleep(0.1)

# Function to read data from Arduino
def read_arduino():
    global tag_scanned
    global uid
    
    while True:
        if ser.in_waiting > 0:
            data = ser.readline().decode().strip()
            print(f"Card UID: {data}")
            with lock:
                tag_scanned = True
                uid = data
                if data in access_rules:
                    access_permission = access_rules[data]
                    if access_permission == "allow":
                        grant_access()
                    else:
                        deny_access()

# Function to grant access
def grant_access():
    print("Access Granted")  # Replace with appropriate action, e.g., trigger door lock

# Function to deny access
def deny_access():
    print("Access Denied")  # Replace with appropriate action, e.g., display access denied message

# Create and start the threads
capture_thread = Thread(target=capture_image)
capture_thread.start()

read_arduino_thread = Thread(target=read_arduino)
read_arduino_thread.start()

# Wait for the threads to complete (you can interrupt with Ctrl+C)
try:
    capture_thread.join()
    read_arduino_thread.join()
except KeyboardInterrupt:
    pass

# Cleanup
ser.close()
video_capture.release()
cv2.destroyAllWindows()
