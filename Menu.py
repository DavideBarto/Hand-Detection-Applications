import cv2
import pyautogui
import HandTrackingModule as htm
from Painter import painter
from RockPaperScissor import rps
from Pointer_control import mouse_control

# Definition of the starting interface based on the fingers Up function
img0 = cv2.imread('Menu/1.jpg')
cap = cv2.VideoCapture(0)
detector = htm.handDetector()

while True:
    success, img = cap.read()  # give our frame
    img = cv2.flip(img, 1)  # to have the right movement
    #find hand landmarks
    img = detector.findHands(img)
    lmRight = detector.findPosition(img,handNo=0)

    if len(lmRight) == 0:
        img0 = cv2.imread('Menu/1.jpg')

    if len(lmRight) != 0:
        fingersUp = detector.fingersUp()
        if  sum(fingersUp[0:4]) == 0 or sum(fingersUp[0:4]) == 4:
            img0 = cv2.imread('Menu/1.jpg')


        if sum(fingersUp[0:4]) == 1:
            img0 = cv2.imread('Menu/2.jpg')
            if fingersUp[4] == 1:
                cv2.imshow('comm', img)
                painter()


        if  sum(fingersUp[0:4]) == 2:
            img0 = cv2.imread('Menu/3.jpg')
            if fingersUp[4] == 1:
                cv2.imshow('comm', img)
                rps()


        if  sum(fingersUp[0:4]) == 3:
            img0 = cv2.imread('Menu/4.jpg')
            if fingersUp[4] == 1:
                cv2.imshow('comm', img)
                mouse_control()



    cv2.imshow('Interface', img0)
    cv2.imshow('comm',img)
    key = cv2.waitKey(1)
