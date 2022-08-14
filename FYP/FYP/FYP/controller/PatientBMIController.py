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

import os
import joblib
import numpy as np
import pandas as pd
#import face_recognition
from sklearn.model_selection import train_test_split


def face_into_encoding(path):
    image = face_recognition.load_image_file(path)
    face_encoding = face_recognition.face_encodings(image)
    if not face_encoding:
        print("skipped" + path)
        return np.zeros(128).tolist()
    return face_encoding[0].tolist()

def predict_bmi(X_images, model):
    X = np.expand_dims(np.array(face_into_encoding(X_images)), axis=0)
    log_value = model.predict(X)
    bmi = np.exp(log_value)
    return bmi.tolist()

@app.route('/PatientBMI', methods=['GET', 'POST'])
def DisplayPatientBMI():
    return render_template('PatientBMI.html', bmifloat = "", showHidden = True)

@app.route('/PatientBMIController', methods=['GET', 'POST'])
def calculateBMI():
    VideoCamera().capture_1_pic()
    rf_model = "FYP/deeplearning/model/rf_bmi_model_tuned"
    model = joblib.load(rf_model)
    
    if 'logged_in' in session: 
        img_location = 'FYP/static/images/loginpic.jpg'
        preds = predict_bmi(img_location, model)
        bmifloat = round(preds[0], 1)
    return render_template('PatientBMI.html', bmifloat = bmifloat, showHidden = False)