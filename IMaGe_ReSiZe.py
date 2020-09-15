import numpy as np
import cv2
image=cv2.imread('cropped-7680-4320-1016499.jpg');
resized=cv2.resize(image,(1920,1080))
cv2.imshow("fixed resizing",resized)
cv2.waitKey(0)
