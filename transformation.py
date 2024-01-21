import cv2 as cv
import numpy as np

img=cv.imread("photo/cat.jpg")
img1=cv.resize(img,(500,500))
cv.imshow("hello",img1)


# def translate(img,x,y):
#     translateMat=np.float32([[1,0,x],[0,1,y]])
#     dimension=(img.shape[1],img.shape[0])

#     return cv.warpAffine(img,translateMat,dimension)



# img2 = cv.resize(img, (500,500))
# img3=translate(img2,100,200)


# cv.imshow("translated imgae",img3)

# rotate image

angle=45

rotateImage=cv.getRotationMatrix2D((img1.shape[1]/2,img1.shape[0]/2),angle,-1)


roate=cv.warpAffine(img1,rotateImage,(500,500))


# flip image 

# img4=cv.flip(roate,0)
# cv.imshow("roatate",img4)




cv.waitKey(0)