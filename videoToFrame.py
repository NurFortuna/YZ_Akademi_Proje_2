
import os
import cv2

def create_folder(dirName):
    
    #Check path exists or not
    if not os.path.exists(dirName):
        os.mkdir(dirName)
        print("Created ")
    else:    
        print("already exists")

    return dirName

def save_frames_and_create_new_folder_per_fifty(pathVideos, pathFrames):
    
    #counter for the number of frames and number of folders
    count = 0
    #Get the list of all videos
    videos = os.listdir(pathVideos)
    
    os.mkdir(pathFrames+"\\"+str(count))
    folder_path = pathFrames+"\\"+str(count)
    #Check path exists or not
    if not os.path.exists(pathFrames+"\\"+str(count)):
        print("Folder is not exists")
   
    for video in videos:
        cap = cv2.VideoCapture(pathVideos+"\\"+video)
        # Check if camera opened successfully
        if(cap.isOpened() == False):
            print("Error Opening Video Stream Or File")
        
        while(cap.isOpened()):
            ret, frame = cap.read()
            if ret:
                count += 1    
                #Save the image to folder_path
                cv2.imwrite(folder_path+"\\"+str(count)+".jpg",frame)
                
                if count%50 == 0:
                    #new folder is created for every 50 frames
                    os.mkdir(pathFrames+"\\"+str(count))
                    folder_path = pathFrames+"\\"+str(count)
                    #Check path exists or not
                    if not os.path.exists(pathFrames+"\\"+str(count)):
                        print("Folder is not exists")
                        break 
            else:
                break  
    #When everything done, release the video capture object 
    cap.release()
   

if __name__ == '__main__':
    path = r"C:\Users\acer\Desktop\yz_akademi"
    pathVideos = r"C:\Users\acer\Desktop\yz_akademi\videos"
    frames = create_folder("frames") 
    pathFrames = path + "\\" + frames
    print(save_frames_and_create_new_folder_per_fifty(pathVideos, pathFrames))
    
    
