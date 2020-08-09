import cv2 as cv
import numpy as np

img = cv.imread('resources/image_capture_demo.png')

#apply gray, blur and edge detection for better contour draw.
#contour is baiscally find white object from black background
imggray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
imgGaublur = cv.GaussianBlur(imggray,(5,5),0)
imgCanny = cv.Canny(imgGaublur,127,255,0)

#find x,y co-ordinates of contours and draw contours in the choosen color.
contours,imgContour = cv.findContours(imgCanny,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
print(len(contours))
imgDrawCont = cv.drawContours(img, contours, -1, (0,255,255), 2)

cv.imshow('Contours-Demo', imgDrawCont)

cv.waitKey(0)
cv.destroyAllWindows()