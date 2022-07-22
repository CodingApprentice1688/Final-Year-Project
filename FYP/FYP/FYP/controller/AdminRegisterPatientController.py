

from FYP import app 
from FYP.entity.User import *
from FYP.entity.Appointments import *
from datetime import datetime, date
from flask import render_template
from FYP import mysql

from flask import Flask,render_template, request, redirect, url_for, Response, session
from flask_mysqldb import MySQL
import MySQLdb.cursors 



"""https://towardsdatascience.com/do-you-know-python-has-a-built-in-database-d553989c87bd"""
#do cicd and unit testing 

#go to admin login, capture and copy paste into the DeepLearning\train and val folder
# find out the face recognition algorithm with auto adding

@app.route('/AdminRegisterPatientController', methods=['GET', 'POST'])
def registerPatient():
    
    name = request.form['name']
    nric = request.form['nric']
    age = request.form['age']
    gender = request.form['gender']
    username = request.form['username']
    password = request.form['password']
    role = 'patient'
    ten = 0
    
    User.registerPatient(name, nric, age, gender, username, password, role)
    return render_template('AdminRegisterPatient.html', ten = ten)


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




    
    