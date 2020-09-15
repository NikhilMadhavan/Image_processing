import numpy as np
import cv2
image=cv2.imread('cropped-7680-4320-1016499.jpg');
resized=cv2.resize(image,(1920,1080))
gray_image=cv2.cvtColor(resized,cv2.COLOR_BGR2HSV)
cv2.imshow('gray_image',gray_image)
#nocmd