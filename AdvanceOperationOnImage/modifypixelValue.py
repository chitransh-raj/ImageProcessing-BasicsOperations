import numpy as np
import cv2 as cv

img=cv.imread('9.png')
# rgb value at (100,100) location
px= img[100,100]
print(px)

# Blue location
bluepx=img[100, 100, 0]
print(bluepx)

# Changing the color values inside the pixels
img[100,100]=[255, 255, 255]
print(img[100,100])