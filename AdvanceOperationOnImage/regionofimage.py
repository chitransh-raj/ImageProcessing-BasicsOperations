import numpy as np 
import cv2 as cv

#reading image 
img_file='9.png'

img=cv.imread(img_file)

#selecting region of image
roi=cv.selectROI(img)
print(roi)

#Cropping slected RoI from the img
roi_crop=img[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]
cv.imshow('ROI Image', roi_crop)
cv.imwrite('cropped.jpeg', roi_crop)
cv.waitKey(0)
cv.destroyAllWindows()