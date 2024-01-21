import cv2 as cv
import numpy as np


blank=np.zeros((500,500,3),dtype='uint8')
cv.imshow("blank",blank)

# specific place
# blank[200:300,400:500]=0,255,0


# Draw a rectangle
# cv.rectangle(blank,(0,0),(250,500),(0,255,0),thickness=-1)
# mehod 2
# cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,255,0),thickness=cv.FILLED)

# if thick -2

# draw circle
# cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,0,255),thickness=-1)

# draw a line
# cv.line(blank,(0,0),(255,255),(255,0,0),thickness=5)

# Text on an image
text="hello brother"
cv.putText(blank,text,(255,255),cv.FONT_HERSHEY_PLAIN,1.2,(0,255,0),thickness=5)


cv.imshow("blank",blank)

cv.waitKey(0)
