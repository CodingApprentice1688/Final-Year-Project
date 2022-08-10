#authentication
#install first > pyrebase4 //github lib of original firebase
import pyrebase

#add firebase into as a new appplication with this config and change into strings dicts
firebaseConfig = {
  'apiKey': "AIzaSyDf3ELC9jK3wtA03qEvyAo0XmvTsg_ywMk",
  'authDomain': "csit321-fc7e5.firebaseapp.com",
  'databaseURL': "https://csit321-fc7e5-default-rtdb.asia-southeast1.firebasedatabase.app",
  'projectId': "csit321-fc7e5",
  'storageBucket': "csit321-fc7e5.appspot.com",
  'messagingSenderId': "766096353726",
  'appId': "1:766096353726:web:3034e9ceb29a36e97a31ef",
  'measurementId': "G-J5DCWLPNM4" }

#init app
firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()
auth = firebase.auth()
storage = firebase.storage()


storage.child("Oswal.jpg").download("", "hola.jpg")



#for person in patient.each():
#    print(person.val())
#    print(person.val()['address'])