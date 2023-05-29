# syntax=docker/dockerfile:1
FROM python:3.7
WORKDIR /app
#RUN chmod g+w .
#RUN chmod g+w /app
COPY requirements.txt requirements.txt
# COPY copyFromS3.sh copyFromS3.sh
# RUN chmod +x copyFromS3.sh
# RUN chmod -R 777 .
RUN apt-get update
RUN apt-get install -y libsasl2-dev
RUN apt-get install -y libsasl2-modules
RUN apt-get install gcc g++ libsasl2-dev -y
#RUN apt-get update && apt-get install -y default-jdk
RUN apt-get updat           e && apt-get install -y openjdk-11-jdk
#Set environment variables
ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64
ENV PATH "$PATH:$JAVA_HOME/bin"
RUN pip3 install --upgrade setuptools
# RUN pip3 install sasl
RUN pip3 install -r requirements.txt
COPY . .
#CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
CMD ["python3", "index.py"]