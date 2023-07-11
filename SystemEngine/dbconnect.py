#                                                           By Rishabhjain2010      

#This is a function module file used to connect with database whenever required eleminating the need to add call function in every module. Making code more develooper friendly

import pymongo

def dbconnect_event():
    client = MongoClient('mongodb://localhost:27017/')
    db = client['image_database']
    collection = db['event']


def dbconnect_user():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mongo = myclient["BEMSystem"]
    collection = mongo["users"]