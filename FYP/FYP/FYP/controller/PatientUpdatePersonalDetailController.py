from FYP import app 
from FYP.entity.User import *
from FYP.entity.Appointments import *
from datetime import datetime, date
from flask import render_template
from FYP import mysql

from flask import Flask,render_template, request, redirect, url_for, Response, session
from flask_mysqldb import MySQL
import MySQLdb.cursors

@app.route('/PatientUpdatePersonalDetail', methods=['GET', 'POST'])
def PatientUpdateSession():
    #if 'logged_in' in session:
    userA = User.PatientUpdateSession()
    return render_template('PatientUpdatePersonalDetail.html', userA = userA)

@app.route('/PatientUpdatePersonalDetailController', methods=['GET', 'POST'])
def updatePersonalDetail():
    name = request.form['name']
    nric = request.form['nric']
    age = request.form['age']
    gender = request.form['gender']
    username = request.form['username']
    password = request.form['password']
    currusername = request.form['currusername']


    #if 'logged_in' in session:
    userA, error = User.updatePersonalDetail(name, nric, age, gender, username, password, currusername)
    return render_template('PatientUpdatePersonalDetail.html', userA = userA, error = error)