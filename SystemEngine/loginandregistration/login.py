                                                                    #by RishabhJain2010
#import required modules

import time
import pymongo
from loginandregistration import register as registration

#Connect to MongoDB
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mongo = myclient["BEMSystem"]
collection = mongo["users"]



#Login Function
def login():
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

    else: 
        print("User Not Found! Please Register")
        time.sleep(3)
        registration()

