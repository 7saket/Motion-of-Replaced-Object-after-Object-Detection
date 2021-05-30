#!/usr/bin/env python
# coding: utf-8

# In[10]:


import cv2
import time
import imutils
import numpy as np


# In[11]:


cap = cv2.VideoCapture(0)

width = 640
height = 480
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)


# In[12]:


logo_org = cv2.imread('F:\\Object Python Logo.jpg')


# In[13]:


last_time = time.time()
while True:
    
    _, frame = cap.read()

   
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    #Creating a mask based on hsv values
    #Considered values according to blue object
    mask = cv2.inRange(hsv, (110, 120, 120), (130, 255, 255))
    
    thresh = cv2.dilate(mask, None, iterations=2)
    
    contours = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)

    
    for contour in contours:
        
        if cv2.contourArea(contour) < 750:
            continue

        
        (x, y, w, h) = cv2.boundingRect(contour)
        
        size = (h + w)//2

        # Checking if logo will be inside frame
        if y + size < height and x + size < width:
            
            logo = cv2.resize(logo_org, (size, size))
            
            img2gray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
            _, logo_mask = cv2.threshold(img2gray, 1, 255, cv2.THRESH_BINARY)

            
            roi = frame[y:y+size, x:x+size]

            
            roi[np.where(logo_mask)] = 0
            roi += logo

    # Adding a FPS label to image
    text = f"FPS: {int(1 / (time.time() - last_time))}"
    last_time = time.time()
    cv2.putText(frame, text, (10, 20), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

    
    cv2.imshow("Webcam", frame)
    
    if cv2.waitKey(1) == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()

