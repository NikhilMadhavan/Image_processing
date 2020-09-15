import cv2
import numpy as np
cam1=cv2.VideoCapture(0)
while(1):
    ref,frame=cam1.read()
    cv2.imshow('Video Demo',frame)
    gray_image=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray_frame',gray_image)
    hsv_image=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    cv2.imshow('gray_image',hsv_image)
    edges=cv2.Canny(frame,150,250)
    cv2.imshow('yo',edges)
    if cv2.waitKey(1) &0xff==ord('q'):
        break
