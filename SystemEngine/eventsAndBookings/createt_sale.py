#ticket selling page
import pymongo
import time
import random
client = pymongo.MongoClient("mongodb://localhost:27017/")
print(client)
db = client["BEMSystem"]
collection = db["users"]

#creating a new collection for storing the booked ticket details


confirmed_booking = db["bookigns"]


# from eventsAndBookings import accounts
# from eventsAndBookings import event


#                                                                                  ticket selling initate 


def ticket_Sale():
    event_id_verification = int(input("Enter your unique event ID :"))
    E_ID_check = collection.find_one({"event_ID":event_id_verification},{"event_ID":True, '_id': False})
    if event_id_verification in E_ID_check.values():
        print("Welcome, Ticket sale window starting")
        time.sleep(2)



        # here we are extracting the cost of each ticket 
        
        query = { "ticket_Price_Single":{"$exists": True} }
        result = collection.find_one(query)
        single_ticket_cost = result["ticket_Price_Single"]
        # print(single_ticket_cost)
        ticket_quantity = int(input("Enter the no. of tickets you want to book: "))



        # here we are collecting the data of customers for ticket booking 





        booking_details = {}
        
        keys = ['name', 'Gender', 'age', 'contact no.', 'email', 'address']
        for _ in range(ticket_quantity):
            values = []
            for key in keys:
                value = input(f"Enter {key}: ")
                values.append(value)

            #generating a unique booking ID
            
            while True:
                booking_id = random.randint(10000,99999)
                if booking_id not in booking_details:
                    break
            

            # Add the booking no as a value in the dictionary with key booking_id


            data = dict(zip(keys, values))
            data["booking_id"] = booking_id
            booking_details[data["booking_id"]] = data



        #inserting the data



        # generating total cost after suscessful insertion of data 

        total_cost = ticket_quantity * single_ticket_cost
        print("The net amount payable is ", total_cost)
        # payment received check 


        payment_verification = input("Enter Y if payment is confirmed and N if you want to cancle the process: ")
        if payment_verification.upper() == 'Y':
            for entry in booking_details.values():
                confirmed_booking.insert_one(entry)


        # now we will update the remaining seats in the data base


            ticket_query = {"ticket_Quantity": {"$exists": True}}

            result1 = collection.find_one(ticket_query)
            seats_prev = result1["ticket_Quantity"]
            remaining_seats = seats_prev - ticket_quantity

        
            print("Ticket booking confirmed ")
            prev={"ticket_Quantity": {"$exists": True}}
            nextt={"$set": {"ticket_Quantity": remaining_seats}}
            collection.update_one(prev, nextt)
            print("Total no. of remaining seats is ", remaining_seats)

            # realising booking ID's 




    else:
        print("The given ID not found")




ticket_Sale()
    



#throw new sale to total sale
client.close()

# call reccursive

