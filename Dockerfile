FROM ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y python3.9 python3.9-dev python3-pip && apt-get clean && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .

RUN pip3 install -r requirements.txt
COPY . .
CMD ["python3", "main.py"]