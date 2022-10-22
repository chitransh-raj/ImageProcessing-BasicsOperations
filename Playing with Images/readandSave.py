import cv2 

#READING AN IMAGE 

image_path=r'D:\PYTHON\openCV\Photos\oldman.jpeg'  #path of image

img=cv2.imread(image_path) #reading an image

cv2.imshow('babaji', img)  #Displaying an image

#waitkey help our system to wait few seconds till any key is press to close the pop up image windoe
cv2.waitKey(0)
#all other windows will be destroyed when running destroyAllWindows() command
cv2.destroyAllWindows()

#SAVING AN IMAGE

filename='savedimage.jpeg' #saving image as
cv2.imwrite(filename, img)

#runs after image is saved
print('Job deone succesfully: Image saved')

#ACCESSING IMAGE PROPERTIES 
#output: (1104, 736, 3) which shows the property of image as (rows, columns, channel) or resoluton of image.
print(img.shape)