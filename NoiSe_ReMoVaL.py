import cv2
img=cv2.imread('ZeRo_TwO_AnD_FraNxx.jpg')
resized=cv2.resize(img,(1920,1080))
dst=cv2.medianBlur(resized,5)
cv2.imshow('noise',dst)
