import cv2
img=cv2.imread(r"E:\computer vision lab\image\panda.jpg")
res=cv2.rotate(img,cv2.ROTATE_180)
cv2.imshow("rotated img",res)
cv2.waitKey(0)