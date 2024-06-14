from osessenstials import clear_terminal
from dbconnect import dbconnect_event


def verify_entry():
    clear_terminal()
    event_ID = input("Please enter your Event_ID: ")
    seatno = input("Please enter seat no. : ")
    collection=dbconnect_event
    # data=collection.findone{}


    