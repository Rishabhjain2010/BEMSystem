#ticket selling page
import pymongo
import time
client = pymongo.MongoClient("mongodb://localhost:27017/")
print(client)
db = client["BEMSystem"]
collection = db["users"]

# from eventsAndBookings import accounts
# from eventsAndBookings import event


#                                                                                  ticket selling initate 


def ticket_Sale():
    event_id_verification = int(input("Enter your unique event ID :"))
    E_ID_check = collection.find_one({"event_ID":event_id_verification},{"event_ID":True, '_id': False})
    if event_id_verification in E_ID_check.values():
        print("Welcome, Ticket sale window starting")
        time.sleep(2)
    else:
        print("The given ID not found")




ticket_Sale()
    



#throw new sale to total sale


# call reccursive

