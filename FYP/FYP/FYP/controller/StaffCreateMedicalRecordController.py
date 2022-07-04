from FYP import app 
from FYP.entity.User import *
from FYP.entity.Appointments import *
from FYP.entity.MedicalRecords import *
from datetime import datetime, date
from flask import render_template
from FYP import mysql

from flask import Flask,render_template, request, redirect, url_for, Response, session
from flask_mysqldb import MySQL
import MySQLdb.cursors 


@app.route('/StaffCreateMedicalRecordController', methods=['GET', 'POST'])
def StaffCreateMedicalRecordController():
    if request.method == "POST":
        appointment_id = request.form['appointment_id'],
        username = request.form['username'],
        vaccination_status = request.form['vaccination_status'],
        blood_pressure = request.form['blood_pressure'],
        temperature = request.form['temperature'],
        heart_rate = request.form['heart_rate'],
        allergies = request.form['allergies'],
        medicine = request.form['medicine'],
        diagnosis = request.form['diagnosis']
        MedicalRecords.StaffCreateMedicalRecord(appointment_id, username, vaccination_status, blood_pressure, temperature, heart_rate, allergies, medicine, diagnosis)
        patientY = session["patientY"]
        return render_template('StaffCreateMedicalRecord.html', patientY = patientY)
    else:
        patientY = session["patientY"]  ##
        return render_template('StaffCreateMedicalRecord.html', patientY = patientY)
