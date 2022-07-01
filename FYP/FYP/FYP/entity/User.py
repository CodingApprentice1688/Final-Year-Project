from datetime import datetime, date
from flask import render_template
from FYP import app
from FYP import mysql

from flask import Flask,render_template, request, redirect, url_for, Response, session
from flask_mysqldb import MySQL
import MySQLdb.cursors 




class User:
    def registerPatient(name, nric, age, gender, username, password, role):
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    
        ten = 0

       # ('SELECT * FROM user where name LIKE %%s% AND role = % s', (name, pat, ))
        cursor.execute ("INSERT INTO user (name, nric, age, gender, username, password, role) VALUES (% s, % s, % s, % s, % s, % s, % s)", (name, nric, age, gender, username, password, role, ))
        mysql.connection.commit()

        
        