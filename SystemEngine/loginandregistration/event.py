#                                                               Utkarsh Jha

import pymongo
import time
import random
import string
# conneting to mongoDB 
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mongo = myclient["BEMSystem"]
collection = mongo["users"]



def event_enquiry():
    print("Event enquiry will be created")

# for event we will take all data as input and store it in dictonary

def event_details():
    print("Event registration starting")
    print("Enter all the details carefully")
    time.sleep(3)
    event_id = input("Enter a unique event ID for future refference")
    event_name = input("Enter event name:  ")
    event_venue = input("Enter event venue:  ")
    event_date = input("Enter event date:  ")
    event_type = input("Enter event type: ")
    event_attendies = input("Enter the no. of expected attendies:  ")
    event_organizers = input("Enter no. of event organizers:  ")
    event_host_contact = input("Enter event ")
    host_name = input("Enter the name of the Host: ")

    event_data = {
            "event_id": event_id,
            "host_name": host_name,
            "event_name": event_name,
            "event_venue": event_venue,
            "event_date": event_date,
            "event_type": event_type,
            "event_attendies": event_attendies,
            "event_organizers": event_organizers,
            "event_host_contact": event_host_contact
    }
    collection.insert_many(event_data)
    time.sleep(1)
    print("Event registration complete")
    print(event_name + " Has been scheduled for " + event_date)

event_details()

myclient.close()