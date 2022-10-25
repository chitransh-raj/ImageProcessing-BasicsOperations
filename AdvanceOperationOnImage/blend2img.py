import numpy as np 
import cv2 as cv

#Taking two images
source1= cv.imread('9.png', cv.IMREAD_COLOR)
source2= cv.imread('8.png', cv.IMREAD_COLOR)

#Converting Images into same resolution
img1=cv.resize(source1,(500,600))
img2=cv.resize(source2,(500,600))

#Blending both images
blend_img=cv.addWeighted(img1,1, img2, 0.5, 0.0)
cv.imshow('Blended images', blend_img)
cv.imwrite('blended.png', blend_img)
cv.waitKey(0)
cv.destroyAllWindows()