# demonstrate face detection on 5 Celebrity Faces Dataset
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import tensorflow as tf
from keras.layers import Conv2D, Dense, Flatten, MaxPool2D, Dropout
from numpy import asarray
from matplotlib import pyplot
from mtcnn import MTCNN
from os import listdir
from tensorflow.keras.utils import to_categorical
from keras.models import load_model


from FYP import app 
from FYP.entity.User import *
from FYP.entity.Appointments import *
from FYP.camera import VideoCamera
from datetime import datetime, date
from flask import render_template
from FYP import mysql

from flask import Flask,render_template, request, redirect, url_for, Response, session
from flask_mysqldb import MySQL
import MySQLdb.cursors 







def extract_face(filename, required_size=(200, 200)):
    # load image from file
    image = Image.open(filename)
    image = image.convert('RGB')
    pixels = asarray(image)
    # use MTCNN face detector to detect faces inside the image
    detector = MTCNN()
    results = detector.detect_faces(pixels)
    x1, y1, width, height = results[0]['box']
    # bug fix
    x1, y1 = abs(x1), abs(y1)
    x2, y2 = x1 + width, y1 + height
    # extract the face
    face = pixels[y1:y2, x1:x2]
    # resize pixels to the model size
    image = Image.fromarray(face)
    image = image.resize(required_size)
    face_array = asarray(image)
    return face_array


@app.route('/FacialLoginController', methods=['POST', 'GET'])
def validateImage():
    VideoCamera().capture_1_pic()

    model = load_model("FYP/FYP/FYP/deeplearning/model/my_modelv3.h5")
    model.summary()
    pixels = extract_face('FYP/FYP/FYP/static/images/loginpic.jpg')
    hello = []
    pixels = pixels.astype('float32')
    pixels = np.array(pixels)
    hello.append(pixels)
    hello = np.array(hello)

    yhat=model.predict(hello)

    
    y_test = []
    i = 0
    for subdir, dirs, files in os.walk("FYP/FYP/FYP/deeplearning/val"):
        if i == 0:
            y_test = dirs
        i = 1

    prediction_index = np.argmax(yhat, axis=None, out=None)
    prediction = y_test[prediction_index]

    userL = User.getImageInfo(prediction)
    if userL:
        if userL['role'] == 'healthcare staff':
            return redirect("/HealthcareStaff_Main")
        if userL['role'] == 'patient':
            return redirect("/Patient_Main")
        if userL['role'] == 'IT admin':
            return redirect("/Admin_Main") 
    else:
        return render_template('login.html')

#from keras.models import load_model

#model = load_model('my_model.h5')
#model.summary()

#pixels = extract_face('../Desktop/framed.jpg')
#hello = []
#pyplot.subplot(2, 7, 1)
#pyplot.axis('off')
#pyplot.imshow(pixels)
#pyplot.show()
#pixels = pixels.astype('float32')
#pixels = np.array(pixels)
#hello.append(pixels)
#hello = np.array(hello)