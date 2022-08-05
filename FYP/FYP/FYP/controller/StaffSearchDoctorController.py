from FYP import app
from FYP.entity.User import *
from FYP.entity.Appointments import *
from datetime import datetime, date
from flask import render_template
from FYP import mysql

from flask import Flask,render_template, request, redirect, url_for, Response, session
from flask_mysqldb import MySQL
import MySQLdb.cursors 


@app.route('/StaffSearchDoctorController', methods=['GET', 'POST'])
def StaffSearchDoctorController():
    if request.method == "POST":
        name = request.form['name']
        doctor = User.StaffSearchDoctorController(name)
        return render_template('StaffSearchDoctor.html', doctor = doctor)
    else:
        doctor = 'doctor'
        doctor = User.StaffSearchDoctor(doctor)
        return render_template('StaffSearchDoctor.html', doctor = doctor)