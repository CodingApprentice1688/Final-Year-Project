import unittest
from unittest import TestCase
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
       self.client = self.app.test_client()
       self.app = app.test_client()
    def validateLogin():
        error = None
        msg = 'Logged in successfully !'   
        error = 'Invalid Credentials. Please try again.'
        username = request.form['username']
        password = request.form['password']
        result, userL = User.validateLogin(username, password)

        if result:
            if userL['role'] == 'healthcare staff':
                return redirect("/HealthcareStaff_Main")
            if userL['role'] == 'patient':
                return redirect("/Patient_Main")
            if userL['role'] == 'IT admin':
                return redirect("/Admin_Main")   

        else:
            return render_template('login.html', error = error)
    def test_login(self):
       with app.test_client() as client:
           #client.post('/Patient_Main', data=dict(username='s', password='s'))
           client.get('/Patient_Main', data=dict(username='s', password='s'))
           with client.session_transaction() as sess:
               self.assertTrue(sess['logged_in'] == True)

    def login(self, username, password):
        return self.app.post('/login', data={'username': username, 'password': password}, follow_redirects=True)
    
    def test_listing_all_users(self):
        self.assertTrue(self.login(username, password).status_code == 200)

    def test_index(self):
        with patch("validateLogin.session", dict()) as session:
            client = app.test_client(self)
            response = client.post("/", data={
                "username": "wenling", "password": "password"
            })
            assert session.get("username") == "test"
            assert response.data == b"userL"


    def test_pass_correct(self):
        tester = app.test_client(self)
        response = tester.post('/Patient_Main', data=dict(username = 'wenling', password='password'))
        self.assertFalse(b'wenling, password' in response.data)
        #self.assertTrue(b'Field must be at least 8 characters long.' in response.data)
        #self.assertTrue(response)

    # Ensure that the password-tester behaves correctly given incorrect credentials
    def test_pass_incorrect(self):
        tester = app.test_client(self)
        response = tester.post('/Patient_Main', data=dict(username = 'wenling', password='password'))
        self.assertTrue(b'wenling, password' in response.data)
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

