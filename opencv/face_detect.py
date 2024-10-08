import cv2 as cv

img=cv.imread('photos/group.jpg')
cv.imshow('nimitha',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

haar_cascade=cv.CascadeClassifier('haar_face.xml')
faces_rect=haar_cascade.detectMultiScale(img,scaleFactor=1.1,minNeighbors=1)
print(f'Number of faces found = {len(faces_rect)}')

for x,y,w,h in faces_rect:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,255),thickness=2)
cv.imshow('detected faces',img)
cv.waitKey(0)