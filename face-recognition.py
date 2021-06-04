import cv2 as cv
import numpy as np

face_classifier = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_classifier = cv.CascadeClassifier('haarcascade_eye.xml')

image = cv.imread('./img/img1.jpg')

image_gray = cv.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = face_classifier.detectMultiScale(image_gray, 1.3, 5)

for (x, y, w, h) in faces:
    cv.rectangle(image)
