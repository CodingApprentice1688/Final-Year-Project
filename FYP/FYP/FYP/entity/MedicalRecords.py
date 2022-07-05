from datetime import datetime, date
from flask import render_template
from FYP import app
from FYP import mysql

from flask import Flask,render_template, request, redirect, url_for, Response, session
from flask_mysqldb import MySQL
import MySQLdb.cursors 


class MedicalRecords:


    def StaffViewMedicalRecord(username):
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

        param = {'username' : username}
        query = """SELECT * FROM medicalrecords WHERE username = %(username)s"""
        cursor.execute(query, param)
        patientX = cursor.fetchall()
        
        query = """SELECT * FROM user WHERE username = %(username)s"""
        cursor.execute(query, param)
        patientY = cursor.fetchall()
        return (patientX, patientY)

    def StaffCreateMedicalRecord(appointment_id, username, vaccination_status, blood_pressure, temperature, heart_rate, allergies, medicine, diagnosis):
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

        params = {
            'appointment_id' : appointment_id,
            'username' : username,
            'vaccination_status' : vaccination_status,
            'blood_pressure' : blood_pressure,
            'temperature' : temperature,
            'heart_rate' : heart_rate,
            'allergies' : allergies,
            'medicine' : medicine,
            'diagnosis' : diagnosis
        }
        query = """INSERT INTO medicalrecords (appointment_id, username, vaccination_status, blood_pressure, temperature, heart_rate, allergies, medicine, diagnosis) 
                   VALUES (%(appointment_id)s, %(username)s, %(vaccination_status)s, %(blood_pressure)s, %(temperature)s, %(heart_rate)s, %(allergies)s, %(medicine)s, %(diagnosis)s)"""
        cursor.execute(query, params)
        mysql.connection.commit()

        param = {'username' : username}
        query = """SELECT * FROM medicalrecords WHERE username = %(username)s"""
        cursor.execute(query, param)
        patientY = cursor.fetchall()  ##
        return (patientY)


    def StaffUpdateMedicalRecord(record_id):
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        param = {'record_id' : record_id}
        query = """SELECT * FROM medicalrecords WHERE record_id = %(record_id)s"""
        cursor.execute(query, param)
        recordX = cursor.fetchall()
        return (recordX)


    def StaffUpdateMedicalRecordController(record_id, appointment_id, username, vaccination_status, blood_pressure, temperature, heart_rate, allergies, medicine, diagnosis):
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        params = {
            'record_id' : record_id,
            'appointment_id' : appointment_id,
            'username' : username,
            'vaccination_status' : vaccination_status,
            'blood_pressure' : blood_pressure,
            'temperature' : temperature,
            'heart_rate' : heart_rate,
            'allergies' : allergies,
            'medicine' : medicine,
            'diagnosis' : diagnosis
        }
        query = """UPDATE medicalrecords 
                SET vaccination_status = %(vaccination_status)s, 
                    blood_pressure = %(blood_pressure)s, 
                    temperature = %(temperature)s, 
                    heart_rate = %(heart_rate)s, 
                    allergies = %(allergies)s, 
                    medicine = %(medicine)s, 
                    diagnosis = %(diagnosis)s
                WHERE record_id = %(record_id)s"""
        cursor.execute(query, params)
        mysql.connection.commit()

        param = {'record_id' : record_id}
        query = """SELECT * FROM medicalrecords WHERE record_id = %(record_id)s"""
        cursor.execute(query, param)
        recordX = cursor.fetchall()
        return (recordX)