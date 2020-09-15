import cv2
img1=cv2.imread('cropped-7680-4320-1016499.jpg')
resizeimg1=cv2.resize(img1,(1280,720))
img2=cv2.imread('ZeRo_TwO_AnD_FraNxx.jpg')
resizeimg2=cv2.resize(img2,(1280,720))
dst1=cv2.add(resizeimg1,resizeimg2)
dst2=cv2.subtract(resizeimg1,resizeimg2)
dst3=cv2.multiply(resizeimg1,resizeimg2)
dst4=cv2.divide(resizeimg1,resizeimg2)

cv2.imshow('add',dst1)
cv2.imshow('sub',dst2)                      
cv2.imshow('mul',dst3)                      
cv2.imshow('div',dst4)

cv2.waitKey(0)
cv2.destroyAllWindows()
