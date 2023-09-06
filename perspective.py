import cv2
import numpy as np
img=cv2.imread(r"E:\computer vision lab\image\panda.jpg")
rimg=cv2.resize(img,(200,200))
rows,cols,_=img.shape
p1 = np.float32([[50,50],[400,95],[45,250],[350,350]])
p2 = np.float32([[100,50],[300,0],[0,300],[300,300]])
M=cv2.getPerspectiveTransform(p1,p2)
dst=cv2.warpPerspective(rimg,M,(cols,rows))
cv2.imshow("image",dst)
cv2.waitKey(0)