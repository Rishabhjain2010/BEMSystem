#Dockerfile
FROM python:3.11.4
WORKDIR /SystemEngine
COPY . /SystemEngineDocker

#RUN pip install --no-cache-dir -r requirements.txt
RUN pip install numpy

#pymongo (MongoDB Connecter for Python)
RUN pip install pymongo  

CMD [ "python", "root.py" ]
