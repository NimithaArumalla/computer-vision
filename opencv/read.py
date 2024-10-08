import cv2 as cv
#image
# img=cv.imread('photos/cat.jpg')
# cv.imshow('cat',img)
# cv.waitKey(0)

#video
capture=cv.VideoCapture('videos\java name.mp4')
while True:
    isTrue,frame=capture.read()
    cv.imshow('video',frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()