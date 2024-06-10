#                                                                   by RishabhJain2010
#V.1

"""

import osessenstials
import pymongo  
import time
import random
import string
import bcrypt
import dashboards 

#Connect to MongoDB
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mongo = myclient["BEMSystem"]
collection = mongo["users"]

#unique username function
def unique_username():
    while True: 

        username = input("Enter a username: ")
        username_available (username)
def username_available(username):
    query = {"Username": username}
    result = collection.find_one(query)
    return result is None
def eusername_available(euser):
    query = {"empusername": euser}
    result = collection.find_one(query)
    return result is None

#employe username function 

def generate_eunique_username(length=6):
    letters = string.ascii_lowercase
    euser = ''.join(random.choice(letters) for i in range(length))
    if eusername_available(euser):
       return euser
    else: 
       return generate_eunique_username()


def genrate_epass(length=12):
     characters = string.ascii_letters + string.digits + string.punctuation
     return ''.join(random.choice(characters) for i in range(length))



#Registration Function
def registration():
    osessenstials.clear_terminal() 
    print("Welcome! \nWe are happy to have you onboard!")
    firstname = input("Please Enter your First Name:")
    lastname = input("Please Enter your Last Name:")
    username = input("Please enter a Username: ")
    #uniqueusername 
    username_available(username)
    if username_available(username):
        print("Username Available!")
    else: 
        print("Username not Available! Please Try Again!")
        return unique_username()
    password = input("Please Create a Password: ")
    password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())      #Encryption of Admin's Password

    companyname = input("Please enter your Company Name: ")
    email = input("Please enter your EMail: ")
    contact = input("Please enter your contact: ")
    #Address Input
    street_address = input("Enter the street address: ")
    city = input("Enter the city: ")
    state = input("Enter the state: ")
    country = input("Enter the country: ")
    postal_code = input("Enter the postal code: ")
    
    employeuser = generate_eunique_username()
    employepass = genrate_epass()
    time.sleep(1)
    osessenstials.clear_terminal()
    
    
    enc_employepass =bcrypt.hashpw(employepass.encode(), bcrypt.gensalt())     #Encryption of Employee's Password

 #insert database (Users)    
    userdata = {
        "First Name": firstname,
        "Last Name": lastname,
        "Username" : username,
        "Password" : password,
        "CompanyN" : companyname,
        "Email" : email,
        "Contact" : contact,
        "StreetAdd" : street_address,
        "City" : city,
        "State" : state,
        "Country" : country,
        "PostalCode" : postal_code,
        "empusername" : employeuser,
        "emppass" : enc_employepass 
        }
    collection.insert_one(userdata)

    print("Registration Completed! Welcome Onboard...")
    print("Your Employee Username is: " + employeuser)
    print("Your Employee Password is: " + employepass)
    print("Please Note it down for future reference!")
    

    #Dashboard Redirect
    dashboards.admin_dashboard()

    

"""
      #V.2    



# Required modules
import osessenstials
import pymongo
import time
import random
import string
import bcrypt

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["BEMSystem"]
collection = db["users"]

# Function to check if username is available
def is_username_available(username):
    query = {"Username": username}
    result = collection.find_one(query)
    return result is None

# Function to generate a unique employee username
def generate_unique_employee_username(length=6):
    letters = string.ascii_lowercase
    while True:
        euser = ''.join(random.choice(letters) for _ in range(length))
        if is_username_available(euser):
            return euser

# Function to generate a random password
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

# Registration Function
def registration():

    from dashboards import admin_dashboard
    osessenstials.clear_terminal()
    print("Welcome! \nWe are happy to have you onboard!")

    # Prompt for user details
    firstname = input("Please Enter your First Name: ")
    lastname = input("Please Enter your Last Name: ")
    
    # Check for a unique username
    while True:
        username = input("Please enter a Username: ")
        if is_username_available(username):
            print("Username Available!")
            break
        else:
            print("Username not Available! Please Try Again!")

    password = input("Please Create a Password: ")
    password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    companyname = input("Please enter your Company Name: ")
    email = input("Please enter your Email: ")
    contact = input("Please enter your contact: ")
    
    # Address Input
    street_address = input("Enter the street address: ")
    city = input("Enter the city: ")
    state = input("Enter the state: ")
    country = input("Enter the country: ")
    postal_code = input("Enter the postal code: ")

    employeuser = generate_unique_employee_username()
    employepass = generate_password()

    # Encryption of Employee's Password
    enc_employepass = bcrypt.hashpw(employepass.encode(), bcrypt.gensalt())

    # Insert data into the database
    userdata = {
        "First Name": firstname,
        "Last Name": lastname,
        "Username": username,
        "Password": password,
        "CompanyN": companyname,
        "Email": email,
        "Contact": contact,
        "StreetAdd": street_address,
        "City": city,
        "State": state,
        "Country": country,
        "PostalCode": postal_code,
        "empusername": employeuser,
        "emppass": enc_employepass
    }
    collection.insert_one(userdata)

    # Display registration confirmation
    print("Registration Completed! Welcome Onboard...")
    print("Your Employee Username is:", employeuser)
    print("Your Employee Password is:", employepass)
    print("Please Note it down for future reference!")

    # Dashboard Redirect
    #admin_dashboard()

# Execute the registration function
#registration()


    