import cv2 as cv
import numpy as np


color = (255,255,255)

img = cv.imread('resources/rsk_resize.jpg')
img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

imgCanny = cv.Canny(img,100,200)
cv.putText(imgCanny,'Canny',(50,50),cv.FONT_HERSHEY_SIMPLEX,1,color,2,cv.LINE_AA)

cv.putText(img,'Original',(50,50),cv.FONT_HERSHEY_SIMPLEX,1,color,2,cv.LINE_AA)

imgstack = np.concatenate((img,imgCanny),axis=1)
cv.imshow('Canny-Demo', imgstack)

cv.waitKey(0)
cv.destroyAllWindows()