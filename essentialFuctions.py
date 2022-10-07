import cv2 as cv
from cv2 import resize

#rescale
def rescaleFrame(frame, scale = 0.05):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimention = (width, height)
    return cv.resize(frame, dimention, interpolation=cv.INTER_AREA)

img = rescaleFrame(cv.imread('SRCFile/Photos/1.jpg'))
cv.imshow('original', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('blur', blur)

canny = cv.Canny(img, 125, 175)
cv.imshow('canny', canny)

resized = cv.resize(img, (250, 250), interpolation=cv.INTER_AREA)
cv.imshow('resized', resized)

cv.waitKey(0)