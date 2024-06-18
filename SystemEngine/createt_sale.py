import random
import string
from dbconnect import dbconnect_event
import time
from osessenstials import clear_terminal
from tabulate import tabulate


# Global variable for MongoDB client
# mongo_client = None
# def get_mongo_client():
# 
    # global mongo_client
    # """Get or initialize the MongoDB client."""
    # if mongo_client is None:
    # 
            # mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
        # try:
            # print("MongoDB connection established successfully.")
        # except pymongo.errors.ConnectionFailure as e:
            # print(f"Failed to connect to MongoDB: {e}")
            # raise  # Rethrow the exception for handling elsewhere

    # return mongo_client
# def get_collection(database_name, collection_name):
    # """Get a MongoDB collection by database name and collection name."""
    # client = get_mongo_client()
    # db = client[database_name]
    # collection = db[collection_name]
    # return collection

# def dbconnect_event():
#     """Get the 'event' collection from the 'image_database' database."""
#     return get_collection('image_database', 'event')

def display_events():
    # from dbconnect import dbconnect_event
    db = dbconnect_event()
    events = db.find()
    print("All events in the collection:")
    for event in events:
        print(event)

def display_seats(event_id, ticket_schema):
    # from dbconnect import dbconnect_event
    db = dbconnect_event()
    try:
        event = db.find_one({"event_ID": event_id})
    except Exception as e:
        print(f"Error finding event: {e}")
        return

    if event:
      
        if 'seating_arrangement' in event and ticket_schema in event['seating_arrangement']:
            seats = event['seating_arrangement'][ticket_schema]
            for row in seats:
                for seat in row:
                    if seat['sale_id']:
                        print("X", end=" ")
                    else:
                        print(seat['seatno'], end=" ")
                print()
        else:
            print(f"No seating arrangement found for ticket schema: {ticket_schema}")
    else:
        print("Event not found")

# def display_ticketschema(event_id): 
#     db = dbconnect_event()
#     try:
#         event = db.find_one({"event_ID":event_id})
#     except Exception as e:
#         print(f"Error findind event: {e}")
#         return
    
#     if event:

#         ticket_schema = event["ticket_Schema"]
#         for ticket_schema in ticket_schema:
#             print(ticket_schema)

def display_ticketschema(event_id): 
    db = dbconnect_event()
    try:
        event = db.find_one({"event_ID":event_id})
        # print(event)
    except Exception as e:
        print(f"Error findind event: {e}")
        return
    
    if event:

        tickets_schemas = event["tickets_Schemas"]
        for tickets_schemas in tickets_schemas:
            print(tickets_schemas)




def book_seat(event_id, ticket_schema, seatno, customer_name, customer_contact, customer_email , emp_ID , security_data):
    from imagecapture import capture_img
    db = dbconnect_event()
    sale_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    # security_data = capture_img()

    try:
        event = db.find_one({"event_ID": event_id})
    except Exception as e:
        print(f"Error finding event: {e}")
        return
    
    if not event:
        print("Event not found")
        return

  

    if 'seating_arrangement' not in event or ticket_schema not in event['seating_arrangement']:
        print(f"No seating arrangement found for ticket schema: {ticket_schema}")
        return

    seat_found = False
    for row_index, row in enumerate(event['seating_arrangement'][ticket_schema]):
        for seat_index, seat in enumerate(row):
            if seat['seatno'] == seatno:
                # Update the seat information
                seat['customer_name'] = customer_name
                seat['customer_contact'] = customer_contact
                seat['customer_email'] = customer_email
                seat['sale_id'] = sale_id
                seat['emp_id'] = emp_ID
                seat['security_data'] = security_data
                seat_found = True
                break
        if seat_found:
            break

    if seat_found:
        update_path = f"seating_arrangement.{ticket_schema}.{row_index}.{seat_index}"
        result = db.update_one(
            {"event_ID": event_id},
            {"$set": {update_path: seat}}
        )
        if result.modified_count > 0:
            clear_terminal()
            print("Seat booked successfully")
            print("Please keep invoice id for future reference." + sale_id )
            time.sleep(5)
        else:
            print("Seat booking failed")
    else:
        print("Seat not found")
        print("Please Enter a valid Seat Number.")
        new_sale(emp_ID)

# Example usage:
# event_id = "941FD"
# ticket_schema = "g"

# Display all events to verify their structure
# display_events()

# Display available seats
# display_seats(event_id, ticket_schema)

# Book a seat
# book_seat(event_id, ticket_schema, "A1", "John Doe", "1234567890", "john.doe@example.com")

def new_sale(emp_id):
    from osessenstials import clear_terminal
    from imagecapture import capture_img
    clear_terminal()
    # Create a new sale
    event_ID = input("Please Enter Event_ID to create new sale: ")
    display_ticketschema(event_ID)

    ticket_schema= input("Please enter ticket scehma: ")
    print("Seats Available: ")
    display_seats(event_ID,ticket_schema)
    print("Please Enter Details: ")
    seatno = input("Seat Number: ")
    customer_name = input("Customer Name: ")
    customer_contact = input("Customer Contact: ")
    customer_email = input("Customer Email: ")
    collection = dbconnect_event()
    event = collection.find_one({"event_ID": event_ID})

    securityverification = event["security_verification"]

    if(securityverification.upper() == "Y"):
        ready = input("Event requires secuirty verification. \n  Press ENTER to click picture when ready or X to Cancel booking.")
        if(ready == ""):
            security_data = capture_img()
        else:
            print("Booking Cancelled")
            time.sleep(5)
            new_sale(emp_id)

    else:
        security_data = "None" 

    security_data = capture_img()
    book_seat(event_ID, ticket_schema , seatno , customer_name , customer_contact , customer_email , emp_id  , security_data)



def view_sales(username):
    from dashboards import admin_dashboard
    clear_terminal()
    event_id = input("Please enter Event ID to view sales: ")

    # Assuming dbconnect_event is a function that returns a MongoDB collection
    from dbconnect import dbconnect_event

    # Get the collection
    collection = dbconnect_event()

    # Find the event by event_ID
    event = collection.find_one({"event_ID": event_id})
    if not event:
        print(f"No event found with event_ID: {event_id}")
        time.sleep(10)
        view_sales()

    # Initialize total sales and details list
    total_sales = 0
    sales_details = []

    # Iterate over seating arrangements
    for schema, seats in event.get("seating_arrangement", {}).items():
        ticket_price = event.get("tickets_Schemas", {}).get(schema, {}).get("ticket_price", 0)
        
        for row in seats:
            for seat in row:
                if seat.get("sale_id"):
                    sales_details.append({
                        "Seat No": seat["seatno"],
                        "Customer Name": seat["customer_name"],
                        "Customer Contact": seat["customer_contact"],
                        "Customer Email": seat["customer_email"],
                        "Sale ID": seat["sale_id"],
                        "Employee ID": seat["emp_id"],
                        "Ticket Price": ticket_price
                    })
                    total_sales += ticket_price

    # Display the sales details in a table format
    if sales_details:
        print(tabulate(sales_details, headers="keys", tablefmt="grid"))
    else:
        print("No sales found for the event.")

    print(f"Total Sales: {total_sales}")
    # return sales_details, total_sales

    findnext = input("Press ENTER to search another event or any other key to return to Admin Dashboard: ")
    if findnext == "":
        view_sales(username)
    elif findnext != "":
        admin_dashboard(username)

        





# Example usage
# view_sales("systemadmin")
# new_sale("avstau")
