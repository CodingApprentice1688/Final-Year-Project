"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from FYP import app
from .camera import VideoCamera

from flask import Flask,render_template, request, redirect, url_for, Response, session
from flask_mysqldb import MySQL
import MySQLdb.cursors 

app.secret_key = 'facial_recognition'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'healthcare_db' #change into your own database
 
mysql = MySQL(app)

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )
@app.route('/main')
def main():
    """Renders the home page."""
    return render_template(
        'index_Main.html',
        title='Home Page',
        year=datetime.now().year,
    )
@app.route('/Appointments')
def viewAppointment():
    """Renders a sample page."""
    return render_template(
        'Patient_ViewAppointment.html',
        title='hello',
        year=datetime.now().year,
        message='All appointments'
    )
@app.route('/HealthcareStaff_Main')
def HealthcareStaff_Main():
    """Renders a sample page."""
    return render_template(
        'testHealthCareStaff.html',
        title='hello',
        year=datetime.now().year,
        message='This page is for healthcare staff'
    )
@app.route('/ITAdmin_Main')
def ITAdmin_Main():
    """Renders a sample page."""
    return render_template(
        'testITAdmin.html',
        title='hello',
        year=datetime.now().year,
        message='This page is for IT Admin '
    )

""" login manually """
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    msg = ''
    if request.method == 'POST':        
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE username = % s AND password = % s', (username, password, ))
        userL = cursor.fetchone()
        if userL:
            session['logged_in'] = True
            session['username'] = userL['username']
            session['role_type'] = userL['role']
            msg = 'Logged in successfully !'
            #return render_template('index_Main.html', msg = msg)
            if userL['role'] == 'healthcare staff':
                return redirect(url_for('HealthcareStaff_Main'))
            if userL['role'] == 'patient':
                return redirect(url_for('main'))
            if userL['role'] == 'IT admin':
                return redirect(url_for('ITAdmin_Main'))    
            #return redirect(url_for('main'))

        else:
            error = 'Invalid Credentials. Please try again.'
    return render_template('login.html', error = error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('username', None)
    return redirect(url_for('login'))

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/LoginController', methods = ['POST'])
def LoginController():
    VideoCamera().stop_camera()
    return redirect(url_for('home'))




@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
@app.route('/test')
def test():  
      return render_template(
        'helloPage.html',
        title='test',
        year=datetime.now().year,
        message='Under testing'
    )
 
 
@app.route('/hello')
def hello():
    """Renders a sample page."""
    return render_template(
        'helloPage.html',
        title='hello',
        year=datetime.now().year,
        message='Under testing'
    )






@app.route('/formPage', methods =['POST', 'GET'])
def submitForm():
   if request.method == 'POST':
        role = request.form['roleName']
        cursor = mysql.connection.cursor()
        cursor.execute(""" INSERT INTO ROLE (roleName) VALUES(%s)""" , [role])
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for('test'))

@app.route('/StaffCreateMedicalRecord')
def StaffCreateMedicalRecord():
    """Renders the about page."""
    return render_template(
        'StaffCreateMedicalRecord.html',
        title='Staff Create Record',
        year=datetime.now().year)



        #hello
