from FYP import app 
from FYP.entity.User import *
from datetime import datetime, date
from flask import render_template
from FYP import mysql
import shutil

from flask import Flask,render_template, request, redirect, url_for, Response, session
from flask_mysqldb import MySQL
import MySQLdb.cursors 

@app.route('/LogoutController')
def validateLogout():
    User.validateLogout();
    try:
        shutil.rmtree("FYP/static/patientimages")
    except:
        pass
    try:
        shutil.rmtree("FYP/static/doctorimages")
    except:
        pass
    try:
        shutil.rmtree("FYP/static/temp")
    except:
        pass
    try:
        shutil.rmtree("FYP/static/pati")
    except:
        pass
    return render_template('login.html')
