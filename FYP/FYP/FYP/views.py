"""
Routes and views for the flask application.
"""

from datetime import datetime, date
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
@app.route('/LoginPage')
def LoginPage():
    """Renders a sample page."""
    return render_template(
        'login.html'
    )

@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )
@app.route('/Patient_Main')
def Patient_Main():
    """Renders the home page."""
    year = datetime.now().date()
    message = ''
    msg = ''
    if 'logged_in' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE username = % s AND nric = % s',  (session['username'], session['nric'], ))
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
        cursor.execute('SELECT * FROM user WHERE username = % s AND nric = % s',  (session['username'], session['nric'], ))
        userA = cursor.fetchone()
        if userA:
          return render_template('StaffMain.html', userA = userA,  message = message, year = year)
    return render_template('StaffMain.html', message = message, year = year)
    


@app.route('/ITAdmin_Main')
def ITAdmin_Main():
    """Renders a sample page."""
    return render_template(
        'testITAdmin.html',
        title='hello',
        year=datetime.now().year,
        message='This page is for IT Admin '
    )
@app.route('/Manage_Credentials')
def Manage_Credentials():
    """Renders a sample page."""
    return render_template(
        'testITAdmin.html',
        title='hello',
        year=datetime.now().year,
        message='IT Admin to manage credentials '
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
            session['name'] = userL['name']
            session['nric'] = userL['nric']
            session['role_type'] = userL['role']
            msg = 'Logged in successfully !'
            #return render_template('index_Main.html', msg = msg)
            if userL['role'] == 'healthcare staff':
                return redirect(url_for('HealthcareStaff_Main'))
            if userL['role'] == 'patient':
                return redirect(url_for('Patient_Main'))
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

#patient view all appointments
@app.route('/PatientViewAppointment', methods=['GET', 'POST'])
def PatientViewAppointment():
    message = ''
    msg = ''
    if 'logged_in' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        current = datetime.now().date()
        cursor.execute('SELECT * FROM appointments WHERE name = % s AND nric = % s AND date_slot >= CURDATE()',  (session['name'], session['nric'], ))
        userA = cursor.fetchall()
        cursor.execute("SELECT * FROM appointments WHERE name = % s AND nric = % s AND date_slot < CURDATE()" ,  (session['name'], session['nric'], ))
        userB = cursor.fetchall()
        

        return render_template('Patient_ViewAppointment.html', userA = userA, userB = userB)
    return render_template('Patient_ViewAppointment.html', userA = userA, userB = userB)


#patient get queue number
@app.route('/PatientQueueNumber', methods=['GET', 'POST'])
def PatientQueueNumber():
    """Renders the contact page."""
    return render_template(
        'PatientQueueNumber.html',
        title='PatientQueueNumber',
        year=datetime.now().year,
        #message='Your contact page.'
    )

@app.route('/QueueNumberController', methods = ['POST'])
def QueueNumberController():
    VideoCamera().stop_camera()
    return redirect(url_for('Patient_Main'))

#patient update personal details
@app.route('/PatientUpdatePersonalDetail', methods=['GET', 'POST'])
def PatientUpdatePersonalDetail():
    """Renders the contact page."""
    return render_template(
        'PatientUpdatePersonalDetail.html',
        title='PatientUpdatePersonalDetail',
        year=datetime.now().year,
        #message='Your contact page.'
    )
    

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





# test insert in sql
@app.route('/formPage', methods =['POST', 'GET'])
def submitForm():
   if request.method == 'POST':
        role = request.form['roleName']
        cursor = mysql.connection.cursor()
        cursor.execute(""" INSERT INTO ROLE (roleName) VALUES(%s)""" , [role])
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for('test'))

@app.route('/StaffSearchPatient')
def StaffSearchPatient():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    patient = 'patient'
    cursor.execute('SELECT * FROM user where role = % s', (patient, ))
    patient = cursor.fetchall()
    return render_template('StaffSearchPatient.html', patient = patient)




#healthcare staff to create medical records
@app.route('/StaffCreateMedicalRecord')
def StaffCreateMedicalRecord():
    """Renders the about page."""
    return render_template(
        'StaffCreateMedicalRecord.html',
        title='Staff Create Record',
        year=datetime.now().year)

@app.route('/StaffUpdateMedicalRecord')
def StaffUpdateMedicalRecord():
    """Renders the about page."""
    return render_template(
        'StaffUpdateMedicalRecord.html',
        title='Staff Update Record',
        year=datetime.now().year)

       
@app.route('/StaffCreateAppointment')
def StaffCreateAppointment():
    """Renders the about page."""
    return render_template(
        'StaffCreateAppointment.html',
        title='Staff Create Appointment',
        year=datetime.now().year)



@app.route('/StaffViewMedicalRecord', methods=['GET', 'POST'])
def StaffViewMedicalRecord():
    """Renders the about page."""
    return render_template(
        'StaffViewMedicalRecord.html',
        title='Staff View Medical Record',
        year=datetime.now().year)       


@app.route('/StaffViewPatientAppointment', methods=['GET', 'POST'])
def StaffViewPatientAppointment():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    username = request.form['username']
    nric = request.form['nric']
    current = datetime.now().date()
    cursor.execute('SELECT * FROM appointments WHERE username = % s AND nric = % s AND date_slot >= CURDATE()',  (username, nric, ))
    userA = cursor.fetchall()
    cursor.execute("SELECT * FROM appointments WHERE username = % s AND nric = % s AND date_slot < CURDATE()" ,  (username, nric, ))
    userB = cursor.fetchall()
        

    return render_template('Patient_ViewAppointment.html', userA = userA, userB = userB)