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
   


    #def test_dummy(self):
    #    self.assertEqual(2+2,4)


        #self.assertIn(b'wenling', result.data) 


    def test_pass_correct(self):
        tester = app.test_client(self)
        sent = {'username': 'wenling', 'password': '',}
        sent1 = 'Leong Wen Ling'
        result = tester.post('/LoginController', data=sent, follow_redirects=True)
       # dataR = request.get_json()

        #print(result.data)
        ##self.assertTrue(result)
        #print(myAuthResponse.status_code)
        #self.assertEqual(result.data, decodeR)
        #self.assertEqual(result.data, json.dumps(sent))
        self.assertIn(b'Leong Wen Ling', result.data)
        #self.assertEqual(result.data, sent1)

        #check if request is successful, new page is created
        #self.assertTrue(result.status_code == 202)
    



if __name__ == '__main__':
    unittest.main()



