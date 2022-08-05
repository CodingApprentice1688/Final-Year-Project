"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)

#error here
from flask_mysqldb import MySQL
app.secret_key = 'facial_recognition'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'healthcare_db' #change into your own database
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = -1
 
mysql = MySQL(app)

import FYP.views
import FYP.controller.AdminRegisterPatientController
import FYP.controller.AdminChangePatientCredentialsController
import FYP.controller.PatientViewAppointmentController
import FYP.controller.PatientCancelAppointmentController
import FYP.controller.PatientQueueNumberController
import FYP.controller.PatientUpdatePersonalDetailController
import FYP.controller.LoginController
import FYP.controller.FacialLoginController
import FYP.controller.LogoutController
import FYP.controller.PatientUpdatePersonalDetailController
import FYP.controller.StaffSearchPatientController
import FYP.controller.StaffViewPatientAppointmentController
import FYP.controller.StaffCreateAppointmentController
import FYP.controller.StaffViewMedicalRecordController
import FYP.controller.StaffCreateMedicalRecordController
import FYP.controller.StaffUpdateMedicalRecordController
import FYP.controller.PatientBMIController