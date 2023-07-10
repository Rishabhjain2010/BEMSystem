#                               Rishabhjain2010     

#This function is an automated image verification which captures images live from web cam and then matches the images from iages available in our database.
#If the image matches with the image in our database then it returns true else it returns false.
#This function is called in the function "personverification" in the file "personverification.py" in the folder "security verification" in the folder "eventsAndBookings" in the folder "SystemEngine".
#This function also automatically mark the person has attended the event and no manual ticket checking is required.

#importing required modules.

import time
import cv2
import pymongo  
import io
import matplotlib 
 
#connecting to the database.
client = pymongo.MongoClient("mongodb://localhost:27017" )
db = client["database"]    
collection = db["eventid"]


#defining the function.

def authentication() :
    
    #image capture function
    #capture =  cv2.VideoCapture(0)
    #ret, frame = capture.read()
    #cv2.imwrite("captured_img.jpg", frame)
    #capture.release()

    # Remove background using OpenCV's grabCut algorithm
    #mask = cv2.GC_PR_BGD * (image != 0).astype('uint8')  # Set pixels not equal to zero as probable background
    #bgd_model = np.zeros((1, 65), dtype="float")
    #fgd_model = np.zeros((1, 65), dtype="float")
    #rect = (0, 0, image.shape[1], image.shape[0])
    #cv2.grabCut(image, mask, rect, bgd_model, fgd_model, 5, cv2.GC_INIT_WITH_MASK)

  #Method using BSON Format

    # Capture image from the webcam
     camera = cv2.VideoCapture(0)
     _, image = camera.read()

    # Remove background using OpenCV's grabCut algorithm
     mask = cv2.GC_PR_BGD * (image != 0).astype('uint8')  # Set pixels not equal to zero as probable background
     bgd_model = np.zeros((1, 65), dtype="float")
     fgd_model = np.zeros((1, 65), dtype="float")
     rect = (0, 0, image.shape[1], image.shape[0])
     cv2.grabCut(image, mask, rect, bgd_model, fgd_model, 5, cv2.GC_INIT_WITH_MASK)

    # Apply mask to the image to remove background
     output_image = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8') * 255
     output_image = cv2.bitwise_and(image, image, mask=output_image)

    # Display the processed image
     plt.imshow(cv2.cvtColor(output_image, cv2.COLOR_BGR2RGB))
     plt.show()
 
    # Convert the image to BSON format
     retval, buffer = cv2.imencode('.jpg', output_image)
     image_bytes = io.BytesIO(buffer).getvalue()
    
    #Finding Image in DataBase
     
     # Search for the image in MongoDB
     query = {"image": image_bytes}
     result = collection.find_one(query)

     if result:
        # Person found, authenticated
        time.sleep(2)
        print("Person authenticated.")
     else:
        # Person not found
        time.sleep(2)
        print("Person not found.")



