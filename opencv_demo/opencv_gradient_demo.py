import cv2 as cv
import numpy as np


color = (0,0,0)

img = cv.imread('resources/rsk_resize.jpg')
img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

imglapl = cv.Laplacian(img,cv.CV_64F)
cv.putText(imglapl,'Laplacian',(50,50),cv.FONT_HERSHEY_SIMPLEX,2,color,4,cv.LINE_AA)

imgsobel = cv.Sobel(img,cv.CV_64F,1,0,5)
cv.putText(imgsobel,'Sobel',(50,50),cv.FONT_HERSHEY_SIMPLEX,2,color,4,cv.LINE_AA)

imgscharr = cv.Scharr(img,cv.CV_64F,0,1)
cv.putText(imgscharr,'Scharr',(50,50),cv.FONT_HERSHEY_SIMPLEX,2,color,4,cv.LINE_AA)

cv.putText(img,'Original',(50,50),cv.FONT_HERSHEY_SIMPLEX,2,color,4,cv.LINE_AA)

imgstack = np.concatenate((img,imglapl,imgsobel,imgscharr),axis=1)
cv.imshow('Gradient-Demo', imgstack)

cv.waitKey(0)
cv.destroyAllWindows()