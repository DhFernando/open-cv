import cv2 as cv
from cv2 import FILLED
from cv2 import FONT_HERSHEY_COMPLEX
from cv2 import FONT_HERSHEY_TRIPLEX
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
# cv.imshow('blank', blank)

#1. paint the image a certain colour 
# blank[10:300, 200:450] = 0,0,255
# cv.imshow('Green', blank)

#2. Draw a Rectangle 
# cv.rectangle(blank, (50,50), (150,150), (0,255,0), thickness=cv.FILLED)
cv.rectangle(blank, (50,50), (blank.shape[0]//2,blank.shape[1]//2), (0,255,0), thickness=cv.FILLED)
# cv.imshow('Draw a Rectangle', blank)

#2. Draw a Circle
cv.circle(blank, (blank.shape[0]//2, blank.shape[1]//2), 40, (0,0,255), thickness=cv.FILLED)
# cv.imshow('Draw a Circle', blank)

#3. Draw a Line
cv.line(blank, (0,0) ,(blank.shape[0]//2, blank.shape[1]//2), (255,255,255), thickness=2)


#4. Write somthing
cv.putText(blank, 'step to machine learning', (blank.shape[1]//2 -100, blank.shape[0]//2+100), cv.FONT_HERSHEY_TRIPLEX, fontScale= 1.0, color=(0,255,0), thickness=2)
cv.imshow('My CV Drawing', blank)

cv.waitKey(0)