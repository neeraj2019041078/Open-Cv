import cv2 as cv
capture=cv.VideoCapture('video/dog.mp4')

while True:

    istrue,frame=capture.read()

    cv.imshow("videoRead",frame)


    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
