import cv2 as cv
import numpy as np

frame = cv.imread('resources/Drawing.png')

#conver bgr to hsv
hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)

# define range of blue color in HSV
lower_blue = np.array([120,255,255])
upper_blue = np.array([120,255,255])

# define range of red color in HSV
lower_red = np.array([0,255,255])
upper_red = np.array([0,255,255])

# define range of red color in HSV
lower_green = np.array([60,255,255])
upper_green = np.array([60,255,255])


mask_blue = cv.inRange(hsv,lower_blue,upper_blue)
mask_red = cv.inRange(hsv,lower_red,upper_red)
mask_green = cv.inRange(hsv,lower_green,upper_green)

mask = mask_blue | mask_red | mask_green
inv_mask = cv.bitwise_not(mask)

res = cv.bitwise_and(frame,frame,mask = mask)

imgstack = np.concatenate((frame,res),axis = 1)
cv.imshow('Image',imgstack)


cv.waitKey(0)

cv.destroyAllWindows()

#formula on how to find hsv of any color
blue = np.uint8([[[255,0,0]]]) #BGR color space image
hsv_blue = cv.cvtColor(blue,cv.COLOR_BGR2HSV)
print(hsv_blue)

red = np.uint8([[[0,0,255]]]) #BGR color space image
hsv_red = cv.cvtColor(red,cv.COLOR_BGR2HSV)
print(hsv_red)

green = np.uint8([[[0,255,0]]]) #BGR color space image
hsv_green = cv.cvtColor(green,cv.COLOR_BGR2HSV)
print(hsv_green)
