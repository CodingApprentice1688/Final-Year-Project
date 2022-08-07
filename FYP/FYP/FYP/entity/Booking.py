from datetime import datetime, date
from flask import render_template
from FYP import app
from FYP import mysql

from flask import Flask,render_template, request, redirect, url_for, Response, session
from flask_mysqldb import MySQL
import MySQLdb.cursors 


class Booking:

    def StaffViewDoctorSchedule(dname, date_from, date_to):
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

        param = {'doctor' : dname,
                #  'today' : date.today(),
                 'date_from' : date_from,
                 'date_to' : date_to}
        # query = """SELECT * FROM booking WHERE doctor = %(doctor)s AND _date > %(today)s """
        query = """SELECT * FROM booking WHERE doctor = %(doctor)s AND (_date >= %(date_from)s AND _date <= %(date_to)s)"""
        cursor.execute(query, param)
        doctor = cursor.fetchall()

        return (doctor)


    def StaffCreateAppointment(doctor,date_slot,app_time):
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

        params = {'doctor' : doctor,
                 '_date' : date_slot,
                 'starttime' : app_time}
        query = """SELECT * FROM booking WHERE doctor = %(doctor)s AND _date = %(_date)s AND starttime = %(starttime)s """
        cursor.execute(query, params)
        appointment = cursor.fetchone()
        
        newavailability = appointment['availability'] - 1
        params = {'doctor' : doctor,
                 '_date' : date_slot,
                 'starttime' : app_time,
                 'newavailability' : newavailability}
        query = """UPDATE booking SET availability = %(newavailability)s WHERE doctor = %(doctor)s AND _date = %(_date)s AND starttime = %(starttime)s """
        cursor.execute(query, params)
        mysql.connection.commit()
