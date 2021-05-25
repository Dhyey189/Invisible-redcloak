import numpy as np
import cv2 as cv
import imutils

captureImage = cv.VideoCapture(0,cv.CAP_DSHOW)

while captureImage.isOpened():
    (status, back) = captureImage.read()
    # back = imutils.resize(back, width=400)
    if status:
        cv.imshow("image", back)
        if cv.waitKey(10) & 0xFF == ord('q'):
            cv.imwrite('Image.jpg', back)
            break

captureImage.release()
cv.destroyAllWindows()



