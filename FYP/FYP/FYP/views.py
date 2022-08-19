"""
Routes and views for the flask application.
"""

from datetime import datetime, date
from flask import render_template
from FYP import app
from FYP import mysql
from .camera import VideoCamera
import shutil

from flask import Flask,render_template, request, redirect, url_for, Response, session
from flask_mysqldb import MySQL
import MySQLdb.cursors 




@app.route('/')
@app.route('/LoginPage')
def LoginPage():
    """Renders a sample page."""
    return render_template(
        'login.html'
    )


@app.route('/Patient_Main')
def Patient_Main():
    """Renders the home page."""
    year = datetime.now().date()
    message = ''
    msg = ''
    if 'logged_in' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE nric = % s',  (session['nric'], ))
        userA = cursor.fetchone()
        if userA:
          return render_template('PatientMain.html', userA = userA,  message = message, year = year)
    return render_template('PatientMain.html', message = message, year = year)


@app.route('/HealthcareStaff_Main')
def HealthcareStaff_Main():
    """Renders the home page."""
    year = datetime.now().date()
    message = ''
    msg = ''
    if 'logged_in' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE nric = % s',  (session['nric'], ))
        userA = cursor.fetchone()
        if userA:
          return render_template('StaffMain.html', userA = userA,  message = message, year = year)
    return render_template('StaffMain.html', message = message, year = year)
    


@app.route('/Admin_Main')
def Admin_Main():
    """Renders the home page."""
    try:
        shutil.rmtree("FYP/static/temp")
    except:
        pass
    try:
        shutil.rmtree("FYP/static/pati")
    except:
        pass
    try:
        shutil.rmtree("FYP/deeplearning/train")
    except:
        pass
    try:
        shutil.rmtree("FYP/deeplearning/val")
    except:
        pass
    year = datetime.now().date()
    message = ''
    msg = ''
    if 'logged_in' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE nric = % s',  (session['nric'], ))
        userA = cursor.fetchone()
        if userA:
          return render_template('AdminMain.html', userA = userA,  message = message, year = year)
    return render_template('AdminMain.html', message = message, year = year)



def gen(camera):
    while True:
        frame = camera.get_frame()
        if frame is not None:
            yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')




@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')




@app.route('/capture_10_pics')
def capture_10_pics():
    VideoCamera().capture_10_pics();
    ten = 10
    return render_template('AdminRegisterPatient.html', ten = ten)

@app.route('/capture_10_pics_change')
def capture_10_pics_change():
    VideoCamera().capture_10_pics();
    ten = 10
    allow = 'block'
    return render_template('AdminChangePatientImage.html', ten = ten, allow = allow)




