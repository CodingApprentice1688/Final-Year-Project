"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request, Flask
from FYP import app

@app.route('/')
@app.route('/test')
def test():  
     return render_template('testIndex.html')  
 
 
  
@app.route('/helloPage', methods=['POST'])  
def hello():  
    first_name = request.form['first_name']  
    last_name = request.form['last_name']  
    data=' %s %s ' % (first_name, last_name)  
    return render_template('helloPage.html',value=data)  