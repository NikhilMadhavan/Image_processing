import cv2
from matplotlib import pyplot as plt

img=cv2.imread('cropped-7680-4320-1016499.jpg',0)
histr=cv2.calcHist([img],[0],None,[256],[0,256])
plt.plot(histr)
plt.show()

