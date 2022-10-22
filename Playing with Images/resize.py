import cv2 

#READING AN IMAGE 
image_path=r'D:\PYTHON\openCV\Photos\my img (1).jpg'  #path of image
img=cv2.imread(image_path) #reading an image


#ACCESSING IMAGE PROPERTIES 
#getting the resoluton of image of original image
print(img.shape)

#RESIZING THE IMAGE
resize= cv2.resize(img, (400,400))
cv2.imshow('original', img)
cv2.imshow('resize Image', resize) #converted image
cv2.waitKey(0)
cv2.destroyAllWindows()