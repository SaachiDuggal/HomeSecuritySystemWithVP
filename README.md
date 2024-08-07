# Home Security System with Computer Vision

## Overview
This project presents the development of a comprehensive home security system leveraging computer vision techniques and video processing in Python. The system is designed to detect and respond to potential security threats, particularly focusing on identifying unknown individuals entering the premises while distinguishing them from registered family members.

## Key Features
- **Real-time Face Detection and Recognition**: Utilizes the OpenCV library to detect and recognize faces.
- **Footage Recording**: Records and saves video footage upon detecting unknown faces.
- **Immediate Notifications**: Sends a notification to the user with a photo of the intruder and options to view live stream or saved footage.
- **SOS Emergency Alert**: An emergency alert feature for immediate response in critical situations.

## Implementation
- **OpenCV**: Used for face detection and recognition, leveraging a trained model to distinguish between registered and unknown faces.
- **Security Measures**: Initiates recording and secure saving of footage upon detecting an unknown face.
- **User Alerts**: Sends notifications with a photo of the detected intruder, providing access to live or recorded footage.

## Results
The system effectively detects and responds to potential security threats with minimal false positives. It ensures that registered family members are not mistakenly flagged as intruders, enhancing usability and reliability.

## Future Work
Potential enhancements include integrating additional sensors, improving real-time performance, and expanding the system's capabilities for advanced threat detection.
