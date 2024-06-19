#                                                                 #by RishabhJain2010
# #employeloginportal

# #import required modules
# import sys , bcrypt 
# import osessenstials
# import time
# import pymongo
# import register as registration
# from dashboards import emp_dashboard

# #Connect to MongoDB
# client = pymongo.MongoClient("mongodb://localhost:27017/")
# db = client["BEMSystem"]
# collection = db["users"]

# #Login Function
# def elogin():
#     osessenstials.clear_terminal()
#     username = input("Please Enter Username: ")
#     passkey = input("Please Enter Password: ")

#     print("Please Wait while we log you in...")
#     time.sleep(3)

#     #Fetch and Verify DataBase
#     verifyidentity = {"empusername": username}
#     result = collection.find_one(verifyidentity)
#     if result is None:
#         print("Invalid Credentials.")
#         choice=input("Press ENTER to try again or Ctrl+C to exit the program.")
#         if choice =="" :
#             return  elogin()
#         else:
#             print(" Exiting  Program...")
#             sys.exit(0)

#     elif result is not None:
#         stored_passkey = verifyidentity["emppass"]


#         if bcrypt.checkpw(passkey.encode(),stored_passkey ):
#             print("User Authenticated!"+ "\nWelcome" + username)
#             print("Please Wait while we redirect you to your dashboard...")
#             time.sleep(3)
#             emp_dashboard(username)
            
#     else: 
#         print("Invalid Credentials!")
#         time.sleep(3)
#         print("Please Retry!")
#         elogin()

# #Completed


                                                                    #by RishabhJain2010
#import required modules

import sys 
import osessenstials
import time
import pymongo
import register as registration
import bcrypt   
import dashboards

#Connect to MongoDB
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mongo = myclient["BEMSystem"]
collection = mongo["users"]


#Function to verify encrypted passkey
def verifypassword(username , passkey) :
    user_data = collection.find_one({"empusername": username}) 
    if user_data is None :
        print("User not found in the database.")
        time.sleep(5) 
        return elogin()
    else : 
        stored_password = user_data["emppass"]
        if bcrypt.checkpw(passkey.encode() , stored_password) :
            return True
        else : 
            return False


#Login Function
def elogin():
    from register import registration
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
        
            print("User Authenticated!"+ "\nWelcome " + username)
            print("Please Wait while we redirect you to your dashboard...")
            time.sleep(3)
                      
                       #Redirecting user to DashBoard page
            return dashboards.emp_dashboard(username)

        else: 
            print("Invalid password. Please try again.")
            ++attempts 
            choice = input("Do you want to create a new account? (Y/N): ").upper()
            if choice.upper() == "Y":
                registration()
                time.sleep(3) 
            elif choice.upper != "Y" : 
                continue

    print("Maximum number of login attempts reached. Please try again later. \n If you need assistance please contact the system administrator. \n Exiting...")
    sys.exit(1)
    

        













# # ticket selling to be re routed