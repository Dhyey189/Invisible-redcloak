import numpy as np
import cv2 as cv
import imutils

captureImage = cv.VideoCapture(0,cv.CAP_DSHOW)
Image = cv.imread('./Image.jpg')
kernel = np.ones((5,5), np.uint8)

while captureImage.isOpened():
    ret , frame = captureImage.read()

    if ret:
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

        red =np.uint8([[[0,0,240]]])

        hsv_red =cv.cvtColor(red, cv.COLOR_BGR2HSV)
        l_red = np.array([0,100,100])
        u_red = np.array([10,255,255])

        mask = cv.inRange(hsv, l_red, u_red)
        # mask = cv.imshow("mask",mask)

        part1 = cv.bitwise_and(Image,Image, mask=mask)
        # cv.imshow('part1',part1)

        mask =cv.bitwise_not(mask)

        part2 = cv.bitwise_and(frame,frame, mask=mask)
        # cv.imshow('part2',part2)
        cv.imshow("cloak", part1 + part2)
        # back = frame
        # img_erosion = cv.erode(back, kernel, iterations=1) 
        # img_dilation = cv.dilate(back, kernel, iterations=1)
        
        
        # cv.imshow('Input', back) 
        
        # cv.imshow('Dilation', img_dilation) 
        # cv.imshow('Erosion', img_erosion)

        if cv.waitKey(5) == ord('q'):
            break

captureImage.release()
cv.destroyAllWindows()