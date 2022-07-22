
from FYP import app 
from FYP.entity.User import *
from FYP.entity.Appointments import *
from datetime import datetime, date
from flask import render_template
from FYP import mysql
"""if LoginController.py is not detected, 
you can copy and deleted the original file, then recreate the new file"""
from flask import Flask,render_template, request, redirect, url_for, Response, session
from flask_mysqldb import MySQL
import MySQLdb.cursors 

@app.route('/LoginController', methods=['GET', 'POST'])
def validateLogin():
    error = None
    msg = 'Logged in successfully !'   
    error = 'Invalid Credentials. Please try again.'
    username = request.form['username']
    password = request.form['password']
    result, userL = User.validateLogin(username, password)

    if result:
        if userL['role'] == 'healthcare staff':
            return redirect("/HealthcareStaff_Main")
        if userL['role'] == 'patient':
            return redirect("/Patient_Main")
        if userL['role'] == 'IT admin':
            return redirect("/Admin_Main")   

    else:
        return render_template('login.html', error = error)



