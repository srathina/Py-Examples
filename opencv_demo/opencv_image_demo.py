import cv2 as cv
import sys

#read the image in gray scale
img = cv.imread('resources/rsk.jpg',cv.IMREAD_GRAYSCALE)

# report if the image is not loaded
if img is None:
    sys.exit('Image not found')

#Show the image
cv.imshow("Display_Image", img)

#wait until the key press
cv.waitKey(0)
