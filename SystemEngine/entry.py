from osessenstials import clear_terminal
from dbconnect import dbconnect_event
import time


def verify_entry(username , emp_id):
    clear_terminal()
    emp_id = input("Please Enter Your Employe ID: ")
    event_ID = input("Please enter your Event_ID: ")
    seatno = input("Please enter seat no. : ")
    ticket_Schema = input("Enter Ticket Schema: ")
    collection=dbconnect_event()
    event=collection.find_one({"event_ID":event_ID})
    if not event:
        print(f"No event found with event_ID: {event_ID}")
        time.sleep(10)
        verify_entry()
        

        
            

    