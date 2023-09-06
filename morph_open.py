import cv2
import numpy as np
img=cv2.imread(r"E:\computer vision lab\image\panda.jpg")
cv2.imshow("og",img)
kernel=np.ones((6,6),np.uint8)
opening=cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
closing=cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)
gradient=cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)
tophat=cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel)
blackhat=cv2.morphologyEx(img,cv2.MORPH_BLACKHAT,kernel)
cv2.imshow("image",opening)
cv2.imshow("image1",closing)
cv2.imshow("image4",gradient)
cv2.imshow("image2",tophat)
cv2.imshow("image3",blackhat)
cv2.waitKey(0)