## Deriving Live Hand Detection using computer vision (v 1.0)
Computer vision is the most popular field today. 
Hand Gesture is one of the most advance ongoing Research. 
MediaPipe is open source library developed by google to understand the 
fundamentals of computer vision.

## Files
- Img-----------------> Sample Image taken from main.py output.
- main.py ---------- > Main python program file.
- README.md ----> This markdown file you are reading.
- Requirement.txt--> Required imports to run the program successfully.

## Description
Hand Gesture detection is possible using various ML model.
Our model has two main ML model running in parallel. 
Mediapipe is very advance cv library, developed by google.
[ visit the website for information](https://google.github.io/mediapipe/solutions/hands.html "Mediapipe Hands"). 
The aim of main.py is to detect hand(s) in the 3d plane and return its (x, y, z) coordinates.
Any hand(s) has 22 points (0 - 21) as shown below.

![MediaPipe_hands](https://google.github.io/mediapipe/images/mobile/hand_landmarks.png)
Main.py returns an array (Hand_point, X-axis, Y-axis). 
hand_point ranges between 0-21, and it's respective x, y value in 3D plane.
For example if the output is (8, 155, 196), this can be interpreted as 
(index_finger_tip, X-axis, Y-axis).
The following code prints the array.
``` python
            for id, lm in enumerate(handNO.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                print(id, cx, cy)
```
## Installation
(Optional) Setup a virtual environment to install necessary packages.
``` commandline
virtualenv .venv
source .venv/bin/activate
```
Install the packages listed in Requirement.txt file
```shell
pip install -r requirements.txt
```
Run Program!

## Usage
This program is simple and can be run using command line in system where python is already installed
```shell
Python main.py
```
You will see screen capturing your video and detecting hands. 
To quit any time simply press q on your keyboard.

_Remember_ the Port(0) is for an internal webcam and Port(1) for any external webcam. Make sure you have assigned
correct Port in a program at below block.
```python
cap = cv2.VideoCapture(0) # for inbuilt webcam (internal)
#or
cap = cv2.VideoCapture(1) # for external webcam
```
## Support
You can contact Author for any support.
* __Email__: [Mr. Sachin Singh](mailto:sachinsinghcad@gmail.com?subject=[GitHub]%20Source%20Han%20Sans)
* __Discord__: **sachin_singh#4558**

## Acknowledgement 
I Would like to give credits to 
* Mediapipe developers for contributing the best open source computer vision library.[Website](https://google.github.io/mediapipe/)
* Murtaza's Workshop - Robotics and AI. [Website](https://www.computervision.zone/courses/hand-tracking/
)
 ## Road Map
1. We can replace kiosk monitor touch using this application.
2. Touch-less User Interface (TUI) can be generated.

## License
This project is completely open-source and does not require any license to use it.

## Project Status
This project is currently under-development.There will be future improvements. 
* last Modification:- 08/11/2021 (mm/dd/yy)