import cv2 as cv
img=cv.imread('photos/pp.jpg')
cv.imshow('cat',img)

# #converting color to gray scale image
# gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('gray',gray)

# #blur images
# blur=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
# cv.imshow('blur',blur)

# #edge detecgtion
canny=cv.Canny(img,125,175)
cv.imshow('canny',canny)
#dilation
dilated=cv.dilate(canny,(7,7),iterations=3)
cv.imshow('dilate',dilated)

#erode
erode=cv.erode(dilated,(7,7),iterations=3)
cv.imshow('eroded',erode)

#resize
resized=cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('resized',resized)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)
cv.waitKey(0)