import cv2 as cv
import numpy as np

img = cv.imread('resources/rsk_resize.jpg')
# img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# kernel = np.ones((5,5),np.uint8)
kernel = cv.getStructuringElement(cv.MORPH_RECT,(5,5))

# erosion, dilation, opening(erosion followed by dilation, closing(dilation followed by erosion))
# gradient - differece between erosion and dilation. so outline of image will be shown
imgerode = cv.erode(img,kernel, iterations =1)
imgdilate = cv.dilate(imgerode,kernel,iterations = 1)
imgopen = cv.morphologyEx(img,cv.MORPH_OPEN, kernel)
imgclose = cv.morphologyEx(img,cv.MORPH_CLOSE,kernel)
imggrad = cv.morphologyEx(img,cv.MORPH_GRADIENT,kernel)

imgstack = np.concatenate((img,imggrad), axis =1)
cv.imshow('Morph', imgstack)

cv.waitKey(0)
cv.destroyAllWindows()
