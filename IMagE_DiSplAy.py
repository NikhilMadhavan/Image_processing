import cv2
import numpy
img1=cv2.imread('cropped-7680-4320-1016499.jpg');
resized=cv2.resize(img1,(1920,1080))
cv2.imshow('ZeRo_TwO',resized)
cv2.waitkey(0)
cv2.destroyAllWindows()
