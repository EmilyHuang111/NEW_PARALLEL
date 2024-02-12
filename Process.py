import cv2 as cv
import numpy as np
def processImage(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    gray_scale = cv.GaussianBlur(gray, (15, 15), 0)
    median_blur = cv.medianBlur(gray_scale, 5)
    canny_image = cv.Canny(median_blur, 100, 20)
    roi = np.zeros(image.shape[:2], dtype="uint8")
    cv.rectangle(roi, (500, 500), (850, 850), 1, -1)
    mask = cv.bitwise_and(canny_image, canny_image, mask=roi)
    cv.rectangle(image, (500, 500), (850, 850), (0, 255, 0), 5)
    lines = cv.HoughLinesP(mask, 1, np.pi / 180, threshold=10, minLineLength=10, maxLineGap=15)
    if lines is not None:
        slope_arr = []
        lines_list = []
        for line in lines:
            x1, y1, x2, y2 = line[0]
            lines_list.append(line[0])
            cv.line(image, (x1, y1), (x2, y2), (0, 255, 0), 10)
            slope = 0
            if x2 - x1 != 0:
                slope = (y2 - y1) / (x2 - x1)
            slope_arr.append(slope)
        for i in range(len(slope_arr)):
            for j in range(len(slope_arr)):
                x1, y1, x2, y2 = lines_list[i]
                x3, y3, x4, y4 = lines_list[j]
                cv.line(image, ((x1 + x3) // 2, (y1 + y3) // 2), ((x2 + x4) // 2, (y2 + y4) // 2), (255, 0, 255), 10)

