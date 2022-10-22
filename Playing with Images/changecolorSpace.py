import cv2 

#READING AN IMAGE 
image_path=r'D:\PYTHON\openCV\Photos\my img (1).jpg'  #path of image
img=cv2.imread(image_path) #reading an image

#CHANGING COLOR-SPACE

#RGB > Gray
gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('original', img)
cv2.imshow('Gray Image', gray) #converted image
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
#Gray> RGB
org=cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
cv2.imshow('Gray Image', org) #re-contructed bavk to original image
'''