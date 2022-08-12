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


@app.route('/StaffSearchDoctorController', methods=['GET', 'POST'])
def StaffSearchDoctorController():
    all_files = storage.list_files() # get all file
    cnt = 0
    path = "doctorimages"
    try:
        os.makedirs("FYP/static/" + path)
    except:
        pass
    for file in all_files:
        if "doctor/" in file.name and file.name != "doctor/":
            joinedpath = os.path.join("FYP/static/", path)
            file.download_to_filename(joinedpath+"/"+str(file.name[file.name.find('/'):]))
            cnt = cnt + 1

    patientX = session["patientX"]  ##
    session['patientX'] = patientX  ##

    if request.method == "POST":
        name = request.form['name']
        doctor = User.StaffSearchDoctorController(name)
        return render_template('StaffSearchDoctor.html', doctor = doctor, patientX = patientX)
    else:
        
        doctor = 'doctor'
        doctor = User.StaffSearchDoctor(doctor)
        return render_template('StaffSearchDoctor.html', doctor = doctor, patientX = patientX)