import cv2 as cv
import numpy as np

# Load the image using OpenCV
img = cv.imread("photo/bgr.png")

# Resize the image if needed
img = cv.resize(img, (500, 500))

# Convert the image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Sobel Edge Detection
sobel_x = cv.Sobel(gray, cv.CV_64F, 1, 0, ksize=5)
sobel_y = cv.Sobel(gray, cv.CV_64F, 0, 1, ksize=5)
magnitude_sobel = np.sqrt(sobel_x**2 + sobel_y**2)

# Canny Edge Detection
edges_canny = cv.Canny(gray, 100, 200)

# Laplacian Edge Detection
laplacian = cv.Laplacian(gray, cv.CV_64F)

# Display the original image and edges
cv.imshow("Original Image", img)
cv.imshow("Sobel X", cv.convertScaleAbs(sobel_x))
cv.imshow("Sobel Y", cv.convertScaleAbs(sobel_y))
cv.imshow("Sobel Magnitude", cv.convertScaleAbs(magnitude_sobel))
cv.imshow("Canny Edges", edges_canny)
cv.imshow("Laplacian Edges", cv.convertScaleAbs(laplacian))

cv.waitKey(0)
cv.destroyAllWindows()