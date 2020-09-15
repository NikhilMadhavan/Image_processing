import cv2
import numpy as np
cam1=cv2.VideoCapture(0)
while(1):
    ref,frame=cam1.read()
    cv2.imshow('Video Demo',frame)
    if cv2.waitKey(1) &0xff==ord('q'):
        break
