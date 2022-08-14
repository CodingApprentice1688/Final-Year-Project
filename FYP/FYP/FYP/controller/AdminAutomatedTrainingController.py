
from FYP import app 
from FYP.entity.User import *
from FYP.entity.Appointments import *
from datetime import datetime, date
from flask import render_template
from FYP import mysql
from FYP import storage

from flask import Flask,render_template, request, redirect, url_for, Response, session
from flask_mysqldb import MySQL
import MySQLdb.cursors 

import re
import os
import numpy as np
import pandas as pd
from PIL import Image
import tensorflow as tf
from keras.layers import Conv2D, Dense, Flatten, MaxPool2D, Dropout
from numpy import asarray
from mtcnn import MTCNN
from os import listdir


from tensorflow.keras.utils import to_categorical
from sklearn.preprocessing import LabelEncoder
from keras.models import load_model

def extract_face(filename, required_size=(200, 200)):
    # load image from file
    image = Image.open(filename)
    image = image.convert('RGB')
    pixels = asarray(image)
    detector = MTCNN()
    results = detector.detect_faces(pixels)
    x1, y1, width, height = results[0]['box']
    x1, y1 = abs(x1), abs(y1)
    x2, y2 = x1 + width, y1 + height
    face = pixels[y1:y2, x1:x2]
    image = Image.fromarray(face)
    image = image.resize(required_size)
    face_array = asarray(image)
    return face_array

def obtain_train_test_dataset(path):
    data = []
    label = []
    directorii = []
    i = 0
    for subdir, dirs, files in os.walk(path):
        if i == 0:
            directorii = dirs
        i = 1
        
    for i in directorii:
        img_path = os.path.join(path, str(i)) 
        print(img_path)
        for img in os.listdir(img_path):
            image = extract_face(img_path + '/' + img)
            images = image.astype('float32')
            images = np.array(images)
            data.append(images)
            label.append(i)

    data = np.array(data)
    label = np.array(label)
    
    return data, label

@app.route('/AdminAutomatedTraining')
def AdminAutomatedTraining():
    return render_template('AdminAutomatedTraining.html')

@app.route('/AdminDownloadImagesController', methods=["POST", "GET"])
def downloadImages():
    all_files = storage.list_files() # get all file
    cnt = 0
    path = ["train", "val"]
    for paths in path:
        try:
            os.makedirs("FYP/deeplearning/" + paths)
        except:
            pass
    for file in all_files:
        joinedpath = "FYP/deeplearning/"
        
        if (file.name.split("/", 1)[0] == "train" or file.name.split("/", 1)[0] == "val") and (file.name != "train/" and file.name != "val/"):
            file_name = file.name.split("/", 1)[1]
            direc = file_name.split(".", 1)[0]
            dir_name = ""
            for value in direc:
                if value.isalpha():
                    dir_name = direc.split(value, 1)[1]
                    dir_name = value + dir_name
                    break

            if file_name[0] == "0":
                for paths in path: 
                    try:
                        os.makedirs("FYP/deeplearning/" + paths + "/" + dir_name)
                    except:
                        continue
                file.download_to_filename(joinedpath+file.name.split("/", 1)[0]+ "/" + dir_name + "/" + file_name)
            else:
                file.download_to_filename(joinedpath+file.name.split("/", 1)[0]+ "/" + dir_name + "/" + file_name)


    return render_template('AdminAutomatedTraining.html')

@app.route('/AdminAutomatedTrainingController', methods=["POST", "GET"])
def automatedTrain():
    x_train, y_train = obtain_train_test_dataset("FYP/deeplearning/train")
    x_test, y_test = obtain_train_test_dataset("FYP/deeplearning/val")

    label_encoder = LabelEncoder()
    y_train = label_encoder.fit_transform(y_train)
    y_test = label_encoder.fit_transform(y_test)
    y_train = to_categorical(y_train)
    y_test = to_categorical(y_test)

    

    model = load_model('FYP/deeplearning/model/my_model.h5')
    model.pop()
    model.layers[0].trainable=False
    model.add(Dense(len(np.unique(y_train)), activation="softmax"))

    model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
    callback = tf.keras.callbacks.EarlyStopping(monitor='loss', patience=10)
    
    model.fit(x_train, y_train, epochs=30, batch_size=64, validation_data=(x_test, y_test),
                       callbacks=[callback])

    model.save("FYP/deeplearning/model/my_model.h5")

    return render_template('AdminAutomatedTraining.html')


