from FYP import app 
from FYP.entity.User import *
from FYP.entity.Appointments import *
from datetime import datetime, date
from flask import render_template
from FYP import mysql

from flask import Flask,render_template, request, redirect, url_for, Response, session
from flask_mysqldb import MySQL
import MySQLdb.cursors 


@app.route('/PatientQueueNumber', methods=['GET', 'POST'])
def queueUpdateSession():
    userA = Appointments.QueueUpdateSession()
    return render_template('PatientQueueNumber.html', userA = userA)

@app.route('/PatientQueueNumberController', methods=['GET', 'POST'])
def PatientQueueNumber():
    queueNumber = request.form['queueNumber']
    userA = Appointments.updateQueueNumber(queueNumber)
    return render_template('PatientQueueNumber.html', userA = userA)

#@app.route('/PatientQueueNumberController', methods=['POST'])
#def QueueNumberCapture():
#    VideoCamera().stop_camera()
#    return redirect(url_for('Patient_Main'))