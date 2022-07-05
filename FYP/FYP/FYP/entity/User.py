from datetime import datetime, date
from flask import render_template
from FYP import app
from FYP import mysql

from flask import Flask,render_template, request, redirect, url_for, Response, session
from flask_mysqldb import MySQL
import MySQLdb.cursors 




class User:
    def registerPatient(name, nric, age, gender, username, password, role):
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    
        ten = 0

       # ('SELECT * FROM user where name LIKE %%s% AND role = % s', (name, pat, ))
        cursor.execute ("INSERT INTO user (name, nric, age, gender, username, password, role) VALUES (% s, % s, % s, % s, % s, % s, % s)", (name, nric, age, gender, username, password, role, ))
        mysql.connection.commit()
    def validateLogin(username, password):
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE username = % s AND password = % s', (username, password, ))
        userL = cursor.fetchone()
        if userL:
            session['logged_in'] = True
            session['username'] = userL['username']
            session['name'] = userL['name']
            session['nric'] = userL['nric']
            session['role_type'] = userL['role']
            return True, userL 

        else:
           return False, userL
    def validateLogout():
        session.pop('logged_in', None)
        session.pop('username', None)
        return render_template('login.html')

    #patient update personal details
    def PatientUpdateSession():
        #if 'logged_in' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE nric = % s' , (session['nric'], ))
        userA = cursor.fetchall()
        return (userA)

    def updatePersonalDetail(name, nric, age, gender, username, password):
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('UPDATE user SET name = % s, nric = % s, age = % s, gender = % s, username = % s, password = % s WHERE nric = % s' , (name, nric, age, gender, username, password, nric, ))
        mysql.connection.commit()
        cursor.execute('SELECT * FROM user WHERE nric = % s', (nric, ))
        userA = cursor.fetchall()
        return (userA)

    def getPatientCreds(nric):
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        patient = 'patient'
        cursor.execute('SELECT * FROM user WHERE nric = % s AND role = % s' , (nric, patient, ))
        userA = cursor.fetchall()
        return (userA)


    def getImageInfo(username):
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE username = % s', (username, ))
        userL = cursor.fetchone()
        if userL:
            session['logged_in'] = True
            session['username'] = userL['username']
            session['name'] = userL['name']
            session['nric'] = userL['nric']
            session['role_type'] = userL['role']
            return userL 

        else:
           return userL