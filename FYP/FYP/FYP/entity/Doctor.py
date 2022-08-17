from datetime import datetime, date
from flask import render_template
from FYP import app
from FYP import mysql

from flask import Flask,render_template, request, redirect, url_for, Response, session
from flask_mysqldb import MySQL
import MySQLdb.cursors 


class Doctor:

    def StaffSearchDoctorController(name):
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute ("SELECT * FROM doctor WHERE dname LIKE %s", ('%' + name + '%', ) )
        doctor = cursor.fetchall()
        return (doctor)