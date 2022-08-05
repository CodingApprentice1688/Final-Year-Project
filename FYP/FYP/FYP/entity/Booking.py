from datetime import datetime, date
from flask import render_template
from FYP import app
from FYP import mysql

from flask import Flask,render_template, request, redirect, url_for, Response, session
from flask_mysqldb import MySQL
import MySQLdb.cursors 


class Booking:

    def StaffViewDoctorSchedule(dname):
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

        param = {'doctor' : dname,
                 'today' : date.today()}
        query = """SELECT * FROM booking WHERE doctor = %(doctor)s AND _date > %(today)s """
        cursor.execute(query, param)
        doctor = cursor.fetchall()

        return (doctor)