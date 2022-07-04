from datetime import datetime, date
from flask import render_template
from FYP import app
from FYP import mysql

from flask import Flask,render_template, request, redirect, url_for, Response, session
from flask_mysqldb import MySQL
import MySQLdb.cursors 




class Appointments:


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

    def StaffViewPatientAppointment(username, nric):
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        current = datetime.now().date()
        cursor.execute('SELECT * FROM appointments WHERE username = % s AND nric = % s AND date_slot >= CURDATE()',  (username, nric, ))
        userA = cursor.fetchall()
        cursor.execute("SELECT * FROM appointments WHERE username = % s AND nric = % s AND date_slot < CURDATE()" ,  (username, nric, ))
        userB = cursor.fetchall()
        cursor.execute('SELECT * FROM user WHERE username = % s AND nric = % s',  (username, nric, ))
        patientX = cursor.fetchall()
        return (userA, userB, patientX)


