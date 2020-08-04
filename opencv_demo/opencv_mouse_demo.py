import cv2 as cv
import numpy as np
import random

def draw(event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONDBLCLK:
        color = 255
        #cv.circle(img,(x,y),50,(color,color,color),1)
        cv.rectangle(img,(x,y),(x+100,y+250),(0,color,0),1)


img = np.zeros((512,512,3),np.uint8)
cv.namedWindow('MouseCircle')

while True:
    cv.setMouseCallback('MouseCircle', draw)
    cv.imshow('MouseCircle', img)
    if cv.waitKey(1) == ord('q'):
        break

cv.destroyAllWindows()
