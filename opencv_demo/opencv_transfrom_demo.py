import cv2 as cv
import numpy as np

img = cv.imread('resources/rsk.jpg')
print(img.shape)

#scale/resize the image to desired percentage
width = int(img.shape[0] * 20 / 100)
height = int(img.shape[1] * 20 / 100)

imgrsz = cv.resize(img, (width,height),interpolation=cv.INTER_LINEAR)
print(imgrsz.shape)

cv.imwrite('resources/rsk_resize.jpg',imgrsz)

#Traslate the image to new location using affine transformation
M = np.float32([[1,0,50],[0,1,75]])
imgtrans = cv.warpAffine(imgrsz,M,(width,height))

#rotating the image
M = cv.getRotationMatrix2D((width/2,height/2),180,1)
imgrot = cv.warpAffine(imgrsz,M,(width,height))

#affine transform
pts1 = np.float32([[50,50],[200,50],[50,200]]) #input image 3 points
pts2 = np.float32([[10,100],[200,50],[100,250]]) #output image 3 points
M = cv.getAffineTransform(pts1,pts2)
imgaff_trans = cv.warpAffine(imgrsz,M,(width,height))

#Perspective transform(zoom)
pts1 = np.float32([[80,60],[340,64],[85,345],[353,335]]) #input image 4 points
pts2 = np.float32([[0,0],[411,0],[0,421],[411,421]]) # ouput image 4 points
M = cv.getPerspectiveTransform(pts1,pts2)
imgpers_zoom = cv.warpPerspective(imgrsz,M,(width,height))

#stack the image using numpy concat so that all images can be displayed at a time
imgstack = np.concatenate((imgrsz,imgtrans,imgrot,imgaff_trans,imgpers_zoom),axis = 1)
cv.imshow('Image',imgstack)

cv.waitKey(0)
cv.destroyAllWindows()
