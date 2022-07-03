from FYP import app 
from FYP.entity.User import *
from datetime import datetime, date
from flask import render_template
from FYP import mysql

from flask import Flask,render_template, request, redirect, url_for, Response, session
from flask_mysqldb import MySQL
import MySQLdb.cursors 

@app.route('/LoginController', methods=['GET', 'POST'])
def validateLogin():
    #error = None
    msg = 'Logged in successfully !'   
    error = 'Invalid Credentials. Please try again.'
    username = request.form['username']
    password = request.form['password']
    error = User.validateLogin(username, password)

    return render_template('login.html', error = error)

