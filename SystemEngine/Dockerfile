#Dockerfile
FROM python:3.11.4

ADD main.py .

RUN pip install pandas numpy

#pymongo (MongoDB Connecter for Python)
RUN pip install pymongo  

CMD [ "python", "root.py" ]
