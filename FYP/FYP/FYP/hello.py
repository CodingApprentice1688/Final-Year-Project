"""
Routes and views for the flask application.
"""

from flask import render_template
from FYP import app

@app.route('/')
@app.route('/testIndex')
def testIndex():  
     return render_template('testIndex.html')  
 
 
  
@app.route('/hello', methods=['POST'])  
def hello():  
    first_name = request.form['first_name']  
    last_name = request.form['last_name']  
    data=' %s %s ' % (first_name, last_name)  
    return render_template('helloPage.html',value=data)  
     
