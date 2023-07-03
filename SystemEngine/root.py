#System Engine (Main Function)
#Welcome DashBoard


#Workflow : 
#Event & Host Details  F-1 
#Ticket Booking & Seat Configuration
#Security Checks (AI Model and Face Recognition System)
#Event Attendance (Using Face Recognition)
#Event Feedback (Auto Audio Sanmpling)
#Event Reminder Alert (Auto Emailing)
#Event Summary Report  (Total Ticket Sold , Profit Earned etc.)
#Invoice Mailing  (Auto Mailing System)
        
#importingmodules
import time
import os

#Importing
from loginandregistration import login 
from loginandregistration import registration 
#definebasicfunctions


def clear_terminal():
    # Clear the terminal screen based on the operating system
    os.system('cls' if os.name == 'nt' else 'clear')

# Call the function to clear the terminal
#clear_terminal()

#MainFunctiion

#print("Hello World!")
#Welcomeportal

#by RishabhJain2010
print("Welcome to BEMSystem \nDeveloped by Rishabh Jain & Utkarsh Jha")
print("Loading System Engine...")
time.sleep(5)
clear_terminal()
loginopt = input("Please Enter 1 to login as Existing User! \nPlease Enter 2 for New Registration")
print(loginopt)
#Login/Registration Window
if loginopt == 1:
    login.login()
#Registration Form (Upload to host.py)
elif loginopt == 2:
    registration.registration()

#Input Basic Info & Create UserName/Password


#Redirect to F-1

#Login Form (Fetch from Host.py)





#_______________________________
print("Please Wait while we log you in...")
print("Loading...")
time.sleep(5)