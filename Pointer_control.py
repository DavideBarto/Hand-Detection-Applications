import time
import numpy as np
import HandTrackingModule as htm
import cv2
import pyautogui
import Utilities as fct

# Modality in which the user can control the position of the mouse, left click with the thumb and right click
# with the ring finger. Is also possible to control the volume by rising all the fingers and moving the index finger
def mouse_control():

    ###################################
    wCam, hCam = 640,480
    frameR = 100 #frame reduction to detect properly
    smoothening = 3
    pTime = 0
    cTime = 0
    ###################################

    plocX,plocY = 0,0
    clocX, clocY = 0,0

    cap = cv2.VideoCapture(0)
    cap.set(3,wCam)    #set height and width
    cap.set(4,hCam)
    detector = htm.handDetector()
    wScr, hScr = pyautogui.size()

    while True:
        success, img = cap.read()  # give our frame
        img = cv2.flip(img, 1)  # to have the right movement

        #find hand landmarks
        img = detector.findHands(img)
        lmRight = detector.findPosition(img,handNo=0)

        if len(lmRight) != 0 :
            index_right = lmRight[8]
            middle_right = lmRight[12]
            fingersUp = detector.fingersUp()
            cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR), (255, 0, 255), 2)

            if fingersUp[1] and fingersUp[2] and not fingersUp[4]:
                #mouse modality
                pointer_x, pointer_y = fct.calculate_middle_point(index_right,middle_right)
                cv2.circle(img, (pointer_x,pointer_y), 15, (255,0,255), cv2.FILLED)

                pointer_x = np.interp(pointer_x, (frameR,wCam-frameR),(0,wScr))
                pointer_y = np.interp(pointer_y, (frameR,hCam-frameR),(0,hScr))

                #smooth the values
                clocX = plocX + (pointer_x-plocX) / smoothening
                clocY = plocY + (pointer_y-plocY) / smoothening


                pyautogui.moveTo(clocX, clocY)
                plocX,plocY = clocX,clocY

                if fct.calculate_distance(lmRight[3],lmRight[5]) < 25:
                    pyautogui.click()

                if fingersUp[3]:
                    pyautogui.rightClick()


            if fingersUp[2] and fingersUp[3] and fingersUp[4]:
                fct.VolumeController(lmRight,img)

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, 'FPS:' + str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255),3)  # position of word and color and font
        cv2.imshow('Image', img)
        key = cv2.waitKey(1)

        if key == ord('q'):
            break