import os
import cv2
import datetime



cap=cv2.VideoCapture(r"C:\Users\acer\Desktop\yz_akademi\videos\gumball.mp4")

i=0
while(cap.isOpened()):
    
    ret,frame=cap.read()
    if ret==False:
        break
    path=r"C:\Users\acer\Desktop\yz_akademi\frames\frame"+str(i)+".jpg"
    cv2.imwrite(path,frame)
    
    i+=1
    if(i==5):
        break
    
cap.release()
cv2.destroyAllWindows()

    
    
    
    
    