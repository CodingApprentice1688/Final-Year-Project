
from FYP import app 
from FYP.entity.User import *
from datetime import datetime, date
from flask import render_template
from FYP import mysql
from FYP import storage
import os

from flask import Flask,render_template, request, redirect, url_for, Response, session
from flask_mysqldb import MySQL
import MySQLdb.cursors 


@app.route('/AdminSearchPatient', methods=['GET', 'POST'])
def AdminSearchPatient():
    all_files = storage.list_files() # get all file
    cnt = 0
    path = "patientimages"
    for file in all_files:
        if file.name == "patient/":
            try:
                os.makedirs("FYP/static/" + path)
            except:
                pass
            continue
        if "patient/" in file.name:
            joinedpath = os.path.join("FYP/static/", path)
            file.download_to_filename(joinedpath+"/"+str(file.name[file.name.find('/'):]))
            cnt = cnt + 1
            
    pat = 'patient'

    patient = User.AdminSearchPatient(pat)
    return render_template('AdminSearchPatient.html', patient = patient)
    

@app.route('/AdminSearchPatientController', methods=['GET', 'POST'])
def AdminSearchPatientController():
    name = request.form['name']
    pat = 'patient'
    patient = User.AdminSearchPatientController(name, pat)
    return render_template('AdminSearchPatient.html', patient = patient)

#the current files 
#@app.route('/AdminSearchPatient', methods=['GET', 'POST'])
#def searchPatient():

#    name = request.form['name']
#    nric = request.form['nric']
#    age = request.form['age']
#    gender = request.form['gender']
#    username = request.form['username']
#    password = request.form['password']
#    role = 'patient'
#    ten = 0
#    #need a line to take the search term from the AdminSearchPatient 
#    User.registerPatient(name, nric, age, gender, username, password, role)
#    return render_template('AdminSearchPatient.html', ten = ten)
