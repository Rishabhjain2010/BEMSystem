#                               Rishabhjain2010     

#This function is an automated image verification which captures images live from web cam and then matches the images from iages available in our database.
#If the image matches with the image in our database then it returns true else it returns false.
#This function is called in the function "personverification" in the file "personverification.py" in the folder "security verification" in the folder "eventsAndBookings" in the folder "SystemEngine".
#This function also automatically mark the person has attended the event and no manual ticket checking is required.

#importing required modules.

import cv2
import pymongo  
import io
import matplotlib   