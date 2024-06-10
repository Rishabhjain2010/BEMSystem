#                                                             By Rishabhajain2010   

#This fucntion shows all tickets sold for a particular event ID entered by user in recent sale last format!

#import dbconnect from
from tabulate import tabulate
import time

def show_eventsale() :

    #FETCH EVENT ID
    event_id = int(input("Enter Event ID: "))
    print("Please wait while we fetch the details! ")
    time.sleep(5)
    
    #Fetch Event Deatils 
    sale=collection.find({"event_id":event_id})        
    
    sale_list = list(sale)
    if sale_list:
        field_names = sale_list[0].keys()
        table = tabulate(sale_list, headers=field_names, tablefmt="pretty")
        print(table)
    else:
        print("No sales found for the specified Event ID.")
        print("Please Try Again!")
        show_eventsale()

