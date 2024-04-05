                                                                    #by RishabhJain2010
#import required modules

import sys
import time
import pymongo
from loginandregistration import register as registration

#Connect to MongoDB
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mongo = myclient["BEMSystem"]
collection = mongo["users"]



#Login Function
def login():
    maxattempts = 3
    attempts = 0

    while maxattempts > attempts:
        username = input("Please Enter Username: ")
        passkey = input("Please Enter Password: ")
        print("Please Wait while we log you in...")
        time.sleep(3)

        #Fetch and Verify DataBase
        verifyidentity = {"username": username, "password": passkey }
        result = collection.find_one(verifyidentity)

        if result is not None:
            print("User Authenticated!"+ "\nWelcome" + username)
            print("Please Wait while we redirect you to your dashboard...")
            time.sleep(3)
            return 

        else: 
            print("Invalid username or password. Please try again.")
            attempts += 1
            choice = input("Do you want to create a new account? (Y/N): ").upper()
            if choice == "Y":
                registration()
            time.sleep(3) 

    print("Maximum number of login attempts reached. Please try again later. \n If you need assistance please contact the system administrator. \n Exiting...")
    sys.exit(1)
    

        

