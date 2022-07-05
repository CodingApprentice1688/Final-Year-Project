from FYP import app 
from FYP.entity.User import *
from FYP.entity.Appointments import *
from datetime import datetime, date
from flask import render_template
from FYP import mysql

from flask import Flask,render_template, request, redirect, url_for, Response, session
from flask_mysqldb import MySQL
import MySQLdb.cursors 

@app.route('/PatientViewAppointmentController', methods=['GET', 'POST'])
def viewAppointment():
    if 'logged_in' in session: 
        userA, userB = Appointments.viewAppointment()
    return render_template('PatientViewAppointment.html', userA = userA, userB = userB)
