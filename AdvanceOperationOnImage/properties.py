import numpy as np 
import cv2 as cv

#reading image 
img='9.png'
#Present image  in the form of RGB color values
rgb_img=cv.imread(img, cv.IMREAD_COLOR) 
#Present image  in the form of ARGB color values
alpha_img=cv.imread(img, cv.IMREAD_UNCHANGED) 
#Present image  in the form of GRAY color values
gray_img=cv.imread(img, cv.IMREAD_GRAYSCALE)

#Imaghe SHAPE
print('RGB shape: ', rgb_img.shape)
print('ARGB shape: ', alpha_img.shape)
print('GRAY shape: ', gray_img.shape)

#Image DATATYPE
print('image datatype: ', rgb_img.dtype)
print('image datatype: ', alpha_img.dtype)
print('image datatype: ', gray_img.dtype)

#Image SIZE
print('image size: ', rgb_img.size)
print('image size: ', alpha_img.size)
print('image size: ', gray_img.size)