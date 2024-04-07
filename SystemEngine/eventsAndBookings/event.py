import pymongo
import time
from datetime import datetime
import random
import string
from osessenstials import clear_terminal


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





def event_details():
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
