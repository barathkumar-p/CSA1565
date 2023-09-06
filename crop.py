import cv2
img = cv2.imread(r"E:\computer vision lab\image\panda.jpg")
a= [100:300,200:300]
roi = img[a[0]:a[1], a[2]:a[3]]
img1 = cv2.imread('E:\computer vision lab\image\panda1.jpg')
b = [50, 50]
img1[b[0]:b[0] + roi.shape[0], b[1]:b[1] + roi.shape[1]] = roi
cv2.imwrite('E:\computer vision lab\image\outputpanda.jpg', img1)
cv2.imshow('og', img1)
cv2.waitKey(0)
