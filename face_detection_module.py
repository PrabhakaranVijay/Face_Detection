import cv2 as cv
import mediapipe as mp
import time

# path of the video file 
# (or give device index '0' for webCam)
video_path = 0

video = cv.VideoCapture(video_path)

pTime = 0

while True:
    isTrue, frame = video.read()

    # print frame pre seconds FPS
    # to find speed of capture
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv.putText(frame, f'fps: {int(fps)}',(10,50),cv.FONT_HERSHEY_PLAIN, 2, (0,0,255),2)

    cv.imshow('video',frame)

    # press 'd' to exit from the loop 
    if cv.waitKey(1) & 0xFF==ord('d'):
        break
 
video.release()
cv.destroyAllWindows()