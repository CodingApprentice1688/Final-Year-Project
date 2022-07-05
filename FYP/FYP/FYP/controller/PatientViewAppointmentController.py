from FYP import app 
from FYP.entity.User import *
from FYP.entity.Appointments import *
from datetime import datetime, date
from flask import render_template
from FYP import mysql

from flask import Flask,render_template, request, redirect, url_for, Response, session
from flask_mysqldb import MySQL
import MySQLdb.cursors 
from flask_classful import FlaskView


class PatientViewAppointmentController:
    def __init__(self, ip, port): 
            self.ip = ip
            self.port = port
            self.app = Flask(__name__)
            self.some_attribute = 'PatientViewAppointmentController'

    @self.app.route('/PatientViewAppointmentController', methods=['GET', 'POST'])
    def viewAppointment(self):
        if 'logged_in' in session: 
            userA, userB = Appointments.viewAppointment()
            return render_template('PatientViewAppointment.html', userA = userA, userB = userB)

#PatientViewAppointmentController.register(app,route_base = '/')

#working without class
#@app.route('/PatientViewAppointmentController', methods=['GET', 'POST'])
#def viewAppointment():
#    if 'logged_in' in session: 
#        userA, userB = Appointments.viewAppointment()
#        return render_template('PatientViewAppointment.html', userA = userA, userB = userB)
