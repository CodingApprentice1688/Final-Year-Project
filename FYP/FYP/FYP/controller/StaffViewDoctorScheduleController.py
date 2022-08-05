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
    dname = request.form['dname']
    doctor = Booking.StaffViewDoctorSchedule(dname)
    # session['patientY'] = patientY
    return render_template('StaffViewDoctorSchedule.html', doctor = doctor, dname = dname)
