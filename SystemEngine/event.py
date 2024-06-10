''' v.1
import pymongo
import time
from datetime import datetime
import random
import string
from osessenstials import clear_terminal
import dbconnect


# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["BEMSystem"]
collection = db["events"]  # Use a more appropriate collection name

def generate_unique_event_id():
    while True:
        # Generate a unique event ID with a maximum length of 5 characters
        random_part = ''.join(random.choices(string.ascii_uppercase, k=2))  # Last two characters are compulsory alphabetic
        numeric_part = ''.join(random.choices(string.digits, k=3))  # First three characters are numeric
        event_id = numeric_part + random_part

        # Check if the generated event ID already exists in the database
        existing_event = collection.find_one({"event_ID": event_id})
        if existing_event is None:
            return event_id  # Return the unique event ID if not found



def display_seating_arrangement(seating_arrangement):
    print("\nSeating Arrangement:")
    for ticket_class, rows in seating_arrangement.items():
        print(f"\n{ticket_class} Class:")
        for i, row in enumerate(rows, start=1):
            print(f"Row {string.ascii_uppercase[i - 1]}: ", " ".join(row))


def enter_seating_arrangement(ticket_data):
    seating_arrangement = {}

    for ticket_class, class_data in ticket_data.items():
        total_seats = class_data["total_seats"]

        # Prompt user to enter the number of rows based on total seats
        while True:
            try:
                num_rows = int(input(f"Enter the number of rows for {ticket_class} class (Total Seats: {total_seats}): "))
                if num_rows <= 0:
                    raise ValueError("Number of rows must be a positive integer.")
                
                # Calculate number of seats per row (rounded up to ensure all seats are accounted for)
                seats_per_row = (total_seats + num_rows - 1) // num_rows  # Ceiling division

                # Generate seating arrangement with calculated rows and seats per row
                rows_data = []
                remaining_seats = total_seats

                for row in range(num_rows):
                    row_label = string.ascii_uppercase[row]  # A, B, C, ...
                    if remaining_seats > 0:
                        num_seats_in_row = min(seats_per_row, remaining_seats)
                        row_seats = [f"{row_label}{col + 1}" for col in range(num_seats_in_row)]
                        rows_data.append(row_seats)
                        remaining_seats -= num_seats_in_row

                # Store seating arrangement for this ticket class
                seating_arrangement[ticket_class] = rows_data
                break  # Exit loop if input and generation is successful

            except ValueError as e:
                print(f"Invalid input: {e}. Please try again.")

    return seating_arrangement





def new_event():
    clear_terminal()
    print("Event registration starting...")
    print("Enter all the details carefully\n")
    time.sleep(1)
     
    # Event registration
    event_ID = generate_unique_event_id()  # Generate unique event ID
    event_Name = input("Enter event name: ")
    event_Venue = input("Enter event venue: ")
    date_string = input("Enter a date (YYYY-MM-DD): ")
    event_Date = datetime.strptime(date_string, "%Y-%m-%d")
    event_Type = input("Enter event type: ")
    event_Attendees = int(input("Enter the number of expected attendees: "))
    event_Organizers = int(input("Enter the number of event organizers: "))
    event_Host_Contact = input("Enter event host contact number: ")
    host_name = input("Enter the name of the host: ")
    
    # Ticketing process 
    security_verification = input("Does this event require attendee's security verification? (Y/N): ")
    
    ticket_data = {}
    
    ticket_type = input("Does your ticketing scheme follow any scheme? (Y/N): ")

    if ticket_type.upper() == 'Y':
        num = int(input("Enter the number of ticket schemes you are offering: "))
        for i in range(num):
            ticket_class = input("Enter the ticket class (Premium, Gold, Platinum, etc.): ")
            total_seats = int(input(f"Enter the total number of seats for {ticket_class} class: "))
            ticket_price = float(input(f"Enter the price per seat for {ticket_class} class: "))
            ticket_data[ticket_class] = {
                "total_seats": total_seats,
                "ticket_price": ticket_price
            }
    
    # Enter seating arrangement details
    seating_arrangement = enter_seating_arrangement(ticket_data)
    
    # Store event data in MongoDB
    event_data = {
        "event_ID": event_ID,
        "host_name": host_name,
        "event_Name": event_Name,
        "event_Venue": event_Venue,
        "event_Date": event_Date,
        "event_Type": event_Type,
        "event_Attendees": event_Attendees,
        "event_Organizers": event_Organizers,
        "event_Host_Contact": event_Host_Contact,
        "security_verification": security_verification,
        "tickets_Schemas": list(ticket_data.keys()),  # List of ticket classes
        "seating_arrangement": seating_arrangement  # Include seating arrangement in event data
    }

    collection.insert_one(event_data)
    time.sleep(1)
    print("\nEvent registration complete!")
    print(f"{event_Name} has been scheduled for {event_Date}")
    print(f"Unique Event ID: {event_ID}")  # Display generated event ID
    display_seating_arrangement(seating_arrangement)  # Display seating arrangement

    # Close the MongoDB client connection
    client.close()


'''
'''

#alternate v.2



import pymongo
import time
from datetime import datetime
import random
import string
from osessenstials import clear_terminal  
import dbconnect  

def generate_unique_event_id():
    while True:
        random_part = ''.join(random.choices(string.ascii_uppercase, k=2))
        numeric_part = ''.join(random.choices(string.digits, k=3))
        event_id = numeric_part + random_part
        existing_event = dbconnect.dbconnect_event().find_one({"event_ID": event_id})
        if existing_event is None:
            return event_id

def display_seating_arrangement(seating_arrangement):
    print("\nSeating Arrangement:")
    for ticket_class, rows in seating_arrangement.items():
        print(f"\n{ticket_class} Class:")
        for i, row in enumerate(rows, start=1):
            print(f"Row {string.ascii_uppercase[i - 1]}: ", " ".join(row))

def enter_seating_arrangement(ticket_data):
    seating_arrangement = {}
    for ticket_class, class_data in ticket_data.items():
        total_seats = class_data["total_seats"]
        while True:
            try:
                num_rows = int(input(f"Enter the number of rows for {ticket_class} class (Total Seats: {total_seats}): "))
                if num_rows <= 0:
                    raise ValueError("Number of rows must be a positive integer.")
                seats_per_row = (total_seats + num_rows - 1) // num_rows
                rows_data = []
                remaining_seats = total_seats
                for row in range(num_rows):
                    row_label = string.ascii_uppercase[row]
                    if remaining_seats > 0:
                        num_seats_in_row = min(seats_per_row, remaining_seats)
                        row_seats = [f"{row_label}{col + 1}" for col in range(num_seats_in_row)]
                        rows_data.append(row_seats)
                        remaining_seats -= num_seats_in_row
                seating_arrangement[ticket_class] = rows_data
                break
            except ValueError as e:
                print(f"Invalid input: {e}. Please try again.")
    return seating_arrangement

def new_event():
    
    clear_terminal()
    print("Event registration starting...")
    print("Enter all the details carefully\n")
    time.sleep(1)
    event_ID = generate_unique_event_id()
    event_Name = input("Enter event name: ")
    event_Venue = input("Enter event venue: ")
    date_string = input("Enter a date (YYYY-MM-DD): ")
    event_Date = datetime.strptime(date_string, "%Y-%m-%d")
    event_Type = input("Enter event type: ")
    event_Attendees = int(input("Enter the number of expected attendees: "))
    event_Organizers = int(input("Enter the number of event organizers: "))
    event_Host_Contact = input("Enter event host contact number: ")
    host_name = input("Enter the name of the host: ")
    security_verification = input("Does this event require attendee's security verification? (Y/N): ")
    ticket_data = {}
    ticket_type = input("Does your ticketing scheme follow any scheme? (Y/N): ")
    if ticket_type.upper() == 'Y':
        num = int(input("Enter the number of ticket schemes you are offering: "))
        for i in range(num):
            ticket_class = input("Enter the ticket class (Premium, Gold, Platinum, etc.): ")
            total_seats = int(input(f"Enter the total number of seats for {ticket_class} class: "))
            ticket_price = float(input(f"Enter the price per seat for {ticket_class} class: "))
            ticket_data[ticket_class] = {
                "total_seats": total_seats,
                "ticket_price": ticket_price
            }
    elif ticket_type.upper() == 'N':
            ticket_class = "Primary"
            total_seats = int(input(f"Enter the total number of seats for {ticket_class} class: "))
            ticket_price = float(input(f"Enter the price per seat for {ticket_class} class: "))
            ticket_data[ticket_class] = {
                "total_seats": total_seats,
                "ticket_price": ticket_price
            }        
    seating_arrangement = enter_seating_arrangement(ticket_data)
    event_data = {
        "event_ID": event_ID,
        "host_name": host_name,
        "event_Name": event_Name,
        "event_Venue": event_Venue,
        "event_Date": event_Date,
        "event_Type": event_Type,
        "event_Attendees": event_Attendees,
        "event_Organizers": event_Organizers,
        "event_Host_Contact": event_Host_Contact,
        "security_verification": security_verification,
        "tickets_Schemas": list(ticket_data.keys()),
        "seating_arrangement": seating_arrangement
    }
    dbconnect.dbconnect_event().insert_one(event_data)
    time.sleep(1)
    print("\nEvent registration complete!")
    print(f"{event_Name} has been scheduled for {event_Date}")
    print(f"Unique Event ID: {event_ID}")
    display_seating_arrangement(seating_arrangement)

if __name__ == "__main__":
    new_event()

    '''

#V.3

import pymongo
import time
from datetime import datetime
import random
import string
from osessenstials import clear_terminal  
import dbconnect  
from tabulate import tabulate
# from dashboards import admin_dashboard

def generate_unique_event_id():
    """Generate a unique event ID by combining random letters and digits."""
    while True:
        random_part = ''.join(random.choices(string.ascii_uppercase, k=2))
        numeric_part = ''.join(random.choices(string.digits, k=3))
        event_id = numeric_part + random_part
        existing_event = dbconnect.dbconnect_event().find_one({"event_ID": event_id})
        if existing_event is None:
            return event_id
'''
def display_seating_arrangement(seating_arrangement):
    """Display the seating arrangement for the event."""
    print("\nSeating Arrangement:")
    for ticket_class, rows in seating_arrangement.items():
        print(f"\n{ticket_class} Class:")
        for i, row in enumerate(rows, start=1):
            print(f"Row {generate_row_label(i - 1)}: ", " ".join(row["seatno"]))
'''


def display_seating_arrangement(seating_arrangement):
    """Display the seating arrangement for the event."""
    print("\nSeating Arrangement:")
    # print(seating_arrangement)  # Print the entire seating arrangement
    for ticket_class, rows in seating_arrangement.items():
        print(f"\n{ticket_class} Class:")
        for i, row in enumerate(rows, start=1):
            row_label = generate_row_label(i - 1)
            seat_numbers = [seat['seatno'] for seat in row]
            print(f"Row {row_label}: ", " ".join(seat_numbers))


# def display_seating_arrangement(seating_arrangement):
#     """Display the seating arrangement for the event."""
#     print("\nSeating Arrangement:")
#     for ticket_class, rows in seating_arrangement.items():
#         print(f"\n{ticket_class} Class:")
#         if isinstance(rows, list):
#             seat_numbers = [seat['seatno'] for seat in rows]
#             print(" ".join(seat_numbers))
#         else:
#             print("Unexpected data type:", type(rows))

def generate_row_label(index):
    """Generate row labels for seats, supporting labels beyond 'Z'."""
    label = ""
    while index >= 0:
        label = chr(index % 26 + 65) + label
        index = index // 26 - 1
    return label


def enter_seating_arrangement(ticket_data):
    """Enter the seating arrangement details for each ticket class."""
    seating_arrangement = {}
    for ticket_class, class_data in ticket_data.items():
        total_seats = class_data["total_seats"]
        while True:
            try:
                num_rows = int(input(f"Enter the number of rows for {ticket_class} class (Total Seats: {total_seats}): "))
                if num_rows <= 0:
                    raise ValueError("Number of rows must be a positive integer.")
                seats_per_row = (total_seats + num_rows - 1) // num_rows
                rows_data = []
                remaining_seats = total_seats
                for row in range(num_rows):
                    row_label = generate_row_label(row)
                    if remaining_seats > 0:
                        num_seats_in_row = min(seats_per_row, remaining_seats)
                        #row_seats = [f"{row_label}{col + 1}" for col in range(num_seats_in_row)]
                        row_seats = [{"seatno":f"{row_label}{col + 1}",
                                      "customer_name":"",
                                      "customer_contact":"",
                                      "customer_email":"",
                                      "sale_id":"", 
                                      "emp_id": "" ,
                                      "security_data":""} for col in range(num_seats_in_row)]
                        rows_data.append(row_seats)
                        remaining_seats -= num_seats_in_row
                seating_arrangement[ticket_class] = rows_data
                break
            except ValueError as e:
                print(f"Invalid input: {e}. Please try again.")
    return seating_arrangement


def new_event(username):
    """Register a new event by gathering all necessary details and saving them in the database."""
    clear_terminal()
    print("Event registration starting...")
    print("Enter all the details carefully\n")
    time.sleep(1)
    
    event_ID = generate_unique_event_id()
    event_Name = input("Enter event name: ")
    event_Venue = input("Enter event venue: ")
    date_string = input("Enter a date (YYYY-MM-DD): ")
    event_Date = datetime.strptime(date_string, "%Y-%m-%d")
    event_Type = input("Enter event type: ")
    event_Attendees = int(input("Enter the number of expected attendees: "))
    event_Organizers = int(input("Enter the number of event organizers: "))
    event_Host_Contact = input("Enter event host contact number: ")
    host_name = input("Enter the name of the host: ")
    security_verification = input("Does this event require attendee's security verification? (Y/N): ")
    
    ticket_data = {}
    ticket_type = input("Does your ticketing scheme follow any scheme? (Y/N): ")
    if ticket_type.upper() == 'Y':
        num = int(input("Enter the number of ticket schemes you are offering: "))
        for i in range(num):
            ticket_class = input("Enter the ticket class (Premium, Gold, Platinum, etc.): ")
            total_seats = int(input(f"Enter the total number of seats for {ticket_class} class: "))
            ticket_price = float(input(f"Enter the price per seat for {ticket_class} class: "))
            ticket_data[ticket_class] = {
                "total_seats": total_seats,
                "ticket_price": ticket_price
            }
    elif ticket_type.upper() == 'N':
        ticket_class = "Primary"
        total_seats = int(input(f"Enter the total number of seats for {ticket_class} class: "))
        ticket_price = float(input(f"Enter the price per seat for {ticket_class} class: "))
        ticket_data[ticket_class] = {
            "total_seats": total_seats,
            "ticket_price": ticket_price
        }        
    
    seating_arrangement = enter_seating_arrangement(ticket_data)
    
    event_data = {
        "event_Company": username,
        "event_ID": event_ID,
        "host_name": host_name,
        "event_Name": event_Name,
        "event_Venue": event_Venue,
        "event_Date": event_Date,
        "event_Type": event_Type,
        "event_Attendees": event_Attendees,
        "event_Organizers": event_Organizers,
        "event_Host_Contact": event_Host_Contact,
        "security_verification": security_verification,
        "tickets_Schemas": ticket_data,
        "seating_arrangement": seating_arrangement
    }
    
    dbconnect.dbconnect_event().insert_one(event_data)
    time.sleep(1)
    print("\nEvent registration complete!")
    print(f"{event_Name} has been scheduled for {event_Date}")
    print(f"Unique Event ID: {event_ID}")
    display_seating_arrangement(seating_arrangement)
    time.sleep(10)
    return_admindashbaord = input("Press Enter to return to Admin Dashbaord or any other key to exit. ")
    if(return_admindashbaord == ""):
        from dashboards import admin_dashboard
        print("Redirecting to admin dashboard.")
        admin_dashboard(username)
    else: 
        exit

def delete_event(username):
    #from dashboards import admin_dashboard
    clear_terminal()
    """Delete an event from the database using its event ID and host contact number for confirmation."""
    eventID = input("Please Enter Event ID of the event you want to delete: ")
    event = dbconnect.dbconnect_event().find_one({"event_ID": eventID})
    
    if event:
        event_details = [
            ["Organizing Company's EmployeeID", event["event_Company"]],
            ["Event ID", event["event_ID"]],
            ["Event Name", event["event_Name"]],
            ["Event Venue", event["event_Venue"]],
            ["Event Date", event["event_Date"].strftime("%Y-%m-%d")],
            ["Event Type", event["event_Type"]],
            ["Expected Attendees", event["event_Attendees"]],
            ["Event Organizers", event["event_Organizers"]],
            ["Event Host Contact", event["event_Host_Contact"]],
            ["Host Name", event["host_name"]],
            ["Security Verification", event["security_verification"]],
            ["Ticket Schemes", ", ".join(event["tickets_Schemas"])],
        ]
        
        print("\nEvent Details:")
        print(tabulate(event_details, headers=["", "Value"]))
        
        event_Host_Contact = input("\nPlease enter the event host contact number to confirm deletion: ")
        if event_Host_Contact == event["event_Host_Contact"]:
            dbconnect.dbconnect_event().delete_one({"event_ID": eventID})
            print(f"\nEvent with ID {eventID} has been deleted.")
            runagain = input("Press Enter to delete another event: ")
            if (runagain == ""):
                delete_event(username)
            elif (runagain != ""):
                from dashboards import admin_dashboard
                print("Redirectin to admin dashbaord: ")
                admin_dashboard(username)

        else:
            print("\nIncorrect host contact number. Deletion aborted.")
    else:
        print(f"\nNo event found with ID {eventID}")
        runagain = input("Press Enter to delete another event: ")
        if (runagain == ""):
            delete_event(username)
        elif (runagain != ""):
            from dashboards import admin_dashboard
            print("Redirectin to admin dashbaord: ")
            admin_dashboard(username)

def view_event(username):
    clear_terminal()
    from dbconnect import dbconnect_event
    print("Please Wait while we get active events")
    
    try:
        # Retrieve the event collection from the database
        collection = dbconnect_event()
        
        # Get current date as string in yyyy-mm-dd format
        current_date = datetime.now()
        
        
        # Fetch and filter events from the collection based on the date and username
        filtered_events = [
            event for event in collection.find()
            if event.get('event_Company') == username and str(event.get('event_Date', ''))[:-1] >= current_date.strftime('%Y-%m-%d')
        ]
        
        
        if filtered_events:
            print(f"Active events for {username}:")
            print("-" * 40)
            for event in filtered_events:
                event_details = f"Event Name: {event.get('event_Name', 'N/A')}\n"
                event_details += f"Date: {event['event_Date']}\n"
                event_details += f"Location: {event.get('event_Venue', 'N/A')}\n"
                event_details += f"Type: {event.get('event_Type', 'N/A')}\n"
                event_details += f"Host Contact: {event.get('event_Host_Contact', 'N/A')}\n"             
                event_details += "-" * 40
                print(event_details)

                return_admindashbaord = input("Press Enter to return to Admin Dashbaord or any other key to exit. ")
                if(return_admindashbaord == ""):
                    from dashboards import admin_dashboard
                    print("Redirecting to admin dashboard.")
                    admin_dashboard(username)
                else :
                    exit

        else:
            print(f"No active events for your company.")
            return_admindashbaord = input("Press Enter to return to Admin Dashbaord or any other key to exit. ")
            if(return_admindashbaord == ""):
                from dashboards import admin_dashboard
                print("Redirecting to admin dashboard.")
                admin_dashboard(username)
            else :
                exit
    
    except Exception as e:
        print(f"An error occurred: {e}")
   


#if __name__ == "__main__":
    #new_event()
    #delete_event("rishabhjain2010")
    #view_event("qowinn")