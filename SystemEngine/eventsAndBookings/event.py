#                                                               Utkarsh Jha

import pymongo
import time
from datetime import datetime
import random
import string

# conneting to mongoDB 
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mongo = myclient["BEMSystem"]
collection = mongo["users"]



def event_enquiry():
    print("Event enquiry will be created")


def event_details():
    print("Event registration starting")
    print("Enter all the details carefully")
    time.sleep(3)

#                                                                                      Event registration

    event_ID = int(input("Enter a unique event ID for future Refference"))
    event_Name = input("Enter event name:  ")
    event_Venue = input("Enter event venue:  ")
    date_string = input("Enter a date (YYYY-MM-DD): ")
    date = datetime.strptime(date_string, "%Y-%m-%d")
    # event_Date = input("Enter event date:  ")
    event_Type = input("Enter event type: ")
    event_Attendies = input("Enter the no. of expected attendies:  ")
    event_Organizers = input("Enter no. of event organizers:  ")
    event_Host_Contact = input("Enter event ")
    host_name = input("Enter the name of the Host: ")


#                                                                                       Ticketing process 

    securityv = input("Does this event require Attendee's security verifiction? , Enter Y if yes, enter N if no ")
    print("Ticketing: \n")
    time.sleep(1)
    ticket_type = input("Does your ticketing scheme follow any scheme, Enter Y if yes, enter N if no")

    ticket_Price_Single = 0
    ticket_Quantity = 0 
    
    if ticket_type.upper() == 'Y':
        num  = int(input("Enter the no of ticket schemes you are offering"))
        ticket_data = { }
        list_of_Prices = []
        for e in range(num):
            key = input("Enter the Booking type (Premimum, Gold, Platinum etc.)")
            value = int(input("Enter the no. of seats in ", +key ,": "))
            price = float(input("Enter the cost of each ", +key ," class ticket:"))
            ticket_data[key] = value
            list_of_Prices.append(price)


    elif ticket_type.upper() == 'N':
        ticket_Quantity = int(input("Enter the no. of tickets you want to sell: "))
        ticket_Price_Single = float(input("Enter price of single ticket: "))


    event_data = {
            "event_ID": event_ID,
            "host_name": host_name,
            "event_Name": event_Name,
            "event_Venue": event_Venue,
            "event_Date": date,
            "event_Type": event_Type,
            "event_Attendies": event_Attendies,
            "event_Organizers": event_Organizers,
            "event_Host_Contact": event_Host_Contact,
            "ticket_Quantity": ticket_Quantity,
            "ticket_Price_Single": ticket_Price_Single,
            "tickets_Schemas" : ticket_data,
            "tickets_Schemas_priceList" : list_of_Prices

    }
    collection.insert_many(event_data)
    time.sleep(1)
    print("Event registration complete")
    print(event_Name + " Has been scheduled for " + date)

event_details()
myclient.close()