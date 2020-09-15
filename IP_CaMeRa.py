import urllib.request
import cv2
import numpy as np

url="http://192.168.0.103:8080/shot.jpg"
while True:
    imgpath=urllib.request.urlopen(url)
    imgNp=np.array(bytearray(imgpath.read()),dtype=np.uint8)
    img=cv2.imdecode(imgNp,-1)
    cv2.imshow('frame',img)
    k=cv2.waitKey(1) & 0xFF 
    if k==ord('q'):
        cv2.imwrite('frame.jpg',img)
