import cv2
import mediapipe as mp
import time
import pyautogui   #library with scripts to control mouse and keyboard

#hand detector class to detect hands and landmarks 
class handDetector():
    def __init__(self, mode=False, max_number_Hands=2, modelComplex=1, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = max_number_Hands
        self.detectionCon = detectionCon
        self.modelComplex = modelComplex
        self.trackCon = trackCon
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.modelComplex, self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils
        self.tipIds = [4, 8, 12, 16, 20]

    def findHands(self, img, draw=True):
        # draw is a flag if we wanna draw or not the hands and critical points
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #works only with RGB
        self.results = self.hands.process(imgRGB)  # process frame for us

        if self.results.multi_hand_landmarks:
            # for each handLmarks (extract information for each hand)
            for handLms in self.results.multi_hand_landmarks:  # we are telling if we have some result, one ore two hands doesn't matter
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)  # img because we show our video image no rgb one. This show the hand points
        return img

# I have to use self.results to use it in the other method
    def findPosition(self, img, handNo=0, draw=True, radius_circle=5):
        self.lmList = [] #all landmark positions
        if self.results.multi_hand_landmarks:
            if len(self.results.multi_hand_landmarks) == 2:
            #we have to understand what hand we are talking about
                myHand = self.results.multi_hand_landmarks[handNo]
            else:
                myHand = self.results.multi_hand_landmarks[0]

            for id, lm in enumerate(myHand.landmark):
                #print(id,lm) each id has a landmark which has specoific x y and z
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)  # position of the center
                self.lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), radius_circle, (255, 0, 0), cv2.FILLED)
        return self.lmList


    def fingersUp(self):
        fingers = []
        #To understand if hand is opened or closed
        if self.lmList[self.tipIds[0]][1] < self.lmList[self.tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)
        #4 fingers
        for id in range(1,5):
            if self.lmList[self.tipIds[id]][2] < self.lmList[self.tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        return fingers



def main():

    cap = cv2.VideoCapture(0)
    detector = handDetector()  # no param because we have the default ones

    while True:
        success, img = cap.read()  # give our frame
        img = detector.findHands(img)
        lmList0 = detector.findPosition(img)
        lmList1 = detector.findPosition(img, handNo=1)

        if len(lmList0) != 0 or len(lmList1) != 0:
            #print(lmList[4])
            detector.drawCirclePolliceIndice(img, lmList0[4], lmList0[8])
            detector.drawCirclePolliceIndice(img, lmList1[4], lmList1[8])
        cv2.imshow('Image', img)
        cv2.waitKey(1)


if __name__ == "__main__":  # this mean 'if I'm running this part'
    main()
