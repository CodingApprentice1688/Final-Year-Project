from FYP import app 
from FYP.entity.User import *
from FYP.entity.Appointments import *
from datetime import datetime, date
from flask import render_template
from FYP import mysql
from FYP import storage
import os

from flask import Flask,render_template, request, redirect, url_for, Response, session
from flask_mysqldb import MySQL
import MySQLdb.cursors 


@app.route('/StaffSearchPatientController', methods=['GET', 'POST'])
def StaffSearchPatientController():
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

    if request.method == "POST":
        name = request.form['name']
        pat = 'patient'
        patient = User.StaffSearchPatientController(name, pat)
        return render_template('StaffSearchPatient.html', patient = patient)
    else:
        patient = 'patient'
        patient = User.StaffSearchPatient(patient)
        return render_template('StaffSearchPatient.html', patient = patient)