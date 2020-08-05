import cv2 as cv
import time

print(cv.useOptimized())
# cv.setUseOptimized(False)

#get tickcount gives the current tick count and get tick frequency gives the number of cycles/second
# t1 = cv.getTickCount()
t1 = time.time()
img1 = cv.imread('resources/rsk.jpg')
img2 = cv.imread('resources/opencv-logo-white.png')
# t2 = cv.getTickCount()
t2 = time.time()


#below calc will be actual time for function exec. in seconds
# t = (t2-t1)/cv.getTickFrequency()
t = t2 - t1
print(f'{t} secs')


