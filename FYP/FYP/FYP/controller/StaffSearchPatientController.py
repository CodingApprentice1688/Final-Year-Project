from FYP import app 
from FYP.entity.User import *
from FYP.entity.Appointments import *
from datetime import datetime, date
from flask import render_template
from FYP import mysql

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
        patient = 'patient'
        patient = User.StaffSearchPatient(patient)
        return render_template('StaffSearchPatient.html', patient = patient)