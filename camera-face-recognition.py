import cv2 as cv
import numpy as np

face_cascade = cv.CascadeClassifier(cv.data.haarcascades +
                                    'haarcascade_frontalface_default.xml')
eyes_cascade = cv.CascadeClassifier(cv.data.haarcascades +
                                    'haarcascade_eye.xml')


def detectAndDisplay(frame):
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame_gray = cv.equalizeHist(frame_gray)
    faces = face_cascade.detectMultiScale(frame_gray, 1.23, 5, 0, [55, 55])
    for (x, y, w, h) in faces:
        frame = cv.ellipse(frame, (x + w // 2, y + h // 2), (w // 2, h // 2),
                           0, 0, 360, (255, 0, 255), 2)
        face_gray = frame_gray[y:y + h, x:x + w]
        face_color = frame[y:y + h, x:x + w]
        eyes = eyes_cascade.detectMultiScale(face_gray, 1.05, 2, 0, [55, 55])
        for (x2, y2, w2, h2) in eyes:
            eye_center = (x2 + w2 // 2, y2 + h2 // 2)
            radius = int(round((w2 + h2) * 0.25))
            frame = cv.circle(face_color, eye_center, radius, (255, 0, 0), 4)
    cv.imshow('Capture - Face detection', frame)
    cv.imwrite('./webcam.png', frame)


# Here, im using IP Webcam mobile app to run the camera device, you can use your notebook camera
# For more info about IP Webcam app, see the "I know python - video" in the references
video = cv.VideoCapture(0)
video.open('http://192.168.0.6:8080/video')

if not video.isOpened:
    print('--(!)Error opening video capture')
    exit(0)

while True:
    ret, frame = video.read()
    if frame is None:
        print('--(!) No captured frame -- Break!')
        break
    detectAndDisplay(frame)
    if cv.waitKey(10) == 27:
        break

video.release()
