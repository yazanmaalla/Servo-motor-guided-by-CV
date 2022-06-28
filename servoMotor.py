import serial
import cvzone
import math
import cv2
from cvzone.HandTrackingModule import HandDetector

sm=serial.Serial('COM8',9600)
sm.timeout=1
cap=cv2.VideoCapture(0)
cap1=cv2.VideoCapture(1)
d=HandDetector(detectionCon=0.8,maxHands=1)
while True:
    success,img=cap.read()
    success1,img1=cap1.read()    
    img=cv2.resize(img,(500,350))
    img1=cv2.resize(img1,(500,350))
    img=d.findHands(img)
    i,box=d.findPosition(img)
    if i:
        f=d.fingersUp()
        x1=i[4][0]
        y1=i[4][1]
        x2=i[8][0]
        y2=i[8][1]
        cv2.circle(img, (x1, y1), 7, (0,255,255), 2)
        cv2.circle(img, (x2, y2), 7,(255,0,255),2)
        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
        di=int( math.sqrt(math.pow(x2-x1,2)+math.pow(y2-y1,2)*1.0))
        di=int( (di/120)*255)
        d1=int( (di/200)*90)

        cv2.putText(img, "Angle:  ", (20, 30), cv2.FONT_HERSHEY_PLAIN, 3,(0, 0, 255), 1)
        cv2.putText(img, str(d1), (200, 30), cv2.FONT_HERSHEY_PLAIN, 3,(255, 100, 255), 1)
		
        e='\n'
        sm.write(str(d1).encode())
        sm.write(e.encode())
    cv2.imshow('im',img)
    cv2.imshow('im1',img1)    
    cv2.waitKey(1)
