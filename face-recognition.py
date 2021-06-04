import cv2 as cv
import numpy as np

face_classifier = cv.CascadeClassifier(cv.data.haarcascades +
                                       'haarcascade_frontalface_default.xml')
eye_classifier = cv.CascadeClassifier(cv.data.haarcascades +
                                      'haarcascade_eye.xml')

image = cv.imread('./img/img7.png')

image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

faces = face_classifier.detectMultiScale(image_gray, 1.23, 5, 0, [55, 55])
print(faces)

for (x, y, w, h) in faces:
    cv.rectangle(image, (x, y), (x + w - 25, y + h - 25), (255, 0, 0), 2)
    face_gray = image_gray[y:y + h - 25, x:x + w - 25]
    face_color = image[y:y + h - 25, x:x + w - 25]
    eyes = eye_classifier.detectMultiScale(face_gray, 1.2, 5, 0, [55, 55])
    for (ex, ey, ew, eh) in eyes:
        cv.rectangle(face_color, (ex, ey), (ex + ew, ey + eh), (255, 0, 0), 2)

cv.imshow('Face recognized', image)
cv.waitKey(10000)
cv.destroyAllWindows()
