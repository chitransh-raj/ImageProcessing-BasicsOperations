import cv2 

#READING AN IMAGE 
image_path=r'D:\PYTHON\openCV\Photos\my img (1).jpg'  #path of image
img=cv2.imread(image_path) #reading an image

#RESIZING THE IMAGE
resize= cv2.resize(img, (500,500))

#DISPLAYING TEXT OVER IMAGE 

#variables
text="Chitransh Raj as Anime Image"
coordinates=(25,350)
font=cv2.FONT_HERSHEY_SCRIPT_COMPLEX
fontsize=1
color=(255,0,0)
thickness=1

img=cv2.putText(resize, text, coordinates, font, fontsize, color, thickness)

cv2.imshow('Text on original', img)
cv2.waitKey(0)
cv2.destroyAllWindows()