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

@app.route('/StaffViewDoctorScheduleController', methods=['GET', 'POST'])
def StaffViewDoctorScheduleController():
    patientX = session["patientX"]  ##
    session['patientX'] = patientX  ##
    
    dname = request.form['dname']
    date_from = request.form['date_from']
    date_to = request.form['date_to']

    doctor = Booking.StaffViewDoctorSchedule(dname, date_from, date_to)

    return render_template('StaffViewDoctorSchedule.html', doctor = doctor, dname = dname)
