import cv2
import os
import tkinter
from tkinter import *
from tkinter import messagebox
global image
import numpy

#creating GUI window
top=Tk()
top.geometry('500x500')


def cap_face():
    # capturing image from webcam
    camera = cv2.VideoCapture(0)
    return_value, image = camera.read()
    #converting colourimage to gray
    gray = cv2.cvtColor(image, cv2.COLOR_BGRA2GRAY)
    # for detecting face from image

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=3,
        minSize=(30, 30)
    )
#extracting detected face from image crop it
    for (x, y, w, h) in faces:
        cv2.rectangle(gray, (x, y), (x + w, y + h), (250, 0, 255), 2)
        roi_image = gray[y:y + h, x:x + w]
#write image in specified folder
    path = os.getcwd() + '/database'
    cv2.imwrite(os.path.join(path, 'new' + '3' + '.png'), roi_image)
   
    msg = messagebox.showinfo('face detector', "Image Stored Successfully")
    del camera




B = Button(top, text='click image', command=cap_face)
B.place(x=50,y=50)
top.mainloop()


