//test_patient.py

import unittest
from unittest import TestCase
#from unittest.mock import patch, MagicMock
#import mysql.connector
#from mysql.connector import errorcode
#from mock import patch
#from entity.User import User
from flask import Flask,render_template, request, redirect, url_for, Response, session
#from flask import Flask, session
from flask_mysqldb import MySQL
#from FYP import mysql
app = Flask(__name__)
class test_patient(unittest.TestCase):
    def setUp(self):
       self.app = app
       self.app.secret_key = 'facial_recognition'
       self.app.config['MYSQL_HOST'] = 'localhost'
       self.app.config['MYSQL_USER'] = 'root'
       self.app.config['MYSQL_PASSWORD'] = ''
       self.app.config['MYSQL_DB'] = 'healthcare_db' #change into your own database

       #self.app.secret_key = 'facial_recognition'
       #app.config['SECRET_KEY'] = 'facial_recognition'
       self.client = self.app.test_client()
       self.app = app.test_client()
       mysql = MySQL(app)
    
    def test_pass_correct(self):
        tester = app.test_client(self)
        response = tester.post('/LoginController', data=dict(username = 'wenling', password='password'))
        self.assertFalse(b'password' in response.data)
        #self.assertTrue(b'Field must be at least 8 characters long.' in response.data)
        #self.assertTrue(response)

    # Ensure that the password-tester behaves correctly given incorrect credentials
    def test_pass_incorrect(self):
        tester = app.test_client(self)
        response = tester.post('/LoginController', data=dict(username = 'wenling', password='password'))
        self.assertTrue(b'password' in response.data)
        #self.assertEqual(b'password' in response.data)
    def test_access_session(client):
        with client:
            client.post("/LoginController", data={"username": "wenling", "password": "password"})
            # session is still accessible
            self.assertTrue(session["username"], "wenling")
            self.assertTrue(session["password"], "password")

#    @app.route('/LoginController', methods=['GET', 'POST'])
#    def test_Login(self):
        #result = 5+6
        #self.assertEqual(result, 11)
 #       with self.client:
 #           response = self.client.post('login', { username: 'James', password: '007' })
            # success
#            assertEquals(user.username, 'James')
        
        #with app.test_client() as client:
        #    client.post('/LoginController', data=dict(username='s', password='s'))
        #    with client.session_transaction() as session:
                #self.assertTrue(session['logged_in'])
        #        self.assertTrue(session['logged_in'])

                #self.assertEqual(username, 'wenling')
                #self.assertEqual(password, 'password')
            #self.assertTrue(username == 'wenling')
            #self.assertTrue(password == 'password')


if __name__ == '__main__':
    unittest.main()
