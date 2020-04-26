FROM ubuntu:18.04
COPY requirements.txt /app/
SHELL ["/bin/bash", "-c"]
RUN apt-get update && \
    apt-get install -y \
    python3-pip && \
    pip3 install -r requirements.txt
COPY . /app/
RUN python3 /app/kladama_test.py
