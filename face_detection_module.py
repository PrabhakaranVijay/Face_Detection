import cv2 as cv
import mediapipe as mp
import time

video_path = '/Users/prabhakaranvijay/Machine Learning/OpenCV/videos/1.mov'

video = cv.VideoCapture(video_path)



while True:
    isTrue, frame = video.read()

    cv.imshow('video',frame)

    if cv.waitKey(1) & 0xFF==ord('d'):
        break

video.release()
cv.destroyAllWindows()