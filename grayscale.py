import cv2
img=cv2.imread("E:\computer vision lab\image\panda.jpg")
gs=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
a=cv2.imshow("grayscale",gs)
cv2.waitKey(0)