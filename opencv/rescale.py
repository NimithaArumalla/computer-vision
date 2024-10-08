import cv2 as cv

img=cv.imread('photos/cat.jpg')
#for standalone videos
def rescale(frame,scale=0.15):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)
#for webcam
def changeRes(width,height):
    capture.set(3,width)
    capture.set(4,height)
resized_image=rescale(img)
cv.imshow('cat',resized_image)

capture=cv.VideoCapture('videos\java name.mp4')
while True:
    isTrue,frame=capture.read()
    frame_resized=rescale(frame,scale=0.2)
    cv.imshow('video resized',frame_resized)
    cv.imshow('video',frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()
cv.waitKey(0)