#FROM python:3.9-buster
#FROM debian:stable
FROM debian:stable-slim

RUN apt-get update && apt-get install -yq \
    xsel \
    unzip \
    libgconf-2-4 \
    libncurses5 \
    libxml2-dev \
    libxslt-dev \
    libz-dev \
    libgirepository1.0-dev \
    libcairo2-dev \
    xclip

RUN apt-get install -y curl xvfb wget python3 python3-pip mlocate
RUN apt install -y libcairo2-dev pkg-config python3-dev
#RUN locate pip3
#RUN dpkg -L python3-pip


RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY ./requirements.txt /usr/src/app/
RUN /usr/bin/pip3 install --no-cache-dir -r requirements.txt
COPY ./ /usr/src/app
CMD ["python3","-u", "app.py"]