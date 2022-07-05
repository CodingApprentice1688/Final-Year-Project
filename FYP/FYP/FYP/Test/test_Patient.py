import unittest
from unittest import TestCase
#from unittest.mock import patch, MagicMock
#import mysql.connector
#from mysql.connector import errorcode
#from mock import patch
#import utils
#from FYP.entity import User
from flask import Flask
#from FYP import app
#from app import app
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

    def test_Login(self):
        #result = 5+6
        #self.assertEqual(result, 11)
        #with self.client:
        #    response = self.client.post('login', { username: 'James', password: '007' })
            # success
        #    assertEquals(user.username, 'James')
        with app.test_client() as client:
            client.post('/LoginController', data=dict(username='s', password='s'))
            with client.session_transaction() as session:
                #self.assertTrue(session['logged_in'])
                self.assertEqual(session['username'], 'wenling')
                self.assertEqual(session['password'], 'password')
            #self.assertTrue(username == 'wenling')
            #self.assertTrue(password == 'password')


if __name__ == '__main__':
    unittest.main()