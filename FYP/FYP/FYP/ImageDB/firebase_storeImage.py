#authentication
#install first > pyrebase4 //github lib of original firebase
import pyrebase

#add firebase into as a new appplication with this config and change into strings dicts
firebaseConfig = {
    'apiKey': "AIzaSyAsiZcMwGaXIuyX6hU6uTP6mCndU1uTFxQ",
  'authDomain': "fyp-facereg-q3.firebaseapp.com",
  'databaseURL': "https://fyp-facereg-q3-default-rtdb.asia-southeast1.firebasedatabase.app",
  'projectId': "fyp-facereg-q3",
  'storageBucket': "fyp-facereg-q3.appspot.com",
  'messagingSenderId': "954204326202",
  'appId': "1:954204326202:web:f08a4d8e5f1c91b044a803",
  'measurementId': "G-BR78Q6GKP8" }

#init app
firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()
auth = firebase.auth()
storage = firebase.storage()

#for auth > 
#web > auth
#eg signin with email n pw
#enable for users // must add into database first 

#letting users auto signin from python line //dummy@gmail.com n password
"""
email = input("enter your email:")
password = input("enter your password:")
try:
    auth.sign_in_with_email_and_password(email, password)
    print("sucess sign in ")
except:
    print("invalid creds, try again")
"""

"""
#sigin up part
email = input("enter your email:")
password = input("enter your password:")
confirmpass = input("confirm password")
if password == confirmpass:
    try:
        auth.create_user_with_email_and_password(email, password)
        print("success")
    except:
        print("the email already exists")

"""




# -------------for storage > create the cloud storage bucket >. 
# #===========================================they can upload the photos that devs can read 

#asking user what i want to upload 
#filename = input("enter the name of the file you want to upload ")

#asking user what i want to name the filee into the cloud, 
#cloudFileName = input("enter the name of the file in cloud ")
 
#storage.child(cloudFileName).put(filename)

#print(storage.child(cloudfilename).get_url(None))


#asking user what to download 
#filename = input("enter the name of the file you want to download ")

#asking user what i want to name the filee into the cloud, 
#cloudFileName = input("enter the name of the file in cloud you want to download")
 

#need to specify a path > book/tester
storage.child(cloudFileName).download("", "downloadtxt.txt")

cloudFileName = input("enter the name of the file in cloud you want to download")
#url = storage.child(cloudFileName).get_url(None)
#f = urllib.request.urlopen(url).read()
#print(f)


#firebase > realtime database > leaf nodes are the data
#--------------------------create data about 1 person, with data node with unique ID
data = { 'age':12, 'address': "SG", 'employed': True, 'name': "Jane sma"}
#db.push(data)

#this pushed data under a node called patient, can keep adding .child to create a new node under, 
#this for eg creates a child ID under patient node
#  db.child("patient").push(data)

#to set my own ID .child by v
#db.child("patient").child("USER_set_ID").set(data)

#update data that was uploaded by using USER_set_ID if column dont exist, 
#it will update and add a new column
#db.child("patient").child("USER_set_ID").update({'name2':"janate"})

#if i wanna access ID of that i dont know , taking all under node "patient" and get
#patient = db.child("patient").get()

#check each patient and change the name 
#for person in patient.each():
 #   if person.val()['name'] == 'Mark':
  #      db.child("patient").child(person.key()).update({'name': "Jane"})


#==========================delete data with known ID
#delete mary 
#db.child("patient").child("mary").remove()

#========================delete data with unknown ID
#patient = db.child("patient").get()

#check each patient and change the name 
#for person in patient.each():
#    if person.val()['name'] == 'John Smith':
#        db.child("patient").child(person.key()).child("age").remove()


#---------------------------------------read with specified ID add a .child
#patient = db.child("patient").get()
#index columns in firebase > go to rules 
#create the "patient" : {.indexOn:["age", "location", "name", "employed"]}

#order by and only print those with Jane
patient = db.child("patient").order_by_child("name").equal_to("Jane sma").get()

#to look for patient at age 12 and before 91 .limit_to_first/last
#patient = db.child("patient").order_by_child("age").start_at(12).end_at(91).get()

for person in patient.each():
    print(person.val())
    print(person.val()['address'])