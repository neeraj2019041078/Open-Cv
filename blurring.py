import cv2 as cv
import numpy as np

# Read the image
img1 = cv.imread("photo/bgr.png")
img = cv.resize(img1, (500, 500))

# Apply Average Blur
average_blur = cv.blur(img, (5, 5))

# Apply Median Blur
median_blur = cv.medianBlur(img, 5)

# Apply Gaussian Blur
gaussian_blur = cv.GaussianBlur(img, (5, 5), 0)

# Display the original and blurred images
# cv.imshow("Original Image", img)
# cv.imshow("Average Blur", average_blur)
# cv.imshow("Median Blur", median_blur)
# cv.imshow("Gaussian Blur", gaussian_blur)
blank=np.zeros([500,500,3],dtype='uint8')


cv.waitKey(0)
cv.destroyAllWindows()
