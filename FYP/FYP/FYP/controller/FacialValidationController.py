from FYP import app 
from FYP.entity.User import *
from FYP.entity.Appointments import *
from datetime import datetime, date
from flask import render_template
from FYP import mysql

from flask import Flask,render_template, request, redirect, url_for, Response, session
from flask_mysqldb import MySQL
import MySQLdb.cursors 






@app.route('/FacialValidationController', methods=['POST', 'GET'])
def validateNRIC():

    nric = request.form['nric']
    result, userL = User.validateNRIC(nric)

    if result:
        if userL['role_type'] == 'healthcare staff':
            return redirect("/HealthcareStaff_Main")
        if userL['role_type'] == 'patient':
            return redirect("/Patient_Main")
        if userL['role_type'] == 'IT admin':
            return redirect("/Admin_Main") 
    else:
        return render_template('login.html')