import numpy as np 
import cv2 as cv

#reading image 
img_file='9.png'
img=cv.imread(img_file)
#Splitting into g,b,r 3 different channel
g,b,r=cv.split(img)
cv.imshow('Green Part', g)
cv.imshow('Blue Part', b)
cv.imshow('Red Part', r)

cv.waitKey(0)
cv.destroyAllWindows()

#Merging above g,b,r images to get original image
img1=cv.merge((g,b,r))
cv.imshow('Image after Merger of the color', img1)
cv.waitKey(0)