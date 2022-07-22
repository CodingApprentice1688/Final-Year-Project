import unittest
from unittest import TestCase
import os
from unittest.mock import patch
from unittest import mock
from flask import Flask,render_template, request, redirect, url_for, Response, session, jsonify
from flask_mysqldb import MySQL
from unittest.mock import create_autospec

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@127.0.0.1/healthcare_db'

"""Unit tests don’t deal with their environment and with external systems to the codebase.  If it you’ve written something that can fail
when run on a machine without the “proper setup,” you haven’t written a unit test."""

"""https://stackify.com/unit-testing-basics-best-practices/"""

class Test_admin_test_1(unittest.TestCase):

    def test_login_w_user(self):
        error = None
        msg = 'Logged in successfully !'   
        error = 'Invalid Credentials. Please try again.'
        username = request.form['username']
        password = request.form['password']
        result, userL = User.validateLogin(username, password)

        
        return redirect("/Admin_Main")   

    def test_login_w_face(self):


        

if __name__ == '__main__':
    unittest.main()
