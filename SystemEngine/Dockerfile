#                                                               By Rishabhjain2010
#                                                               Date: 2023/07/11
#                                                               Time: 04:11:00

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
CMD [ "python", "root.py" ]
