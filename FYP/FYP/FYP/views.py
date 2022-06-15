"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from FYP import app


from flask import Flask,render_template, request, redirect, url_for
from flask_mysqldb import MySQL
 
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'restaurantapp' #change into your own database
 
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
    