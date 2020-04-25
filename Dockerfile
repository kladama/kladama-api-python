FROM ubuntu:18.04
SHELL ["/bin/bash", "-c"]
RUN apt-get update && \
    apt-get install -y \
    python3-pip && \
    pip3 install jsonlib-python3 && \
    pip3 install requests
COPY . /app/
RUN cd /app/src/ && \
    python3 kladama_test.py
