#                                                           By Rishabhjain2010      

#This is a function module file used to connect with database whenever required eleminating the need to add call function in every module. Making code more develooper friendly
# By Rishabhjain2010

import pymongo

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
    return get_collection('BEMSystem', 'event')

def dbconnect_user():
    """Get the 'users' collection from the 'BEMSystem' database."""
    return get_collection('BEMSystem', 'users')

def dbconnect_employee():
    """Get the 'employee' collection from the 'BEMSystem' database."""
    return get_collection('BEMSystem', 'employee')

def dbconnect_sales():
    """Get the 'sales' collection from the 'BEMSystem' database."""
    return get_collection('BEMSystem', 'sales')

def dbconnect_accounts():
    """Get the 'accounts' collection from the 'BEMSystem' database."""
    return get_collection('BEMSystem', 'accounts')
