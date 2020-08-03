import cv2 as cv

#call the video capture method
cap = cv.VideoCapture(0)

#define codec
fourcc = cv.VideoWriter_fourcc(*'DIVX')
#Provision the video writer and the parameters are output file name, codec details, fps, frame size
out = cv.VideoWriter('resources/output.avi', fourcc, 30.0, (640,  480))

#check camera is opened
if not cap.isOpened():
    exit()

#grab the frame until key press or error
while True:
    ret, frame = cap.read()

    if not ret:
        print("cannot read image")
        break

    #Display and save the frame until user press the q button
    out.write(frame)
    cv.imshow('Display_video', frame)

    #capture the last frame as an image file
    cv.imwrite('resources/Image_capture_demo.png', frame)

    if cv.waitKey(1) == ord('q'):
        break





#release and destroy all the resources and windows
cap.release()
out.release()
cv.destroyAllWindows()
