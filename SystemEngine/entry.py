from osessenstials import clear_terminal
from dbconnect import dbconnect_event
import time


def verify_entry(username):
    from imagecapture import verify_img
    from dashboards import emp_dashboard
    clear_terminal()
    event_ID = input("Please enter your Event_ID: ")
    seatno = input("Please enter seat no. : ")
    ticket_Schema = input("Enter Ticket Schema: ")
    collection=dbconnect_event()
    event=collection.find_one({"event_ID":event_ID})
    if not event:
        print(f"No event found with event_ID: {event_ID}")
        time.sleep(10)
        verify_entry()
   # Get the seating arrangement for the specified schema
    seating_arrangement = event.get('seating_arrangement', {}).get(ticket_Schema)

    if not seating_arrangement:
        print(f"Schema '{ticket_Schema}' not found.")
        return

    # Iterate through the seating arrangement to find the specified seat number
    for row in seating_arrangement:
        for seat in row:
            if seat['seatno'] == seatno:
                print(f"Seat Number: {seat['seatno']}")
                print(f"Customer Name: {seat['customer_name']}")
                print(f"Customer Contact: {seat['customer_contact']}")
                time.sleep(10)
                image_db=seat['security_data']
                verify_img(image_db)                
    next=input("Press ENTER for next entry or R to return to dashboard.")
    if next == "" :
        verify_entry()
    elif next == "R" :
        emp_dashboard(username)
        




        
# verify_entry()         


    