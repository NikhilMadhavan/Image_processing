import numpy as np
import cv2

cap=cv2.VideoCapture(0)
fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('output1.mp4',fourcc,20.0,(640,480))

while(True):
    ret,frame=cap.read()
    hav=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    out.write(hav)
    cv2.imshow('original',frame)
    cv2.imshow('frame',hav)
    if cv2.waitKey(2) & 0xFF==ord('q'):
        break
cap.release()
out.release()
cv2.destroyAllWindows()
