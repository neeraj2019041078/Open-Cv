import cv2 as cv
import numpy as np

# Load the image
img1 = cv.imread("photo/bgr.png")


img = cv.resize(img1, (500, 500))


blank = np.zeros(img.shape[:2], dtype='uint8')


mask = cv.circle(blank,(img.shape[1]//2,img.shape[0]//2), 100, (255, 255, 255), -1)

masked = cv.bitwise_and(img, img, mask=mask)

cv.imshow("Masked Image", masked)


cv.waitKey(0)
cv.destroyAllWindows()
