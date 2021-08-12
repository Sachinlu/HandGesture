import cv2  # import opencv for the project
import mediapipe as mp  # import mediapipe platform for hand gesture

""""" Read image from camera at port 1 which is external webcam
in case of your laptop (internal) camera, use port 0"""""

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands  # fetch hands from mediapipe and store it in a variable
hands = mpHands.Hands()  # fetch one single hand from 2 hands present in mpHands.
mpDraw = mp.solutions.drawing_utils  # now we need to draw points on the hand

while True:
    success, img = cap.read()  # read image successfully
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # convert image to RGB value
    results = hands.process(imgRGB)  # process the image (find hand) and store the result.
    if results.multi_hand_landmarks:  # if there are any hands in image we proceed and process.
        for handNO in results.multi_hand_landmarks:
            for id, lm in enumerate(handNO.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                print(id, cx, cy)
            mpDraw.draw_landmarks(img, handNO, mpHands.HAND_CONNECTIONS)  # Now we draw points on image and draw
        # connection between those points using green line
    cv2.imshow("IMAGE", img)  # We show these points and line on the camera screen

    if cv2.waitKey(1) & 0XFF == ord('q'):
        break  # Press q to Quit
