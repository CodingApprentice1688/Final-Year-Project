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
    userA, userB = Appointments.QueueUpdateSession()
    return render_template('PatientQueueNumber.html', userA = userA, userB = userB)

@app.route('/PatientQueueNumberController', methods=['GET', 'POST'])
def PatientQueueNumber():
    queueNumber = request.form['queueNumber']
    userA, userB = Appointments.updateQueueNumber(queueNumber)
    return render_template('PatientQueueNumber.html', userA = userA, userB = userB)