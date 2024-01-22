import cv2 as cv

img=cv.imread('photo/many.jpg')
cv.imshow("person",img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)

haar_caascade=cv.CascadeClassifier('haar_face.xml')
faces_rect=haar_caascade.detectMultiScale(gray,
                                          1.1,4)

print(f'Number of face ={len(faces_rect)}')

for x,y,w,h in faces_rect:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)

cv.namedWindow("faces detected",cv.WINDOW_NORMAL)
cv.imshow("faces detected",img)


cv.waitKey(0)