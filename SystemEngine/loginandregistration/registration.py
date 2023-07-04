#                                                                   by RishabhJain2010

import pymongo
import time
import random
import string


#Connect to MongoDB
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mongo = myclient["BEMSystem"]
collection = mongo["users"]

#unique username function
def unique_username():
    username = input("Enter a username: ")
def username_available(username):
    query = {"username": username}
    result = collection.find_one(query)
    return result is None
def eusername_available(euser):
    query = {"empusername": euser}
    result = collection.find_one(query)
    return result is None

#employe username function 

def generate_eunique_username(lenght=6):
    letters = string.ascii_lowercase
    euser = join(random.choice.(characters) for i in range(lenght))
    if eusername_available(euser):
       return esuer
    else: 
       return generate_eunique_username()


def genrate_epass(lenght=12):
     characters = string.ascii_letters + string.digits + string.punctuation
     return ''.join(random.choice(characters) for i in range(length))



#Registration Function
def registration():
    print("Welcome! \nWe are happy to have you onboard!")
    firstname = input("Please Enter your First Name:")
    lastname = input("Please Enter your Last Name:")
    username = input("Please enter a Username: ")
    #uniqueusername 
    username_available()
    if username_available(username):
        print("Username Available!")
    else: 
        print("Username not Available! Please Try Again!")
        return unique_username()
    password = input("Please Create a Password: ")
    #password recheck & strenght check to be created later (encrption mode)
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

 #insert database (Users)    
 userdata = {
     "First Name": firstname,
     "Last Name": lastname,
     "Username" : username,
     "Password" : password,
     "CompanyN" ; companyname,
     "Email" : email,
     "Contact" : contact,
     "StreetAdd" : street_address,
     "City" : city,
     "State" : state,
     "Country" : country,
     "PostalCode" : postal_code,
     "empusername" : employeuser,
     "emppass" : employepass
 }
 collection.insert_one(userdata)
 time.sleep(1)
 print("Registration Completed! Welcome Onboard...")
 print("Your Employee Username is: " + employeuser)
 print("Your Employee Password is: " + employepass)
 print("Please Note it down for future reference!")
 
client.close()


    