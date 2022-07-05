from FYP import app 
from FYP.entity.User import *
from FYP.entity.Appointments import *
from datetime import datetime, date
from flask import render_template
from FYP import mysql

from flask import Flask,render_template, request, redirect, url_for, Response, session
from flask_mysqldb import MySQL
import MySQLdb.cursors 


#patient get queue number
@app.route('/PatientQueueNumberController', methods=['GET', 'POST'])
def PatientQueueNumber():
    return render_template(
        'PatientQueueNumber.html',
        title='PatientQueueNumber',
        year=datetime.now().year
    )

@app.route('/PatientQueueNumberController', methods = ['POST'])
def QueueNumberCapture():
    VideoCamera().stop_camera()
    return redirect(url_for('Patient_Main'))