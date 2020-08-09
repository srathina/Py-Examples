import cv2 as cv
import numpy as np

img = cv.imread('resources/rsk_resize.jpg')

#higher resolution to low resolution and vice versa
imgpyrdn = cv.pyrDown(img)
imgpyrup = cv.pyrUp(imgpyrdn)


imgstack = np.concatenate((imgpyrup1,imgpyrup1),axis=1)
cv.imshow('Pyramid-Demo', imgstack)

cv.waitKey(0)
cv.destroyAllWindows()