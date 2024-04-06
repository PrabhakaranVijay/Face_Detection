import cv2 as cv
import mediapipe as mp
import time

# path of the video file 
# (or give device index '0' for webCam)
video_path = 0

video = cv.VideoCapture(video_path)

pTime = 0

# imports the necessary libraries and creates an 
# instance of the Face Detection model from the Mediapipe library.
mp_face_detection = mp.solutions.face_detection
mp_draw = mp.solutions.drawing_utils
face_detection = mp_face_detection.FaceDetection()

while True:
    isTrue, frame = video.read()

    # mediapipe reads RGB images 
    # so we need to convert the BGR image to RGB
    frame_rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    results = face_detection.process(frame_rgb)
    # print(results)  # <class 'mediapipe.python.solution_base.SolutionOutputs'>
    
    if results.detections:
        for faceID, detection in enumerate(results.detections):
            # This id default datatype to draw rectangle on detected faces
            mp_draw.draw_detection(frame,detection)
            # print(faceID, detection)  # faceID -> says no.of detected faces,
                                        # detection -> shows the bounding box and score
            # print(faceID, detection.score)  # score -> accuracy

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