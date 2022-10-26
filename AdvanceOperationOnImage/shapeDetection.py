import numpy as np 
import cv2 as cv
from matplotlib import pyplot as plt

img=cv.imread('shapedetection.png')
gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#Setting thresholding of the gray scale

_, threshold= cv.threshold(gray, 127, 255, cv.THRESH_BINARY)

# contours usinf findcontours function

contours, _=cv.findContours(threshold, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
i=0
for contour in contours:
    if i==0:
       i=1
       continue
    appox= cv.approxPolyDP(contour, 0.01*cv.arcLength(contour, True), True)
    cv.drawContours(img, [contour], 0, (255,0,255), 5)

# Finding the centre of Different Shapes
M=cv.moments(contour)
if M['m00'] != 0.0:
    x= int(M['m10']/M['m00'])
    y= int(M['m01']/M['m00'])  

# Names of the shapes inside the corresponding shapes

if len(appox) == 3:
    cv.putText(img, 'Triangle', (x,y), cv.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 1)

elif len(appox) == 4:
    cv.putText(img, 'Quadrilateral', (x,y), cv.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 1)    

elif len(appox) == 5:
    cv.putText(img, 'Pentagon', (x,y), cv.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 1)  

else: 
    cv.putText(img, 'Circle', (x,y), cv.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 1)       

#Displaying

cv.imshow('Shapes', img)
cv.waitKey(0)
cv.destroyAllWindows()