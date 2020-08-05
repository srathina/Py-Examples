import cv2 as cv


img1 = cv.imread('resources/rsk.jpg')
img2 = cv.imread('resources/opencv-logo-white.png')

cv.namedWindow("Blend", cv.WINDOW_NORMAL)

print(img1.shape)
print(img2.shape)

#image blending
# finalImage = cv.addWeighted(img1,0.7,img2,0.3,0)

#image addition
# finalImage = img1+img2

#image bitwise operation
rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]

#create a mask for the selected region
img2gry = cv.cvtColor(img2,cv.COLOR_BGR2GRAY)
ret, mask = cv.threshold(img2gry,10,255,cv.THRESH_BINARY)
inv_mask = cv.bitwise_not(mask)

#now blend the images using mask
img1bg = cv.bitwise_and(roi,roi,mask=inv_mask)
img2fg = cv.bitwise_and(img2,img2,mask=mask)

dst = cv.add(img1bg,img2fg)
img1[0:rows, 0:cols] = dst

cv.imshow('Blend', img1)

cv.waitKey(0)

cv.destroyAllWindows()
