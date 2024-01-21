import cv2 as cv

img=cv.imread('photo/cat.jpg')

new_width=300
new_heigh=200

img1=cv.resize(img,(new_width,new_heigh))


cv.imshow("cat",img)
cv.imshow("cat",img1)
cv.namedWindow("cat",cv.WINDOW_NORMAL)


cv.waitKey(0)