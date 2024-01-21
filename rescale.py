import cv2 as cv

def changesres(width,height):
    # live video

    cap.set(3,width)
    cap.set(4,height)


# def rescale(frame,scale=0.30):
#     # images videos and live videos
#     width=int(frame.shape[1]*scale)
#     height=int(frame.shape[0]*scale)
#     dimension=(width,height)

#     return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)

# // images

img=cv.imread('photo/cat.jpg')

# img1=rescale(img)

# cv.imshow("resized_image",img1)


# //vdieo

cap=cv.VideoCapture('video/dog.mp4')

while True:
    isTrue,frame=cap.read()

    frame_resized=changesres(width=4,height=5)

    cv.imshow("old_video",frame)
    cv.imshow("new_video",frame_resized)


    if cv.waitKey(20) & 0xff==ord('d'):
        break

cap.release()
cv.destroyAllWindows()

#  import cv2 as cv

# def changesres(frame, width, height):
#     # Resize the frame
#     frame_resized = cv.resize(frame, (width, height), interpolation=cv.INTER_AREA)
#     return frame_resized

# # Images
# img = cv.imread('photo/cat.jpg')
# cv.imshow("original_image", img)

# # Video
# cap = cv.VideoCapture('video/dog.mp4')

# while True:
#     isTrue, frame = cap.read()

#     # Specify the new dimensions for resizing
#     new_width, new_height = 400, 300

#     frame_resized = changesres(frame, new_width, new_height)

#     cv.imshow("original_video", frame)
#     cv.imshow("resized_video", frame_resized)

#     if cv.waitKey(20) & 0xff == ord('d'):
#         break

# cap.release()
# cv.destroyAllWindows()
