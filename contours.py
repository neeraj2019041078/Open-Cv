# import cv2 as cv
# import numpy as np
# img=cv.imread("photo/cat.jpg")

# gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# gray1=cv.resize(gray,(500,500))
# # cv.imshow("gray_image",gray1)

# blank=np.zeros((500,500,3),dtype='uint8')
# cv.imshow("blank image",blank)

# blur=cv.GaussianBlur(gray1,(3,3),cv.BORDER_DEFAULT)
# cv.imshow("blur image",blur)

# # edges=cv.Canny(blur,125,200)
# # cv.imshow("edges detect",edges)
# # # img_copy=gray1.copy()


# ret,thresh=cv.threshold(blur,125,255,cv.THRESH_BINARY)
# # cv.imshow("thresh image",thresh)

# contours,hierarchies=cv.findContours(blur,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
# # print(f'{len(contours)}')

# img4=cv.drawContours(blank,thresh,-1,(0,0,255),1)

# cv.imshow("draw contour",img4)
# # img2=cv.drawContours(img_copy,contours,-1,(0,255,0),5)
# # cv.imshow("contours image",img2)
# # print(contours)
# # cv.waitKey(0)

import cv2 as cv
import numpy as np

img = cv.imread("photo/cat.jpg")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

gray_resized = cv.resize(gray, (500, 500))

blank = np.zeros((500, 500, 3), dtype='uint8')

blur = cv.GaussianBlur(gray_resized, (3, 3), cv.BORDER_DEFAULT)

ret, thresh = cv.threshold(blur, 125, 255, cv.THRESH_BINARY)

contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

img_with_contours = cv.drawContours(blank, contours, -1, (0, 0, 255), 1)

cv.imshow("Draw Contours", img_with_contours)

cv.waitKey(0)
cv.destroyAllWindows()
