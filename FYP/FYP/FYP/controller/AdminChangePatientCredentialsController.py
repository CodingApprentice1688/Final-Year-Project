

from FYP import app 
from FYP.entity.User import *
from FYP.entity.Appointments import *
from datetime import datetime, date
from flask import render_template
from FYP import mysql
from FYP import storage
from FYP.camera import VideoCamera
import os


from flask import Flask,render_template, request, redirect, url_for, Response, session
from flask_mysqldb import MySQL
import MySQLdb.cursors 

@app.route('/AdminChangePatientCredentials',  methods=['GET', 'POST'])
def AdminChangePatientCredentials():
    nric = request.form['nric']

    userA = User.getPatientCreds(nric)
    """Renders the about page."""
    return render_template(
        'AdminChangePatientCredentials.html', userA = userA, error = '')


@app.route('/AdminChangePatientCredentialsController',  methods=['GET', 'POST'])
def adminUpdatePersonalDetails():
    name = request.form['name']
    nric = request.form['nric']
    age = request.form['age']
    gender = request.form['gender']
    username = request.form['username']
    password = request.form['password']

    userA = User.updatePersonalDetail(name, nric, age, gender, username, password, 'admin')
    """Renders the about page."""
    return render_template(
        'AdminChangePatientCredentials.html', userA = userA, error = '')





#class AdminRegisterPatientController:
    

#    def RegisterPatient():
#        name = request.form['name']
#        nric = request.form['nric']
#        age = request.form['age']
#        gender = request.form['gender']
#        username = request.form['username']
#        password = request.form['password']
#        role = 'patient'
        
#        user = User()
#        user.AdminRegisterPatient(name, nric, age, gender, username, password, role)




    
    