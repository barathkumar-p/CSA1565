import cv2
img=cv2.imread("E:\computer vision lab\image\panda.jpg")
cv2.imshow("og",img)
gs=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gb=cv2.GaussianBlur(gs,(9,9),0)
cv2.imshow("grayscale",gs)
cv2.waitKey(0)