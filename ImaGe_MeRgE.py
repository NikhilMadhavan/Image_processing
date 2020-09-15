import cv2
img1=cv2.imread('cropped-7680-4320-1016499.jpg')
resizeimg1=cv2.resize(img1,(1920,1080))
img2=cv2.imread('ZeRo_TwO_AnD_FraNxx.jpg')
resizeimg2=cv2.resize(img2,(1920,1080))
dst=cv2.addWeighted(resizeimg1,0.8,resizeimg2,0.2,0)
cv2.imshow('dst',dst)
