#Modules 
import cv2
import random 
import time 
import dropbox
startTime = time.time()
def takeSnapshots():
    #generate random #
    num = random.randint(0,100)

    #initializing cv2
    videoCaptureObj = cv2.VideoCapture(0)
    result = True

    while(result): 
        #read the frames while the camera is on
        ret,frame = videoCaptureObj.read()    

        #cv2.imwrite(fileName, image) method is used to save an image to any storage device
        imageName = "img"+str(num)+".png"
        cv2.imwrite(imageName, frame)

        startTime = time.time
        result = False        

    return imageName

    print('Picture has been Clicked')

    #release the camera
    videoCaptureObj.release()

    #close all the windows that might be opened while this process
    cv2.destroyAllWindows()


def UploadFile(imageName):
    access_token = 'oqUU21S1GIkAAAAAAAAAAb3VDjO39HBwFZUExli4XSU4WBK1TLe4uA3pSyFLdVHB'

    file_from = imageName
    file_to = '/Dropbox/Class102/'+(imageName)
  
    dbx = dropbox.Dropbox(access_token)

    with open(file_from,"rb") as f:
        dbx.files_upload(f.read(), file_to, dropbox.files.WriteMode.overwrite)
        print("file uploaded")

def main():
    while (True):
        if ((time.time()-startTime) >= 5):
            name = takeSnapshots()
            UploadFile(name)


main()