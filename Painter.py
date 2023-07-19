import cv2
import numpy as np
import time
import os
import HandTrackingModule as htm

# Painter modality where the user can draw with the index finger up and select with
# index and middle fingers up

def painter():
    brushThickness = 10
    eraserThickness = 10

    folderPath = 'paint_menu/brush_colors'
    myList = os.listdir(folderPath)
    overlayList = []

    folderBrush = 'paint_menu/brush_size'
    myListBrush = os.listdir(folderBrush)
    overlayListBrush = []

    for imagePath in myList:
        image = cv2.imread(f'{folderPath}/{imagePath}')
        overlayList.append(image)

    for imagePath in myListBrush:
        imageb = cv2.imread(f'{folderBrush}/{imagePath}')
        overlayListBrush.append(imageb)

    header = overlayList[0]  # starting image
    brush_img = overlayListBrush[0]
    drawColor = (255, 0, 255)
    detector = htm.handDetector(detectionCon=0.85)  # we wanna it to be good in painting
    xp, yp = 0, 0

    imgCanvas = np.zeros((720, 1280, 3), np.uint8)

    cap = cv2.VideoCapture(0)
    cap.set(3, 1280)
    cap.set(4, 720)

    while True:
        # import image
        success, img = cap.read()
        img = cv2.flip(img, 1)  # to have the right movement

        # Find hand LandMarks
        img = detector.findHands(img)
        lmList = detector.findPosition(img, draw=False)

        if len(lmList) != 0:
            # tip of index and middle fingers
            x1, y1 = lmList[8][1:]
            x2, y2 = lmList[12][1:]

            # Check which finger are up
            fingers = detector.fingersUp()

            # If two fingers are up we have to select, not draw
            if fingers[1] and fingers[2]:
                xp, yp = 0, 0
                # selection mode

                # Checking for the click
                if y1 < 125:  # we are in the header
                    if 250 < x1 < 450:
                        header = overlayList[0]
                        drawColor = (255, 0, 255)
                    elif 550 < x1 < 750:
                        header = overlayList[1]
                        drawColor = (255, 0, 0)
                    elif 800 < x1 < 950:
                        header = overlayList[2]
                        drawColor = (0, 255, 0)
                    elif 1050 < x1 < 1250:
                        header = overlayList[3]
                        drawColor = (0, 0, 0)

                if x1 < 100:  # we are in the header
                    if 150 < y1 < 250:
                        brush_img = overlayListBrush[0]
                        brushThickness = 10
                        eraserThickness = brushThickness
                    elif 350 < y1 < 450:
                        brush_img = overlayListBrush[1]
                        brushThickness = 20
                        eraserThickness = brushThickness
                    elif 500 < y1 < 700:
                        brush_img = overlayListBrush[2]
                        brushThickness = 40
                        eraserThickness = brushThickness

                cv2.rectangle(img, (x1, y1 - 15), (x2, y2 + 15), drawColor, cv2.FILLED)


            if fingers[1] and fingers[2] == False:
                cv2.circle(img, (x1, y1), 15, drawColor, cv2.FILLED)
                # drawing mode
                if xp == 0 and yp == 0:  # first frame
                    xp, yp = x1, y1

                if drawColor == (0, 0, 0):
                    cv2.line(img, (xp, yp), (x1, y1), drawColor, eraserThickness)
                    cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, eraserThickness)
                else:
                    cv2.line(img, (xp, yp), (x1, y1), drawColor, brushThickness)
                    cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, brushThickness)

                xp, yp = x1, y1  # previous points

        imgGray = cv2.cvtColor(imgCanvas, cv2.COLOR_BGR2GRAY)
        _, imgInv = cv2.threshold(imgGray, 50, 255,
                                  cv2.THRESH_BINARY_INV)  # create a mask to convert black to white and color into white
        imgInv = cv2.cvtColor(imgInv, cv2.COLOR_GRAY2BGR)
        img = cv2.bitwise_and(img, imgInv)
        img = cv2.bitwise_or(img, imgCanvas)
        # If drawing mode, one finger is up
        img[0:720, 0:100] = brush_img
        img[0:125, 0:1280] = header  # assign to this area of the image the header img
        cv2.imshow('Image', img)
        #cv2.imshow('Canvas', imgCanvas)
        key = cv2.waitKey(1)

        if key == ord('q'):
            break
