# Face recognization
Python and Opencv project to perform face recognization in images.

## Requirements
You will need [Python](https://www.python.org/) and [OpenCV](https://opencv.org/).

Linux already comes with a python version, is a bit old, so i recommend you to update it.
I have python3.7 here, so im using it.

First, lets install pip, a python package manager:
```bash
$ python3.7 -m pip install pip
```

Now, install OpenCV:
```bash
$ pip3.7 install opencv-contrib-python
```

Testing if the OpenCV is correctly installed:
```bash
$ python3.7     # will open the Python terminal
```
Import the OpenCV package and log the version of it:
```python
import cv2
cv2._version_
```
If no errors, we are done.

## Running the face recognition
To run the program, just do:
```bash
$ python3.7 face-recognition.py
```

You can selet other images to test, i let some in the `img` folder. You can also play with the values of the functions, configure it another way trying to get better results.

## References
[OpenCV documentation](https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html)

[Marlon de Alencar Rocha](https://blog.cedrotech.com/opencv-uma-breve-introducao-visao-computacional-com-python/)

## Leonardo Zanotti
