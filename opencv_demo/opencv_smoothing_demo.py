import cv2 as cv
import numpy as np

img = cv.imread('resources/rsk_resize.jpg')

#filter for smoothen it.
kernel = np.ones((5,5),np.float32)/25

#filter for edge detection
# kernel = np.array([[0.0, -1.0, 0.0],
#                    [-1.0, 4.0, -1.0],
#                    [0.0, -1.0, 0.0]])
# kernel = kernel/(np.sum(kernel) if np.sum(kernel)!=0 else 1)

imgfilter = cv.filter2D(img,-1,kernel)

#blur the image for removing noises
# imgBoxblur = cv.boxFilter(img,-1,ksize=(5,5))
imgBblur = cv.blur(img,(5,5))
imgGaublur = cv.GaussianBlur(img,(5,5),0)
imgmedblur = cv.medianBlur(img,5)
imgbilatfilt = cv.bilateralFilter(img,9,75,75)

imgstack = np.concatenate((img,imgbilatfilt,imgGaublur),axis=1)
cv.imshow('Smooth',imgstack)

cv.waitKey(0)
cv.destroyAllWindows()
