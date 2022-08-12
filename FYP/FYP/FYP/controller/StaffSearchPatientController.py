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
    if request.method == "POST":
        name = request.form['name']
        pat = 'patient'
        patient = User.StaffSearchPatientController(name, pat)
        return render_template('StaffSearchPatient.html', patient = patient)
    else:
        all_files = storage.list_files() # get all file
        cnt = 0
        path = "patientimages"
        try:
            os.makedirs("FYP/static/" + path)
        except:
            pass
        for file in all_files:
            if "patient/" in file.name and file.name != "patient/":
                joinedpath = os.path.join("FYP/static/", path)
                file.download_to_filename(joinedpath+"/"+str(file.name[file.name.find('/'):]))
                cnt = cnt + 1
        patient = 'patient'
        patient = User.StaffSearchPatient(patient)
        return render_template('StaffSearchPatient.html', patient = patient)