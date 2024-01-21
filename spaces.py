import cv2

# Read the image
img1 = cv2.imread("photo/cat.jpg")
img = cv2.resize(img1, (500, 500))

# BGR to Gray
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image", gray_img)

# BGR to HSV
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV Image", hsv_img)


# BGR to LAB
lab_img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
cv2.imshow("LAB Image", lab_img)


# BGR to RGB
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow("RGB Image", rgb_img)


# Reverse conversions

# Gray to BGR
bgr_from_gray = cv2.cvtColor(gray_img, cv2.COLOR_GRAY2BGR)
cv2.imshow("BGR from Gray", bgr_from_gray)


# HSV to BGR
bgr_from_hsv = cv2.cvtColor(hsv_img, cv2.COLOR_HSV2BGR)
cv2.imshow("BGR from HSV", bgr_from_hsv)


# LAB to BGR
bgr_from_lab = cv2.cvtColor(lab_img, cv2.COLOR_LAB2BGR)
cv2.imshow("BGR from LAB", bgr_from_lab)


# RGB to BGR
rgb=cv2.cvtColor(rgb_img,cv2.COLOR_RGB2BGR)
cv2.imshow("BGR from LAB", rgb)
