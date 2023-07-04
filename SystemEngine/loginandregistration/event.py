#                                                               Utkarsh Jha

import pymongo
import time
import random
import string
# conneting to mongoDB 
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mongo = myclient["BEMSystem"]
collection = mongo["users"]


# for event we will take all data as input and store it in dictonary

def event_details():
    event_data = {
        "host_name": host_name,
        "guest_name"
    }
event_name =
event_venue =
event_date =
event_type =
event_attendies =
event_organizers =
event_host_contact =


host_name = input("Enter the name of the Host")