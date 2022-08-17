

from FYP import app 
from FYP.entity.User import *
from FYP.entity.Appointments import *
from datetime import datetime, date
from flask import render_template
from FYP import mysql
from FYP import storage
from FYP.camera import VideoCamera
import os

from flask import Flask,render_template, request, redirect, url_for, Response, session
from flask_mysqldb import MySQL
import MySQLdb.cursors 

@app.route('/AdminChangePatientCredentialsController',  methods=['GET', 'POST'])
def adminUpdatePersonalDetails():
    name = request.form['name']
    nric = request.form['nric']
    age = request.form['age']
    gender = request.form['gender']
    username = request.form['username']
    password = request.form['password']

    userA = User.updatePersonalDetail(name, nric, age, gender, username, password)
    """Renders the about page."""
    return render_template(
        'AdminChangePatientCredentials.html', userA = userA)

@app.route('/AdminChangePatientCredentials',  methods=['GET', 'POST'])
def AdminChangePatientCredentials():
    nric = request.form['nric']
    password = request.form['passworda']
    name = request.form['namea']
    age = request.form['agea']
    gender = request.form['gendera']
    userA = User.getPatientCreds(nric)
    """Renders the about page."""
    return render_template(
        'AdminChangePatientImage.html', userA = userA)



@app.route('/change_25_pics', methods=["POST", "GET"])
def change_25_pics():
    username = request.form['usernameb']
    password = request.form['passwordb']
    name = request.form['nameb']
    nric = request.form['nricb']
    age = request.form['ageb']
    gender = request.form['genderb']
    VideoCamera().capture_10_pics(username);
    
    ten = 25
    return render_template('AdminChangePatientImage.html', ten = ten, dform = "none", dcheck = "inline", dcheck1 = "none", submitb = "block", username = username,
                               password = password, name = name, nric = nric, age = age, gender = gender)

@app.route('/change_one_pic', methods=["POST", "GET"])
def change_one_pic():
    username = request.form['usernamea']
    password = request.form['passworda']
    name = request.form['namea']
    nric = request.form['nrica']
    age = request.form['agea']
    gender = request.form['gendera']
    VideoCamera().capture_one_pic(username);
    #VideoCamera().get_frame(username, "one");
    return render_template('AdminChangePatientImage.html', ten = 0, dform = "none", dcheck = "inline", dcheck1 = "none", submitb = "block", username = username,
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




    
    