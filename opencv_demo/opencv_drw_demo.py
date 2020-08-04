import cv2 as cv
import numpy as np

#create a array which represent image
img = np.full((512,512,3), 0, np.uint8)

# print(img)

#parameters are image name, co-ordinates, color in BGR, thickness of drawing
cv.line(img,(0,0),(511,511),(0,255,0),3)
cv.rectangle(img,(5,5),(250,250), (255,0,0),2)

#parameters are image name, center co-ordinates, radius, color in BGR, thickness of drawing
cv.circle(img,(253,253),250,(0,0,255),2)

#parameters are image name, center co-ordinates, major axis, minor axis length, rotation angle, start angle,
#end angle, color in BGR, thickness of drawing
cv.ellipse(img,(253,253),(100,50),270,0,360,(157,157,157),3)

#parameters are image name, text to be shown, font, font scale, color, thickness, line type
cv.putText(img,'RSK_OpenCV',(50,50),cv.FONT_HERSHEY_SIMPLEX,2,(255,255,255),5,cv.LINE_AA)

#show and save the image
cv.imshow("Drawing", img)
cv.imwrite("resources/Drawing.png",img)

#wait for key stroke and destroy all windows
cv.waitKey(0)
cv.destroyAllWindows()
