
from FYP import app 
from FYP.entity.User import *
from FYP.entity.Appointments import *
from datetime import datetime, date
from flask import render_template
from FYP import mysql
from FYP import storage

from FYP.camera import VideoCamera

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




@app.route('/AdminChangePatientImage', methods=['GET', 'POST'])
def AdminChangePatientImage():
    username = request.form['usernamea']
    ten = 0
    allow = 'none'

    """Renders the about page."""
    return render_template(
        'AdminChangePatientImage.html', username = username, ten = ten, allow = allow)


@app.route('/AdminChangePatientImageController',  methods=['GET', 'POST'])
def changeImage():

    path = "FYP/static/pati/"
    for files in os.listdir(str(path)):
        storage.child("patient/" + str(files)).put(str(path) + str(files))

    path1 = "FYP/static/temp/"
    for files in os.listdir(str(path1)):
        if int(files[0]) != 2:
            storage.child("train/" + str(files)).put(str(path1) + str(files))
        elif int(files[0]) == 2 and files[1].isalpha():
            storage.child("train/" + str(files)).put(str(path1) + str(files))
        else:
            storage.child("val/" + str(files)).put(str(path1) + str(files))
    """Renders the about page."""
    return redirect('/Admin_Main')



@app.route('/change_25_pics', methods=["POST", "GET"])
def change_25_pics():
    username = request.form['usernameb']
    VideoCamera().capture_10_pics(username);
    
    ten = 25
    return render_template('AdminChangePatientImage.html', ten = ten, username = username)

@app.route('/change_one_pic', methods=["POST", "GET"])
def change_one_pic():
    username = request.form['username']
    VideoCamera().capture_one_pic(username);
    return render_template('AdminChangePatientImage.html', ten = 0, username = username)