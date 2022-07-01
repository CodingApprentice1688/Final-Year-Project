from FYP import app 
from FYP.entity.User import *
from datetime import datetime, date
from flask import render_template
from FYP import mysql

from flask import Flask,render_template, request, redirect, url_for, Response, session
from flask_mysqldb import MySQL
import MySQLdb.cursors 

@app.route('/PatientCancelAppointmentController', methods=['GET', 'POST'])
def PatientCancelAppointmentController():
    message = ''
    msg = ''
    if 'logged_in' in session: 
        app_id = request.form['appointment_id']
        userA, userB = User.PatientCancelAppointmentController(app_id)
        return render_template('Patient_ViewAppointment.html', userA = userA, userB = userB)

