#                                                               By Rishabhjain2010
#                                                               Date: 2024/04/06
#                                                               Time: 04:51:00

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
RUN pip install Matplotlib
RUN pip install bcrypt


CMD [ "python", "root.py" ]
