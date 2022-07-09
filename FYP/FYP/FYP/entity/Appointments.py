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
    

    def StaffCreateAppointment(username, name, nric, date_slot, app_time, department, doctor, reason):
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        params = {
            'username' : username,
            'name' : name,
            'nric' : nric,
            'date_slot' : date_slot,
            'app_time' : app_time,
            'department' : department,
            'doctor' : doctor,
            'reason' : reason
        }
        query = """INSERT INTO appointments (username, name, nric, date_slot, app_time, department, attending, reason) 
                   VALUES (%(username)s, %(name)s, %(nric)s, %(date_slot)s, %(app_time)s, %(department)s, %(doctor)s, %(reason)s)"""
        cursor.execute(query, params)
        mysql.connection.commit()

        params = {'username' : username,'nric' : nric}
        query = """SELECT * FROM user WHERE username = %(username)s AND nric = %(nric)s"""
        cursor.execute(query, params)
        patientX = cursor.fetchall()
        return (patientX)


    def QueueUpdateSession():
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM appointments WHERE nric = % s' , (session['nric'], ))
        userA = cursor.fetchall()
        return (userA)

    def updateQueueNumber(queueNumber):
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('UPDATE appointments SET queue_number = % s WHERE nric = % s' , (queueNumber, session['nric'], ))
        mysql.connection.commit()
        cursor.execute('SELECT * FROM appointments WHERE nric = % s', (session['nric'], ))
        userA = cursor.fetchall()
        return (userA)