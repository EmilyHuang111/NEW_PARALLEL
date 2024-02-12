import cv2 as cv
import Process
import Display
try:
    def DisplayLines():
        videoIsPlaying = True
        video = cv.VideoCapture(0)
        while videoIsPlaying == True:
            videoIsPlaying, frame = video.read()
            Process.processImage(frame)
            Display.displayImage(frame)
        cv.destroyAllWindows()
    DisplayLines()
except:
    print("Quitting the program")
finally:
    exit()
