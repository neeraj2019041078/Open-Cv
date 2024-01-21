import cv2 as cv

def rescale(frame,scale=0.3):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimension=(width,height)

    return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)
img=cv.imread("photo/cat.jpg")

resized_image=rescale(img)

# coverting image to gray
# gray=cv.cvtColor(resized_image,cv.COLOR_BGR2GRAY)

# blur
# blur=cv.GaussianBlur(resized_image,(8),cv.BORDER_DEFAULT)

#canny
canny=cv.Canny(resized_image,150,250)

cv.imshow("gray",canny)

cv.waitKey(0)

