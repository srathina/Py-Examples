import cv2 as cv

#read the image
img = cv.imread('resources/roi.jpg',cv.IMREAD_UNCHANGED)

# read and modify pixel values and its color channels
# px = img[200,200,0]
px = img.item(200,200,0)
print(f'blue pixel {px}')

# img[200,200] = [255,255,255]
px = img.itemset((200,200,0),255)

px = img[200,200,0]
print(f'blue pixel {px}')

#image shape and size
print(img.shape)
print(img.size)
print(img.dtype)

#select a region of interest (roi) and paste it in different place in same image
test = img[240:280, 350:390]
img[50:90,150:190] = test

#split the color channels and set the color channels to desired values
b = img[:,:,0]
# img[:,:,1] = 0

cv.imwrite('resources/mod_roi.jpg',img)

#make border for the image
color = [0,255,255]
constant = cv.copyMakeBorder(img,5,5,5,5,cv.BORDER_CONSTANT ,value=color)

cv.imshow('border',constant)

cv.waitKey(0)
