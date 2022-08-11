#authentication
#install first > pyrebase4 //github lib of original firebase
import pyrebase
import os

#add firebase into as a new appplication with this config and change into strings dicts
firebaseConfig = {
  'apiKey': "AIzaSyDf3ELC9jK3wtA03qEvyAo0XmvTsg_ywMk",
  'authDomain': "csit321-fc7e5.firebaseapp.com",
  'databaseURL': "https://csit321-fc7e5-default-rtdb.asia-southeast1.firebasedatabase.app",
  'projectId': "csit321-fc7e5",
  'storageBucket': "csit321-fc7e5.appspot.com",
  'messagingSenderId': "766096353726",
  'appId': "1:766096353726:web:3034e9ceb29a36e97a31ef",
  'measurementId': "G-J5DCWLPNM4",
  "serviceAccount": "FYP/FYP/FYP/ImageDB/csit321-fc7e5-firebase-adminsdk-m3r1k-df2514abc0.json"}

#init app
firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()
auth = firebase.auth()
storage = firebase.storage()



  
all_files = storage.child("train/hugotan/").list_files() # get all file
cnt = 0
for file in all_files:
    if file.name == "patient/":
        continue
    if "patient/" in file.name:
        path = "jancok"
        os.makedirs("FYP/FYP/FYP/static/" + path)
        
        file.download_to_filename(path+"/"+str(cnt)+".jpg")
        cnt = cnt + 1


for file in all_files:
    if file.name == "train/":
        path = "train"
        os.makedirs("FYP/deeplearning/" + path)
        continue
    if file.name == "test/":
        path = "test"
        os.makedirs("FYP/deeplearning/" + path)
        continue    
    if "train/" in file.name and ".jpg" in file.name:
        path = file.name



#for person in patient.each():
#    print(person.val())
#    print(person.val()['address'])