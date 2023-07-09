                                                                #by RishabhJain2010
#employeloginportal

#import required modules

import time
import pymongo
from loginandregistration import register as registration

#Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["BEMSystem"]
collection = db["users"]

#Dashboard Function
def dashboard() :
    print("Welcome to Dashboard!")
    ename = input("Please enter your Full Name: ") 
    eid = input("Please Enter your Employee ID: ")

 # Create Ticket Sale!

    #Call ticket sale function here! (throw ename & eid)
    print("Please Wait while we create your ticket sale...") 
    time.sleep(5)
    print("Ticket Sale Created!")
    





#Login Function
def elogin():
    username = input("Please Enter Username: ")
    passkey = input("Please Enter Password: ")
    print("Please Wait while we log you in...")
    time.sleep(3)

    #Fetch and Verify DataBase
    verifyidentity = {"eusername": username, "epassword": passkey }
    result = collection.find_one(verifyidentity)

    if result is not None:
        print("User Authenticated!"+ "\nWelcome" + username)
        print("Please Wait while we redirect you to your dashboard...")
        dashboard()
        time.sleep(3)

    else: 
        print("User Not Found or Invalid Credentials!")
        time.sleep(3)
        print("Please Retry!")
        elogin()

#Dashboard Function











# ticket selling to be re routed