#Dockerfile
FROM python:3.11.4
#workdirectory
WORKDIR /App-SystemEngine
COPY root.py /App-SystemEngine

RUN pip install numpy 
#pymongo (MongoDB Connecter for Python)
RUN pip install pymongo  
CMD [ "python", "root.py" ]
