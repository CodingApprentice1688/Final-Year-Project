

from FYP import app 
from FYP.entity.User import *
from FYP.entity.Appointments import *
from datetime import datetime, date
from flask import render_template
from FYP import mysql
from FYP.camera import VideoCamera

from flask import Flask,render_template, request, redirect, url_for, Response, session
from flask_mysqldb import MySQL
import MySQLdb.cursors 



"""https://towardsdatascience.com/do-you-know-python-has-a-built-in-database-d553989c87bd"""
#do cicd and unit testing 

#go to admin login, capture and copy paste into the DeepLearning\train and val folder
# find out the face recognition algorithm with auto adding

@app.route('/AdminRegisterPatientController', methods=['GET', 'POST'])
def registerPatient():
    
    name = request.form['name']
    nric = request.form['nric']
    age = request.form['age']
    gender = request.form['gender']
    username = request.form['username']
    password = request.form['password']
    role = 'patient'
    ten = 0
    
    User.registerPatient(name, nric, age, gender, username, password, role)
    return render_template('AdminRegisterPatient.html', ten = ten)


@app.route('/capture_25_pics', methods=["POST", "GET"])
def capture_25_pics():
    username = request.form['usernameb']
    password = request.form['passwordb']
    name = request.form['nameb']
    nric = request.form['nricb']
    age = request.form['ageb']
    gender = request.form['genderb']
    VideoCamera().capture_10_pics(username);
    ten = 25
    return render_template('AdminRegisterPatient.html', ten = ten, dform = "none", dcheck = "inline", dcheck1 = "none", submitb = "block", username = username,
                               password = password, name = name, nric = nric, age = age, gender = gender)

@app.route('/capture_one_pic', methods=["POST", "GET"])
def capture_one_pic():
    username = request.form['usernamea']
    password = request.form['passworda']
    name = request.form['namea']
    nric = request.form['nrica']
    age = request.form['agea']
    gender = request.form['gendera']
    VideoCamera().capture_one_pic(username);

    return render_template('AdminRegisterPatient.html', ten = 0, dform = "none", dcheck = "inline", dcheck1 = "none", submitb = "block", username = username,
                               password = password, name = name, nric = nric, age = age, gender = gender)
#class AdminRegisterPatientController:
    

#    def RegisterPatient():
#        name = request.form['name']
#        nric = request.form['nric']
#        age = request.form['age']
#        gender = request.form['gender']
#        username = request.form['username']
#        password = request.form['password']
#        role = 'patient'
        
#        user = User()
#        user.AdminRegisterPatient(name, nric, age, gender, username, password, role)




    
    