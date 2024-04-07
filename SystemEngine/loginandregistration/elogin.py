                                                                #by RishabhJain2010
#employeloginportal

#import required modules
import sys , bcrypt 
import osessenstials
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
    osessenstials.clear_terminal()
    username = input("Please Enter Username: ")
    passkey = input("Please Enter Password: ")

    print("Please Wait while we log you in...")
    time.sleep(3)

    #Fetch and Verify DataBase
    verifyidentity = {"eusername": username}
    result = collection.find_one(verifyidentity)
    if result is None:
        print("Invalid Credentials.")
        choice=input("Press ENTER to try again or Ctrl+C to exit the program.")
        if choice ==" " :
            return  elogin()
        else:
            print(" Exiting  Program...")
            sys.exit(0)
    elif result is not None:
        stored_passkey = verifyidentity["epasskey"]
        if bcrypt.checkpw(passkey.encode(),stored_passkey ):
            print("User Authenticated!"+ "\nWelcome" + username)
            print("Please Wait while we redirect you to your dashboard...")
            time.sleep(3)
            dashboard()
            
    else: 
        print("Invalid Credentials!")
        time.sleep(3)
        print("Please Retry!")
        elogin()

#Dashboard Function











# ticket selling to be re routed