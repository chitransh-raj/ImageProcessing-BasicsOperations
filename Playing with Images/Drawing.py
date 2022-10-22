import cv2 

#READING AN IMAGE 
image_path=r'D:\PYTHON\openCV\Photos\flat-3252983_1280.png'  #path of image
img=cv2.imread(image_path) #reading an image

#RESIZING THE IMAGE
resize= cv2.resize(img, (500,500))

#DRAW LINE ON IMAGE

start_coord=(25,25)
end_coord=(450,300)
color=(255,0,0)
thickness=4

img=cv2.line(resize, start_coord, end_coord, color, thickness)
cv2.imshow('Line on original', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#DRAW Circle ON IMAGE

centre_point=(250,250)
radius= 100
color=(255,0,0)
thickness=4

img=cv2.circle(resize, centre_point, radius, color, thickness)
cv2.imshow('circle on original', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#DRAW Rectangle ON IMAGE

start=(250,250)
end= (350,450)
color=(0,0,0)
thickness=6

img=cv2.rectangle(resize, start, end, color, thickness)
cv2.imshow('Rectangle on original', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#DRAW Ellipse ON IMAGE

centre_coord=(120,100)
axislen=(100,50)
angle=30
startangle=0
endangle=360
color=(0,0,0)
thickness=6

img=cv2.ellipse(resize, centre_coord, axislen, angle, startangle, endangle, color, thickness)
cv2.imshow('Ellipse on original', img)
cv2.waitKey(0)
cv2.destroyAllWindows()