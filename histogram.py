
# import cv2 as cv
# import numpy as np
# import matplotlib.pyplot as plt

# img = cv.imread("photo/bgr.png")
# img = cv.resize(img, (500, 500))

# # # Convert the image to grayscale
# # # gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# blank=np.zeros((500,500),dtype='uint8')

# # Create a mask (e.g., for a specific region in the grayscale image)
# # mask = cv.inRange(gray, 0,100)  # Example: masking pixel values between 100 and 255

# # Compute and display the histogram for the masked region
# hist_masked = cv.calcHist([blank], [0], None, [256], [0, 256])
# plt.plot(hist_masked)
# plt.xlabel("number of bins")
# plt.ylabel("intensity")
# plt.title("Histogram with Mask")
# plt.show()


# // color histogram



# cv.imshow("masked image",masked)
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("photo/bgr.png")
img = cv.resize(img, (500, 500))

# Create a blank image for the mask
blank = np.zeros((500, 500), dtype='uint8')

# Create a circular mask
circle = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, (255, 255, 255), -1)

# Apply the mask to the image
masked = cv.bitwise_and(img, img, mask=circle)

plt.figure()
plt.title('Color Histogram')
plt.xlabel("Bins")
plt.ylabel("# Intensity")

colors = ('b', 'g', 'r')

for i, col in enumerate(colors):
    # Convert the mask to CV_8UC1 if needed
    mask_for_calcHist = np.uint8(circle)
    
    # Calculate and plot the histogram
    hist_plot = cv.calcHist([img], [i], mask_for_calcHist, [256], [0, 256])
    plt.plot(hist_plot, color=col)

plt.show()

cv.imshow("Circle", circle)
cv.waitKey(0)

