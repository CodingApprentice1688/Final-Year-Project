import unittest
from unittest import TestCase
import os
#import FYP.controller.LoginController
from unittest.mock import patch
from unittest import mock
from flask import Flask,render_template, request, redirect, url_for, Response, session, jsonify
from flask_mysqldb import MySQL
from unittest.mock import create_autospec
import json
import requests

#from flask_sqlalchemy import SQLAlchemy
#import testing.mysqld
from FYP.entity import User
from FYP import app

class test_Patient1(unittest.TestCase):
    def setUp(self):
       self.app = Flask(__name__)
       app.config['SECRET_KEY'] = 'facial_recognition'
       app.config['MYSQL_HOST'] = 'localhost'
       app.config['MYSQL_USER'] = 'root'
       app.config['MYSQL_PASSWORD'] = ''
       app.config['MYSQL_DB'] = 'healthcare_db'
       app.config['TESTING'] = True
       app.config['LOGIN_DISABLED'] = False
       self.client = self.app.test_client()
       self.app = app.test_client()
       #
   


    def test_incorrect_username(self):
        tester = app.test_client(self)
        sent = {'username': 'wenlingg', 'password': 'password',}
        sent1 = 'Leong Wen Ling'
        result = tester.post('/LoginController', data=sent, follow_redirects=True)
        self.assertIn(b'Leong Wen Ling', result.data)
    
    def test_incorrect_password(self):
        tester = app.test_client(self)
        sent = {'username': 'wenling', 'password': 'P@$$W0RD',}
        sent1 = 'Leong Wen Ling'
        result = tester.post('/LoginController', data=sent, follow_redirects=True)
        self.assertIn(b'Leong Wen Ling', result.data)
    
    def test_no_username(self):
        tester = app.test_client(self)
        sent = {'username': '', 'password': 'password',}
        sent1 = 'Leong Wen Ling'
        result = tester.post('/LoginController', data=sent, follow_redirects=True)
        self.assertIn(b'Leong Wen Ling', result.data)

    def test_no_password(self):
        tester = app.test_client(self)
        sent = {'username': 'wenling', 'password': '',}
        sent1 = 'Leong Wen Ling'
        result = tester.post('/LoginController', data=sent, follow_redirects=True)
        self.assertIn(b'Leong Wen Ling', result.data)

    def test_pass_correct(self):
        tester = app.test_client(self)
        sent = {'username': 'wenling', 'password': 'password',}
        sent1 = 'Leong Wen Ling'
        result = tester.post('/LoginController', data=sent, follow_redirects=True)

        self.assertIn(b'Leong Wen Ling', result.data)



    
    


if __name__ == '__main__':
    unittest.main()



