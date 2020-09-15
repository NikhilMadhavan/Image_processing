import cv2

img=cv2.imread('cropped-7680-4320-1016499.jpg',0)
resized=cv2.resize(img,(1920,1080))
edges=cv2.Canny(resized,100,200)
cv2.imshow('yo',edges)
