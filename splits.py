import cv2 as cv 
import numpy as np 

img1=cv.imread("photo/bgr.png")
img=cv.resize(img1,(500,500))
# cv.imshow("hello",img)

blank=np.zeros((500,500,3),dtype='uint8')



b,g,r=cv.split(img)
# cv.imshow("orginal image",img)
# cv.imshow("blue",b)
# cv.imshow("green",g)
# cv.imshow("red",r)


# rgb=cv.merge([b,g,r])
# cv.imshow("orignal image comes",rgb)
zeros = np.zeros_like(b)


blueimage=cv.merge([b,zeros,zeros])
cv.imshow("blacnkblue",blueimage)

cv.waitKey(0)
