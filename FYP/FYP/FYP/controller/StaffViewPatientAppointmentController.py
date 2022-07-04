from FYP import app 
from FYP.entity.User import *
from FYP.entity.Appointments import *
from datetime import datetime, date
from flask import render_template
from FYP import mysql

from flask import Flask,render_template, request, redirect, url_for, Response, session
from flask_mysqldb import MySQL
import MySQLdb.cursors 


@app.route('/StaffViewPatientAppointmentController', methods=['GET', 'POST'])
def StaffViewPatientAppointmentController():
    
    username = request.form['username']
    nric = request.form['nric']
    userA, userB, patientX = Appointments.StaffViewPatientAppointment(username, nric)
    session['patientX'] = patientX  ##
    return render_template('StaffViewPatientAppointment.html', userA = userA, userB = userB)