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
            msg = 'Logged in successfully !'
            if userL['role'] == 'healthcare staff':
                return redirect(url_for('HealthcareStaff_Main'))
            if userL['role'] == 'patient':
                return redirect(url_for('Patient_Main'))
            if userL['role'] == 'IT admin':
                 return redirect(url_for('Admin_Main'))    

        else:
           error = 'Invalid Credentials. Please try again.'

    def viewAppointment():
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM appointments WHERE nric = % s AND date_slot >= CURDATE()' ,  (session['nric'], ))
        userA = cursor.fetchall()
        cursor.execute('SELECT * FROM appointments WHERE nric = % s AND date_slot < CURDATE()' ,  (session['nric'], ))
        userB = cursor.fetchall()
        return (userA, userB)

    def cancelAppointment(appointment_id):
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('DELETE FROM appointments WHERE appointment_id = % s' ,  (appointment_id, ))
        mysql.connection.commit()
        cursor.execute('SELECT * FROM appointments WHERE nric = % s AND date_slot >= CURDATE()',  (session['nric'], ))
        userA = cursor.fetchall()
        cursor.execute('SELECT * FROM appointments WHERE nric = % s AND date_slot < CURDATE()',  (session['nric'], ))
        userB = cursor.fetchall()
        return (userA, userB)
        