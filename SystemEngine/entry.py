from osessenstials import clear_terminal
from dbconnect import dbconnect_event


def verify_entry(username , emp_id):
    clear_terminal()
    emp_id = input("Please Enter Your Employe ID: ")
    event_ID = input("Please enter your Event_ID: ")
    seatno = input("Please enter seat no. : ")
    collection=dbconnect_event
    event=collection.findone({"event_ID":event_ID})
    if event:
        if event["emp_id"]==emp_id:


    