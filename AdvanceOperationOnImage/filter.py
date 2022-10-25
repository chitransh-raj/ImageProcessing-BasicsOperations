import numpy as np 
import cv2 as cv

img_file='9.png'
img=cv.imread(img_file)
img=cv.resize(img,(500,600))
#kernel arrat within array
#Shapning Mask
k_sharped= np.array([[-1, -1, -1],
                     [-1, 15, -1],
                     [-1, -1, -1]])
shaprened=cv.filter2D(img, -1, k_sharped)
cv.imshow('sharpened images', shaprened)
cv.imwrite('sharpenedFilter.png', shaprened)
cv.waitKey(0)
cv.destroyAllWindows()                     