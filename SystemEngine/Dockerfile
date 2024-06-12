#                                                               By Rishabhjain2010
#                                                               Date: 2024/06/13
#                                                               Time: 01:09:00

#Dockerfile
FROM python:3.11.4

#workdirectory
WORKDIR /App-SystemEngine
COPY root.py /App-SystemEngine
COPY . /App-SystemEngine

RUN pip install numpy  

#pymongo (MongoDB Connecter for Python)
RUN pip install pymongo  

RUN pip install pandas

#AI Image Recognition
RUN pip install opencv-python

#Matplotlib (Visualization with python)
RUN pip install Matplotlib
RUN pip install tabulate
RUN pip install bcrypt
RUN sudo apt-get install libqt5gui5
RUN sudo apt install cmake
RUN pip install face_recognition
RUN pip install prettytable
RUN pip install pillow          
RUN 



CMD [ "python", "root.py" ]

