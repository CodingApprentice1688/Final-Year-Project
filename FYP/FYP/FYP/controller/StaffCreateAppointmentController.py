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


@app.route('/StaffCreateAppointmentController', methods=['GET', 'POST'])
def StaffCreateAppointmentController():
    if request.method == "POST":
        username = request.form['username'],
        name = request.form['name'],
        nric = request.form['nric'],
        date_slot = request.form['date_slot'],
        app_time = request.form['app_time'],
        department = request.form['department'],
        doctor = request.form['doctor'],
        reason = request.form['reason']
        patientX = Appointments.StaffCreateAppointment(username, name, nric, date_slot, app_time, department, doctor, reason)

        Booking.StaffCreateAppointment(doctor,date_slot,app_time)

        return render_template('StaffCreateAppointment.html', patientX = patientX)
    else:
        patientX = session["patientX"]  ##
        return render_template('StaffCreateAppointment.html', patientX = patientX)
    
        