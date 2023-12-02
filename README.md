# RFID Access Control System

## Overview

This Python script creates a simple RFID (Radio-Frequency Identification) access control system using an Arduino and a webcam. The system captures an image from the webcam whenever an RFID tag is scanned and performs an action based on predefined access rules.

## Components

1. **Arduino:**
   - Connect the RFID reader to the Arduino, and connect the Arduino to the computer via USB.

2. **Serial Communication:**
   - The script establishes serial communication with the Arduino to receive RFID tag data.

3. **Webcam:**
   - The script captures an image from the webcam using OpenCV whenever an RFID tag is scanned.

4. **Access Rules:**
   - Define access rules using the UID (Unique Identifier) of RFID tags.
   - Example access rules:
     - Allow access for UID: 2271848952
     - Allow access for UID: 1954571157
     - Deny access for UID: 5114816326

## Instructions

1. **Serial Port Settings:**
   - Set the correct serial port (`serial_port`) where the Arduino is connected.
   - Modify the `baud_rate` if needed.

2. **Image Directory:**
   - Set the destination directory (`image_directory`) for storing captured images.

3. **Webcam Configuration:**
   - Adjust the webcam index (`video_capture = cv2.VideoCapture(0)`) if you have multiple webcams.

4. **Access Rules:**
   - Modify the `access_rules` dictionary to define access permissions based on RFID UIDs.

5. **Access Actions:**
   - Define actions to be taken upon access being granted or denied in the `grant_access` and `deny_access` functions.

6. **Run the Script:**
   - Run the script and ensure that the Arduino is properly connected.
   - The script will continuously monitor the Arduino for RFID tag data and capture images based on access rules.

7. **Interrupt the Script:**
   - The script can be interrupted using Ctrl+C in the terminal.

