#Import all the libraries
import pyautogui as p
import cv2 as c
import numpy as np

#Create resolution
res = p.size()

#filename in which we store recording
file_name = 'D:/Image_processing/recording.mp4'

#Fix the frame rate
fps = 25.0
fourcc = c.VideoWriter_fourcc(*'XVID')
output = c.VideoWriter(file_name,fourcc,fps,res)

#create recording module
c.namedWindow("Live_Recording",c.WINDOW_NORMAL)

#Resize the window
c.resizeWindow("Live_Recording",(600,400))
while True:
    img = p.screenshot() #image
    f = np.array(img) #convert image into array
    f = c.cvtColor(f,c.COLOR_BGR2RGB)
    output.write(f)
    c.imshow("screenshot", f)
    if c.waitKey(1) == ord("q"):
        break
c.destroyAllWindows()
output.release()  
