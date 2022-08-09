from FYP import app 
from FYP.entity.User import *
from FYP.entity.Appointments import *
from FYP.entity.Booking import *
from datetime import datetime, date
from flask import render_template
from FYP import mysql

from flask import Flask,render_template, request, redirect, url_for, Response, session
from flask_mysqldb import MySQL
import MySQLdb.cursors 


@app.route('/StaffCreateAppointment', methods=['GET', 'POST'])
def StaffCreateAppointment():
    patientX = session["patientX"]  ##
    doctor = request.form['doctor']
    _date = request.form['_date']
    starttime = request.form['starttime']
    department = request.form['department']
    return render_template('StaffCreateAppointment.html', patientX = patientX, doctor = doctor, _date = _date, starttime = starttime, department = department)


@app.route('/StaffCreateAppointmentController', methods=['GET', 'POST'])
def StaffCreateAppointmentController():
    username = request.form['username'],
    name = request.form['name'],
    nric = request.form['nric'],
    date_slot = request.form['_date'],
    app_time = request.form['starttime'],
    department = request.form['department'],
    doctor = request.form['doctor'],
    reason = request.form['reason']
    #patientX = Appointments.StaffCreateAppointment(username, name, nric, date_slot, app_time, department, doctor, reason)
    Appointments.StaffCreateAppointment(username, name, nric, date_slot, app_time, department, doctor, reason)
    Booking.StaffCreateAppointment(doctor,date_slot,app_time)
    
    # return render_template('StaffCreateAppointment.html', patientX = patientX)
    patient = 'patient'
    patient = User.StaffSearchPatient(patient)
    return render_template('StaffSearchPatient.html', patient = patient)
