                                                                    #by RishabhJain2010
#import required modules

import sys 
from .. import osessenstials
import time
import pymongo
from loginandregistration import register as registration
import bcrypt   

#Connect to MongoDB
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mongo = myclient["BEMSystem"]
collection = mongo["users"]


#Function to verify encrypted passkey
def verifypassword(username , passkey) :
    user_data = collection.find_one({"Username": username}) 
    if user_data is None :
        print("User not found in the database.")  
        return login()
    else : 
        stored_password = user_data["Password"]
        if bcrypt.checkpw(passkey.encode() , stored_password) :
            return True
        else : 
            return False


#Login Function
def login():
    osessenstials.clear_terminal()
    maxattempts = 3
    attempts = 0

    while maxattempts > attempts:
        username = input("Please Enter Username: ")
        passkey = input("Please Enter Password: ")
        print("Please Wait while we log you in...")
        time.sleep(3)

        #Fetch and Verify DataBase
        if  verifypassword(username, passkey):
        
            print("User Authenticated!"+ "\nWelcome" + username)
            print("Please Wait while we redirect you to your dashboard...")
            time.sleep(3)
            #Redirecting user to DashBoard page
            return 

        else: 
            print("Invalid password. Please try again.")
            attempts += 1
            choice = input("Do you want to create a new account? (Y/N): ").upper()
            if choice == "Y":
                registration()
            time.sleep(3) 

    print("Maximum number of login attempts reached. Please try again later. \n If you need assistance please contact the system administrator. \n Exiting...")
    sys.exit(1)
    

        

