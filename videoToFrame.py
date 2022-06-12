import os
import cv2



pathVideos=r"C:\Users\acer\Desktop\yz_akademi\videos"
videos=os.listdir(pathVideos)

i=1
for video in videos:
    
    cap=cv2.VideoCapture(pathVideos+"\\"+video)
    
    if(cap.isOpened() == False):
        print("Error Opening Video Stream Or File")
    
    while(cap.isOpened()):
        # Capture frame-by-frame
        ret, frame =cap.read()
        
        cv2.imwrite(r"C:\Users\acer\Desktop\yz_akademi\frames\frame"+str(i)+".jpg",frame)
              
        i+= 1 # Advance file counter
                
        if i%5==0:
            break
    
  

cap.release()
cv2.destroyAllWindows()