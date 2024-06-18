import cv2
import base64
from PIL import Image
import io
import pymongo
import face_recognition
import numpy as np
import matplotlib.pyplot as plt
import time

def capture_image_from_webcam():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        raise Exception("Could not open video device")

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    ret, frame = cap.read()

    if not ret:
        raise Exception("Failed to capture image")

    cap.release()
    cv2.destroyAllWindows()

    return frame

def convert_image_to_base64(image):
    image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    buffered = io.BytesIO()
    image.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")

    return img_str

def store_image_in_mongodb(image_base64, db_name="image_db", collection_name="images"):
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client[db_name]
    collection = db[collection_name]

    image_document = {
        "image_data": image_base64
    }

    collection.insert_one(image_document)
    print("Image stored in MongoDB")

def retrieve_image_from_mongodb(db_name="image_db", collection_name="images"):
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client[db_name]
    collection = db[collection_name]

    # Retrieve the most recent image document
    image_document = collection.find_one(sort=[('_id', pymongo.DESCENDING)])
    image_base64 = image_document['image_data']

    # Decode the base64 string
    img_data = base64.b64decode(image_base64)
    image = Image.open(io.BytesIO(img_data))
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    return image

def verify_faces(image1, image2):
    # Get face encodings for each face in the image
    image1_encodings = face_recognition.face_encodings(image1)
    image2_encodings = face_recognition.face_encodings(image2)

    if len(image1_encodings) == 0:
        print("No faces found in the stored image.")
        return False

    if len(image2_encodings) == 0:
        print("No faces found in the new image.")
        return False

    # Compare faces
    results = face_recognition.compare_faces([image1_encodings[0]], image2_encodings[0])
    return results[0]

# Capture and store an image
def capture_img(): 
    # print("Press any key to capture the image...")
    image = capture_image_from_webcam()
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show(block=False)
    # input("Press Enter to continue...")
    if face_recognition.face_encodings(image):
        image_base64 = convert_image_to_base64(image)
        # print(image_base64)
        return image_base64
    else:
        print("No faces detected in the image. Please Retry.")
        input("Press Enter to continue...")
        return capture_img()
    

# Capture another image for verification

def verify_img(image_db):
    
    input("Press any key to capture the image for verification...")
    new_image = capture_image_from_webcam()
    print("Image Captured Successfully")
    plt.imshow(cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show(block=False)
    input("Press Enter to continue...")
    if not face_recognition.face_encodings(new_image):
        print("No faces detected in the second image. Please Retry.")
        verify_img(image_db)

    # Retrieve the stored image from MongoDB
    img_data = base64.b64decode(image_db)
    image = Image.open(io.BytesIO(img_data))
    stored_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)


    # Verify if the new image matches the stored image
    print("Verifying the images...")
    is_match = verify_faces(stored_image, new_image)
    if is_match:
        print("Identity match!")
        time.sleep(10)
        return True
    else:
        # print("Identity do not match. Press enter to retry.")
        retry= input("Identity do not match. Press enter to retry.")
        if retry == "":
            verify_img(image_db)
        else:
            return False


#capture_img()
#verify_img()