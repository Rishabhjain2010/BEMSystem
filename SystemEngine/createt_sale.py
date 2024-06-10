import pymongo
from bson.objectid import ObjectId
import random
import string

# Global variable for MongoDB client
mongo_client = None

def get_mongo_client():
    """Get or initialize the MongoDB client."""
    global mongo_client
    
    if mongo_client is None:
        try:
            mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
            print("MongoDB connection established successfully.")
        except pymongo.errors.ConnectionFailure as e:
            print(f"Failed to connect to MongoDB: {e}")
            raise  # Rethrow the exception for handling elsewhere
    return mongo_client

def get_collection(database_name, collection_name):
    """Get a MongoDB collection by database name and collection name."""
    client = get_mongo_client()
    db = client[database_name]
    collection = db[collection_name]
    return collection

def dbconnect_event():
    """Get the 'event' collection from the 'image_database' database."""
    return get_collection('image_database', 'event')

def display_events():
    db = dbconnect_event()
    events = db.find()
    print("All events in the collection:")
    for event in events:
        print(event)

def display_seats(event_id, ticket_schema):
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

def book_seat(event_id, ticket_schema, seatno, customer_name, customer_contact, customer_email):
    from imagecapture import capture_img
    db = dbconnect_event()
    sale_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    emp_id = "EMP_ENT"
    security_data = capture_img()

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
                seat['emp_id'] = emp_id
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
            print("Seat booked successfully")
        else:
            print("Seat booking failed")
    else:
        print("Seat not found")

# Example usage:
event_id = "941FD"
ticket_schema = "g"

# Display all events to verify their structure
# display_events()

# Display available seats
display_seats(event_id, ticket_schema)

# Book a seat
book_seat(event_id, ticket_schema, "A1", "John Doe", "1234567890", "john.doe@example.com")
