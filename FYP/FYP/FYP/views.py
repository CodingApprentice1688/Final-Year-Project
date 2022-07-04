"""
Routes and views for the flask application.
"""

from datetime import datetime, date
from flask import render_template
from FYP import app
from FYP import mysql
from .camera import VideoCamera

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





""" login manually """
#@app.route('/login', methods=['GET', 'POST'])
#def login():
#    error = None
#    msg = ''
#    if request.method == 'POST':        
#        username = request.form['username']
#        password = request.form['password']
#        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#        cursor.execute('SELECT * FROM user WHERE username = % s AND password = % s', (username, password, ))
#        userL = cursor.fetchone()
#        if userL:
#            session['logged_in'] = True
#            session['username'] = userL['username']
#            session['name'] = userL['name']
#            session['nric'] = userL['nric']
#            session['role_type'] = userL['role']
#            msg = 'Logged in successfully !'
            #return render_template('index_Main.html', msg = msg)
#            if userL['role'] == 'healthcare staff':
#                return redirect(url_for('HealthcareStaff_Main'))
#            if userL['role'] == 'patient':
#                return redirect(url_for('Patient_Main'))
#            if userL['role'] == 'IT admin':
#                return redirect(url_for('Admin_Main'))    
            #return redirect(url_for('main'))

#        else:
#           error = 'Invalid Credentials. Please try again.'
#    return render_template('login.html', error = error)

#@app.route('/logout')
#def logout():
#    session.pop('logged_in', None)
#    session.pop('username', None)
#    return render_template('login.html')

#@app.route('/PatientViewAppointment')
#def PatientViewAppointment():
#    userA = ""
#    userB = ""
#    return render_template('PatientViewAppointment.html', userA = userA, userB = userB)

#patient view all appointments
#@app.route('/PatientViewAppointment', methods=['GET', 'POST'])
#def PatientViewAppointment():
#    message = ''
#    msg = ''
#    if 'logged_in' in session: 
#        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#        current = datetime.now().date()
#        cursor.execute('SELECT * FROM appointments WHERE nric = % s AND date_slot >= CURDATE()' ,  (session['nric'], ))
#        userA = cursor.fetchall()
#        cursor.execute('SELECT * FROM appointments WHERE nric = % s AND date_slot < CURDATE()' ,  (session['nric'], ))
#        userB = cursor.fetchall()
        

#        return render_template('PatientViewAppointment.html', userA = userA, userB = userB)
#patient view all appointments

#@app.route('/PatientCancelAppointment', methods=['GET', 'POST'])
#def PatientCancelAppointment():
#    message = ''
#    msg = ''
#    if 'logged_in' in session: 
#        app_id = request.form['appointment_id']
#        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#        cursor.execute('DELETE FROM appointments WHERE appointment_id = % s' ,  (app_id, ))
#        mysql.connection.commit()
#        cursor.execute('SELECT * FROM appointments WHERE nric = % s AND date_slot >= CURDATE()',  (session['nric'], ))
#        userA = cursor.fetchall()
#        cursor.execute('SELECT * FROM appointments WHERE nric = % s AND date_slot < CURDATE()',  (session['nric'], ))
#        userB = cursor.fetchall()
#        return render_template('Patient_ViewAppointment.html', userA = userA, userB = userB)




#patient get queue number
#@app.route('/PatientQueueNumber', methods=['GET', 'POST'])
#def PatientQueueNumber():
#    return render_template(
#        'PatientQueueNumber.html',
#        title='PatientQueueNumber',
#        year=datetime.now().year
#    )

#@app.route('/QueueNumberController', methods = ['POST'])
#def QueueNumberController():
#    VideoCamera().stop_camera()
#    return redirect(url_for('Patient_Main'))

#patient update personal details
#@app.route('/PatientUpdatePersonalDetail', methods=['GET', 'POST'])
#def PatientUpdatePersonalDetail():
#    if 'logged_in' in session: 
#        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#        cursor.execute('SELECT * FROM user WHERE nric = % s' , (session['nric'], ))
#        userA = cursor.fetchall()
#    return render_template('PatientUpdatePersonalDetail.html', userA = userA)

#@app.route('/PatientUpdatePersonalDetailController', methods=['GET', 'POST'])
#def PatientUpdatePersonalDetailController():
#    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#    name = request.form['name']
#    nric = request.form['nric']
#    age = request.form['age']
#    gender = request.form['gender']
#    username = request.form['username']
#    password = request.form['password']

#    if 'logged_in' in session: 
#        cursor.execute('UPDATE user SET name = % s, nric = % s, age = % s, gender = % s, username = % s, password = % s WHERE nric = % s' , (name, nric, age, gender, username, password, session['nric'], ))
#        mysql.connection.commit()
#        cursor.execute('SELECT * FROM user WHERE nric = % s', (nric,))
#        userA = cursor.fetchall()
#    return render_template('PatientUpdatePersonalDetail.html', userA = userA)

    

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




#@app.route('/StaffSearchPatient', methods=['GET', 'POST'])
#def StaffSearchPatient():
#    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#    patient = 'patient'
#    cursor.execute('SELECT * FROM user where role = % s', (patient, ))
#    patient = cursor.fetchall()
#    return render_template('StaffSearchPatient.html', patient = patient)


#@app.route('/StaffSearchPatientController', methods=['GET', 'POST'])
#def StaffSearchPatientController():
#    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#    name = request.form['name']
#    pat = 'patient'
#   # ('SELECT * FROM user where name LIKE %%s% AND role = % s', (name, pat, ))
#    cursor.execute ("SELECT * FROM user WHERE name LIKE %s AND role = %s", ('%' + name + '%', pat, ))
#    patient = cursor.fetchall()

#    return render_template('StaffSearchPatient.html', patient = patient)



#@app.route('/StaffViewPatientAppointment', methods=['GET', 'POST'])
#def StaffViewPatientAppointment():
#    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#    username = request.form['username']
#    nric = request.form['nric']
#    current = datetime.now().date()
#    cursor.execute('SELECT * FROM appointments WHERE username = % s AND nric = % s AND date_slot >= CURDATE()',  (username, nric, ))
#    userA = cursor.fetchall()
#    cursor.execute("SELECT * FROM appointments WHERE username = % s AND nric = % s AND date_slot < CURDATE()" ,  (username, nric, ))
#    userB = cursor.fetchall()
    
#    cursor.execute('SELECT * FROM user WHERE username = % s AND nric = % s',  (username, nric, ))
#    patientX = cursor.fetchall()
#    session['patientX'] = patientX  ##

#    return render_template('StaffViewPatientAppointment.html', userA = userA, userB = userB)



#@app.route('/StaffCreateAppointment', methods=["POST", "GET"])
#def StaffCreateAppointment():

#    patientX = session["patientX"]  ##

#    return render_template(
#        'StaffCreateAppointment.html',
#        title='Staff Create Appointment',
#        patientX = patientX)



#@app.route('/StaffCreateAppointmentController', methods=['GET', 'POST'])
#def StaffCreateAppointmentController():
#    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    
#    params = {
#        'username' : request.form['username'],
#        'name' : request.form['name'],
#        'nric' : request.form['nric'],
#        'date_slot' : request.form['date_slot'],
#        'app_time' : request.form['app_time'],
#        'department' : request.form['department'],
#        'doctor' : request.form['doctor'],
#        'reason' : request.form['reason']
#    }
#    query = """INSERT INTO appointments (username, name, nric, date_slot, app_time, department, attending, reason) 
#               VALUES (%(username)s, %(name)s, %(nric)s, %(date_slot)s, %(app_time)s, %(department)s, %(doctor)s, %(reason)s)"""
#    cursor.execute(query, params)
#    mysql.connection.commit()

#    params = {
#        'username' : request.form['username'],
#        'nric' : request.form['nric']
#    }
#    query = """SELECT * FROM user WHERE username = %(username)s AND nric = %(nric)s"""
#    cursor.execute(query, params)
#    patientX = cursor.fetchall() 
    
#    return render_template('StaffCreateAppointment.html', patientX = patientX)



#@app.route('/StaffViewMedicalRecord', methods=['GET', 'POST'])
#def StaffViewMedicalRecord():

#    username = request.form['username']
#    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    
#    params = {'username' : request.form['username']}
#    query = """SELECT * FROM medicalrecords WHERE username = %(username)s"""
#    cursor.execute(query, params)
#    patientX = cursor.fetchall()

#    param = {'username' : request.form['username']}
#    query = """SELECT * FROM user WHERE username = %(username)s"""
#    cursor.execute(query, param)
#    patientY = cursor.fetchall()
#    session['patientY'] = patientY

#    return render_template('StaffViewMedicalRecord.html', patientX = patientX)



@app.route('/StaffCreateMedicalRecord')
def StaffCreateMedicalRecord():
    
    patientY = session["patientY"]  ##

    return render_template(
        'StaffCreateMedicalRecord.html',
        title='Staff Create Record',
        patientY = patientY)



@app.route('/StaffCreateMedicalRecordController', methods=['GET', 'POST'])
def StaffCreateMedicalRecordController():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

    params = {
        'appointment_id' : request.form['appointment_id'],
        'username' : request.form['username'],
        'vaccination_status' : request.form['vaccination_status'],
        'blood_pressure' : request.form['blood_pressure'],
        'temperature' : request.form['temperature'],
        'heart_rate' : request.form['heart_rate'],
        'allergies' : request.form['allergies'],
        'medicine' : request.form['medicine'],
        'diagnosis' : request.form['diagnosis']
    }
    query = """INSERT INTO medicalrecords (appointment_id, username, vaccination_status, blood_pressure, temperature, heart_rate, allergies, medicine, diagnosis) 
               VALUES (%(appointment_id)s, %(username)s, %(vaccination_status)s, %(blood_pressure)s, %(temperature)s, %(heart_rate)s, %(allergies)s, %(medicine)s, %(diagnosis)s)"""
    cursor.execute(query, params)
    mysql.connection.commit()

    param = {'username' : request.form['username']}
    query = """SELECT * FROM medicalrecords WHERE username = %(username)s"""
    cursor.execute(query, param)
    patientY = cursor.fetchall()  ##
    
    return render_template('StaffCreateMedicalRecord.html', patientY = patientY)



@app.route('/StaffUpdateMedicalRecord', methods=['GET', 'POST'])
def StaffUpdateMedicalRecord():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    param = {'record_id' : request.form['record_id']}
    query = """SELECT * FROM medicalrecords WHERE record_id = %(record_id)s"""
    cursor.execute(query, param)
    recordX = cursor.fetchall()

    return render_template('StaffUpdateMedicalRecord.html', title='Staff Update Record', recordX = recordX)



@app.route('/StaffUpdateMedicalRecordController', methods=['GET', 'POST'])
def StaffUpdateMedicalRecordController():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

    params = {
        'record_id' : request.form['record_id'],
        'appointment_id' : request.form['appointment_id'],
        'username' : request.form['username'],
        'vaccination_status' : request.form['vaccination_status'],
        'blood_pressure' : request.form['blood_pressure'],
        'temperature' : request.form['temperature'],
        'heart_rate' : request.form['heart_rate'],
        'allergies' : request.form['allergies'],
        'medicine' : request.form['medicine'],
        'diagnosis' : request.form['diagnosis']
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

    param = {'record_id' : request.form['record_id']}
    query = """SELECT * FROM medicalrecords WHERE record_id = %(record_id)s"""
    cursor.execute(query, param)
    recordX = cursor.fetchall()

    return render_template('StaffUpdateMedicalRecord.html', recordX = recordX)





@app.route('/AdminSearchPatient', methods=['GET', 'POST'])
def AdminSearchPatient():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    patient = 'patient'
    cursor.execute('SELECT * FROM user where role = % s', (patient, ))
    patient = cursor.fetchall()
    
    """Renders the about page."""
    return render_template(
        'AdminSearchPatient.html', patient = patient)

@app.route('/AdminSearchPatientController', methods=['GET', 'POST'])
def AdminSearchPatientController():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    name = request.form['name']
    pat = 'patient'
   # ('SELECT * FROM user where name LIKE %%s% AND role = % s', (name, pat, ))
    cursor.execute ("SELECT * FROM user WHERE name LIKE %s AND role = %s", ('%' + name + '%', pat, ))
    patient = cursor.fetchall()
    return render_template('AdminSearchPatient.html', patient = patient)

@app.route('/AdminRegisterPatient')
def AdminRegisterPatient():
    """Renders the about page."""
    ten = 0
    return render_template(
        'AdminRegisterPatient.html', ten = ten)

#@app.route('/AdminRegisterPatientController', methods=['GET', 'POST'])
#def AdminRegisterPatientController():
#    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#    name = request.form['name']
#    nric = request.form['nric']
#    age = request.form['age']
#    gender = request.form['gender']
#    username = request.form['username']
#    password = request.form['password']
#    role = 'patient'
#    ten = 0

#   # ('SELECT * FROM user where name LIKE %%s% AND role = % s', (name, pat, ))
#    cursor.execute ("INSERT INTO user (name, nric, age, gender, username, password, role) VALUES (% s, % s, % s, % s, % s, % s, % s)", (name, nric, age, gender, username, password, role, ))
#    mysql.connection.commit()
#    return render_template('AdminRegisterPatient.html', ten = ten)


@app.route('/AdminChangePatientImage',  methods=['GET', 'POST'])
def AdminChangePatientImage():
    """Renders the about page."""
    ten = 0
    allow = 'none'
    return render_template(
        'AdminChangePatientImage.html', ten = ten, allow = allow)