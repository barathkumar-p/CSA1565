import cv2
import numpy as np
img = cv2.imread(r"E:\computer vision lab\image\panda.jpg")
img1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img1 = np.float32(img1)
img2 = cv2.cornerHarris(img1,2,5,0.07)
img2 = cv2.dilate(img2,None)
img[img2 > 0.01 * img2.max()]=[0,0,255]
cv2.imshow("original image",img)
cv2.waitKey(0)