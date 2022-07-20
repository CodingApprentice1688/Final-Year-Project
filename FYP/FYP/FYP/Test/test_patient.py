import unittest
from unittest import TestCase
import os
#import FYP.controller.LoginController
from unittest.mock import patch
from unittest import mock
from flask import Flask,render_template, request, redirect, url_for, Response, session, jsonify
from flask_mysqldb import MySQL
from unittest.mock import create_autospec
import sqlite3
from flask_sqlalchemy import SQLAlchemy
import testing.mysqld

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@127.0.0.1/healthcare_db'
#mysql://root:''@localhost:5555/healthcare_db

#String url = "jdbc:mysql://<ip_goes_here>:port/dbname";
#db = SQLAlchemy(app)

def insert_rows(rows, table_name, dbc):
        field_names = rows[0].keys()
        field_names_str = ', '.join(field_names)
        placeholder_str = ','.join('?'*len(field_names))
        insert_sql = f'INSERT INTO {table_name}({field_names_str}) VALUES ({placeholder_str})'
        saved_autocommit = dbc.autocommit
        with dbc.cursor() as cursor:
            try:
                dbc.autocommit = False
                tuples = [ tuple((row[field_name] for field_name in field_names)) for row in rows ]
                cursor.executemany(insert_sql, tuples)
                cursor.commit()
            except Exception as exc:
                cursor.rollback()
                raise exc
            finally:
                dbc.autocommit = saved_autocommit

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
       #
   


    
    def test_login(self):
       with app.test_client() as client:
           #client.post('/Patient_Main', data=dict(username='s', password='s'))
           client.get('/Patient_Main', data=dict(username='s', password='s'))
           with client.session_transaction() as sess:
               self.assertTrue(sess['logged_in'] == True)

    def test_login_v1(self):
       with app.test_client() as client:
           client.post('/LoginController', data=dict(username='wenling', password='password'))
           with client.session_transaction() as session:
               self.assertTrue(session.get("username") == "wenling")
               #self.assertTrue(session['logged_in'])
               #self.assertTrue(sess['logged_in'])
    def test_test(self, username, password):
        test = self.app.post('/LoginController', data={'username': username, 'password': password}, follow_redirects=True)
        self.assertTrue(test)

    def test_admin_login_with_default_password(self):
        s = rq.Session()
        url = 'http://localhost/'
        data = {'username': 'admin', 'password': ''}
        r = s.post(url, data=json.dumps(data), headers=self.headers)
        self.assertEqual(r.status_code, 200)

    def test_index_login(self):
        with patch("session", dict()) as session:
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
    def test_pass_incorrect(self):
            tester = app.test_client(self)
            response = tester.post('/LoginController', data=dict(username = 'wenling', password='password'))
            self.assertTrue(b'wenling' in response.data)

    def test_database(self):
        tester = os.path.exists("healthcare_db.sql")
        self.assertTrue(tester)

    

    def fix_dbc(self):
        dbc = mock.MagicMock(spec=['cursor'])
        dbc.autocommit = True
        return dbc

    def fix_rows(self):
        rows = [{'id':1, 'name':'John'}, {'id':2, 'name':'Jane'},]
        return rows

    def test_insert_rows_calls_cursor_method(self):
        dbc = self.fix_dbc()
        rows = self.fix_rows()
        insert_rows(rows, 'users', dbc)
        self.assertTrue(dbc.cursor.called)
    
    def test_username_exist(self):
        expected = 'SELECT * from users where username="John"'
        actual = [{'id':1, 'name':'John'},]
        self.assertTrue(expected, actual)


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


