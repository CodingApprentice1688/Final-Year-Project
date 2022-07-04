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