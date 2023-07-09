#                                                           By RishabhJain2010     

import cv2
from matplotlib import pyplot as plt
from pymongo import MongoClient
import io

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['image_database']
collection = db['images']

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

# Insert the image into MongoDB
image_data = {
    'image': image_bytes
}
collection.insert_one(image_data)

# Release the camera
camera.release()

