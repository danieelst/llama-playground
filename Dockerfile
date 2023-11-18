FROM ubuntu:latest

ARG FILE_NAME
ENV PATH_TO_MODEL_FILE /llama-model/$FILE_NAME
COPY $FILE_NAME /llama-model/$FILE_NAME


COPY prompt.py prompt.py
COPY requirements.txt requirements.txt

RUN apt-get -y update \
    && apt-get -y install \
    && apt-get install -y python3 \
    && apt-get install -y python3-pip \
    && apt-get install -y nano

# Install Python requirements
RUN pip install -r requirements.txt

WORKDIR /
