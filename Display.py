import cv2 as cv
def displayImage(image):
    cv.imshow("Detected Lines", image)
    cv.waitKey(1)
