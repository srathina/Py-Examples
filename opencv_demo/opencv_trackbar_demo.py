import cv2 as cv
import numpy as np

def dummy(a):
    img[:] = [b,g,r]

#create a array which represent image
img = np.zeros((512,512,3),  np.uint8)
cv.namedWindow("Trackbar_Demo")

cv.createTrackbar('R', "Trackbar_Demo",0,255,dummy)
cv.createTrackbar('G', "Trackbar_Demo",0,255,dummy)
cv.createTrackbar('B', "Trackbar_Demo",0,255,dummy)

while True:
    r = cv.getTrackbarPos('R', "Trackbar_Demo")
    g = cv.getTrackbarPos('G', "Trackbar_Demo")
    b = cv.getTrackbarPos('B', "Trackbar_Demo")
    cv.imshow("Trackbar_Demo", img)
    if cv.waitKey(1) == ord('q'):
        break

cv.destroyAllWindows()
