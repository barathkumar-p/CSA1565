import cv2
import numpy as np
img=cv2.imread(r"E:\computer vision lab\image\panda.jpg")
k=np.ones((5,5),np.uint8)
img1=cv2.dilate(img,k,iterations=1)
cv2.imshow("og",img1)
cv2.waitKey(0)