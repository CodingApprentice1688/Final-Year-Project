"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from FYP import app

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