import cv2 as cv
import sys

#read the image
img = cv.imread('resources/rsk.jpg',cv.IMREAD_UNCHANGED)

# report if the image is not loaded
if img is None:
    sys.exit('Image not found')

#conver to grey scale
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#it is possible to resize the window before even showing the image
cv.namedWindow("Display_Image", cv.WINDOW_NORMAL)

#Show the image
cv.imshow("Display_Image", img)

#save the image
cv.imwrite('resources/rsk_grey.png',img)

#wait until the key press
cv.waitKey(0)

#destroy all windows
cv.destroyAllWindows()
