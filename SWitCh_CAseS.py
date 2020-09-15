import numpy as np
import cv2
for i in range(1,5):
    cndn=int(input('enter the operation'))


    if (cndn==1):
        image=cv2.imread('cropped-7680-4320-1016499.jpg');
        resized=cv2.resize(image,(1920,1080))
        gray_image=cv2.cvtColor(resized,cv2.COLOR_BGR2GRAY)
        cv2.imshow('gray_image',gray_image)
        cv2.imwrite('ZeRo_TwO_GraYScalE.jpg',gray_image);

    elif (cndn==2): 
        image=cv2.imread('cropped-7680-4320-1016499.jpg');
        resized=cv2.resize(image,(1920,1080))
        hsv_image=cv2.cvtColor(resized,cv2.COLOR_BGR2HSV)
        cv2.imshow('hsv_image',hsv_image)

    elif (cndn==3):
        img=cv2.imread('cropped-7680-4320-1016499.jpg',0)
        resized=cv2.resize(img,(1920,1080))
        edges=cv2.Canny(resized,100,200)
        cv2.imshow('yo',edges)
    else:
        print('SAD YOU WILL NOT SEE ZeRo_TwO TODAY!!!')
