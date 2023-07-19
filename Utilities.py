import cv2
import time
import HandTrackingModule as htm
import pyautogui
import pycaw  #library to see
import math
import numpy as np
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# Here some functions are defined in order to calculate distance, control the volume of the computer with the index finger

#need to be passed the x and the y values
def calculate_distance(point1,point2):
    distance = math.dist(point1,point2)
    return distance



#calculate the middle point between two
def calculate_middle_point(point1,point2):
    x_m = int((point1[1]+point2[1]) /2)
    y_m = int((point1[2]+point2[2]) /2)
    return x_m,y_m



def line_creation(img,point1,point2):
    cv2.line(img, (point1[1],point1[2]), (point2[1],point2[2]), (255, 0, 255), 3)



def VolumeController(lmList,img):
    # initialization Volume
    index_tip = lmList[8]
    thumb_tip = lmList[4]
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER((IAudioEndpointVolume)))
    #volume_range = volume.GetVolumeRange()  #from -65.25 to 0
    volume.SetMasterVolumeLevel(-5.0, None)  # set volume
    minVol = -65
    maxVol = 0
    #vol = 0
    #volBar = 400
    ################################################################################
    # VOLUME CONTROLLER
    # line creation and center of line and length of the line to change volume
    line_creation(img,index_tip, thumb_tip)
    x_m, y_m = calculate_middle_point(index_tip, thumb_tip)
    cv2.circle(img, (x_m, y_m), 8, (255, 0, 255), cv2.FILLED)
    length = calculate_distance(index_tip, thumb_tip)
    # between 15 and 200
    if length < 40:
        cv2.circle(img, (x_m, y_m), 8, (0, 255, 0), cv2.FILLED)

    # Hand range 15 - 200
    # Volume range -65 0
    vol = np.interp(length, [5, 180], [minVol, maxVol])  # to adjust the change of length
    #volBar = np.interp(length, [15, 150], [400, 150])  # to adjust the change of length
    volume.SetMasterVolumeLevel(vol, None)
    # make appear a rectangle to visualize the volume
    #cv2.rectangle(img, (50, 150), (85, 400), (0, 255, 0), 3)
    #cv2.rectangle(img, (50, int(volBar)), (85, 400), (0, 255, 0), cv2.FILLED)
    ######################################################################################
