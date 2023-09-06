import cv2
path=r"E:\computer vision lab\image\panda.jpg"
img=cv2.imread(path)
c=cv2.Canny(img,100,200,5)
cv2.imshow("img",c)
cv2.waitKey(0)
