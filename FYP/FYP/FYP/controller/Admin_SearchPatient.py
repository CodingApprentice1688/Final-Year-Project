
from FYP import app 
from FYP.entity.User import *
from datetime import datetime, date
from flask import render_template
from FYP import mysql

from flask import Flask,render_template, request, redirect, url_for, Response, session
from flask_mysqldb import MySQL
import MySQLdb.cursors 




#the current files 
@app.route('/AdminSearchPatient', methods=['GET', 'POST'])
def searchPatient():
    
    name = request.form['name']
    nric = request.form['nric']
    age = request.form['age']
    gender = request.form['gender']
    username = request.form['username']
    password = request.form['password']
    role = 'patient'
    ten = 0
    #need a line to take the search term from the AdminSearchPatient 
    User.registerPatient(name, nric, age, gender, username, password, role)
    return render_template('AdminSearchPatient.html', ten = ten)
