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
    image = Image.open(filename)
    image = image.convert('RGB')
    pixels = asarray(image)
    detector = MTCNN()
    results = detector.detect_faces(pixels)
    if results:
        x1, y1, width, height = results[0]['box']
        x1, y1 = abs(x1), abs(y1)
        x2, y2 = x1 + width, y1 + height
        face = pixels[y1:y2, x1:x2]
        image = Image.fromarray(face)
        image = image.resize(required_size)
        face_array = asarray(image)
        return True, face_array
    else:
        return






@app.route('/FacialLoginController', methods=['POST', 'GET'])
def validateImage():
    VideoCamera().capture_1_pic()

    model = load_model("FYP/deeplearning/model/vggface_model_30.h5")
    try:
        result, pixels = extract_face('FYP/static/images/loginpic.jpg')
    except:
        result = False
        pass


    if result:
        hello = []
        pixels = pixels.astype('float32')
        pixels = np.array(pixels)
        hello.append(pixels)
        hello = np.array(hello)

        yhat=model.predict(hello)

        my_file = open("FYP/deeplearning/model/patientlist.txt", "r")
  
        # reading the file
        data = my_file.read()
        y_test = data.split("\n")
        y_test.sort()
        my_file.close()

        app.logger.info(y_test)

        prediction_index = np.argmax(yhat, axis=None, out=None)
        prediction = y_test[prediction_index]

        userL = User.getImageInfo(prediction)
        return render_template('validation.html', userL = userL)
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