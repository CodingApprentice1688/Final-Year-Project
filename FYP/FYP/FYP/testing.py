"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request, Flask
from FYP import app

@app.route('/')
@app.route('/testHello')
def testHello():
    """Renders the home page."""
    return render_template(
        'helloPage.html',
        title='hello Page',
        year=datetime.now().year,
        message='This is a Hello page.'
    )
 
  
