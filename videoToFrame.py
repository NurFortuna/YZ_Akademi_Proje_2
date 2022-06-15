import os
import cv2


def createFolder(count,parent_dir=r"C:\Users\acer\Desktop\yz_akademi\frames"):
    
    # Parent Directory path
    #parent_dir=r"C:\Users\acer\Desktop\yz_akademi\frames"
   
    # Directory
    directory = "frame"+str(count)
   
    # Path for frame
    path = os.path.join(parent_dir, directory)
    os.mkdir(path)
    
    return path


def video_to_frame(pathVideos=r"C:\Users\acer\Desktop\yz_akademi\videos"):
   
    folder_count=0
    frame_count=0
    
    #Get the list of all videos
    videos=os.listdir(pathVideos)
    
    #create new folder
    folder_path=createFolder(folder_count)
    
    for video in videos:
        
        #Create a video capture object
        #we are reading the video
        cap=cv2.VideoCapture(pathVideos+"\\"+video)
        
        # Check if camera opened successfully
        if(cap.isOpened() == False):
            print("Error Opening Video Stream Or File")
        
        while(cap.isOpened()):
            
            # Capture frame-by-frame
            ret, frame =cap.read()
            
            # if frame is read correctly ret is True
            if ret:
                frame_count+= 1
                
                # Saving the image
                cv2.imwrite(folder_path+"\\"+str(frame_count)+".jpg",frame)
                
                    
                #for every 50 frames is created a new folder
                
                if frame_count%50==0:
                    folder_count+=1 
                    folder_path=createFolder(folder_count)    
                    
            # Break the loop
            else:
                break
    
    # When everything done, release the video capture object                
    cap.release()
    
    
video_to_frame()

