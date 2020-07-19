# Use ubuntu as a base image
from ubuntu:latest

#Install python3-pip and python3-dev
RUN apt-get update \
    && apt-get install -y python3-pip python3-dev \
    && ln -s /usr/bin/python3 python \
    && pip3 install --upgrade pip \
    && apt-get install -y nano \
    && apt-get install -y iputils-ping \
    && apt install -y curl \
    && apt install -y wget

WORKDIR /app
COPY . /app
RUN pip3 --no-cache-dir install -r requirements.txt
EXPOSE 5000
CMD ["python3","app.py"]
