import unittest
from unittest import TestCase
import FYP.controller.LoginController
from unittest.mock import patch
from flask import Flask,render_template, request, redirect, url_for, Response, session
from flask_mysqldb import MySQL

app = Flask(__name__)

class test_patient(unittest.TestCase):
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

    
    def test_login(self):
       with app.test_client() as client:
           #client.post('/Patient_Main', data=dict(username='s', password='s'))
           client.get('/Patient_Main', data=dict(username='s', password='s'))
           with client.session_transaction() as sess:
               self.assertTrue(sess['logged_in'] == True)

    def test_login(self):
       with app.test_client() as client:
           client.post('/LoginController', data=dict(username='wenling', password='password'))
           with client.session_transaction() as session:
               assert session['logged_in']
               #self.assertTrue(sess['logged_in'])
    def login(self, username, password):
        test = self.app.post('/LoginController', data={'username': username, 'password': password}, follow_redirects=True)
        self.assertTrue(test)

    def test_admin_login_with_default_password(self):
        s = rq.Session()
        url = 'http://localhost/'
        data = {'username': 'admin', 'password': ''}
        r = s.post(url, data=json.dumps(data), headers=self.headers)
        self.assertEqual(r.status_code, 200)

    def test_index(self):
        with patch("LoginController.session", dict()) as session:
            client = app.test_client()
            response = client.post("/LoginController", data={
                "username": "wenlng"
            })
            self.assertTrue(session.get("username") == "wenling")
    #def test_index(self):
    #    with patch("validateLogin.session", dict()) as session:
    #        client = app.test_client(self)
    #        response = client.post("/", data={
    #            "username": "wenling", "password": "password"
    #        })
        #       self.assertTrue(session.get("username") == "test")
        #       self.assertTrue(response.data == b"userL")

    def test_dummy(self):
        self.assertEqual(2+2,4)

    def test_users_login(self):
        result = self.app.post('/LoginController', data=dict(username='wenling', password='password'), follow_redirects=True)
        #result = self.app.post('/LoginController', data=dict(username='oswaldo', password='password'))
        # I want to check the HTML tag's text value data after logging in
        #self.assertIn(result.data.getTag("h1", b"Nicole") #What I imagined using <h1>
        #self.assertin(result.data.getId("userA", b"Nicole") #What I imagined using id

        #This returns true which is okay, because 'Nicole' exists in the whole page
        #self.assertTrue(result, b'wenling')
        #self.assertTrue(result)
        self.assertEqual(result.data, 'wenling')
        #self.assertIn(b'wenling', result.data)
        #self.assertIn(b'wenling', result.data) 


    def test_pass_correct(self):
        tester = app.test_client(self)
        response = tester.post('/LoginController', data=dict(username = 'wenling', password='password'))
        self.assertFalse(b'wenling, password' in response.data)
        #self.assertTrue(b'Field must be at least 8 characters long.' in response.data)
        #self.assertTrue(response)

    # Ensure that the password-tester behaves correctly given incorrect credentials
    def test_pass_incorrect(self):
        tester = app.test_client(self)
        response = tester.post('/LoginController', data=dict(username = 'wenling', password='password'))
        self.assertTrue(b'wenling' in response.data)
        #self.assertEqual(b'password' in response.data)

   

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

