#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2

# Get the webcam
cap = cv2.VideoCapture(0)

while True:
    
    _, frame = cap.read()

    cv2.imshow("Webcam", frame)
    
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

