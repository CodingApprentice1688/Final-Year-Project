"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from FYP import app
from .camera import VideoCamera

from flask import Flask,render_template, request, redirect, url_for, Response
from flask_mysqldb import MySQL
 
 
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

@app.route('/login')
def login():
    """Renders the home page."""
    return render_template(
        'login.html',
        title='Login Page',
        year=datetime.now().year,
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


@app.route('/formPage', methods =['POST', 'GET'])
def submitForm():
   if request.method == 'POST':
        role = request.form['roleName']
        cursor = mysql.connection.cursor()
        cursor.execute(""" INSERT INTO ROLE (roleName) VALUES(%s)""" , [role])
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for('test'))
    