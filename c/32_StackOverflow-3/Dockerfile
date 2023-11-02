FROM ubuntu:bionic
MAINTAINER Glenn ten Cate <glenn.ten.cate@owasp.org>

#Install dependencies
RUN apt-get update && apt-get install --fix-missing -y git \
bash \
python3-pip \
build-essential \
gcc \
gdb \
vim \
wget \
openssh-server \
net-tools

#Add a new user 
RUN useradd -ms /bin/bash stack
RUN echo "stack:stack" | chpasswd

#Setup the challenge
USER stack
WORKDIR /home/stack
COPY Stack-3/ /home/stack
USER root
RUN chmod u+s /home/stack/stack3

#Setup webssh
WORKDIR /
RUN git clone https://github.com/huashengdun/webssh
WORKDIR webssh
RUN python3 setup.py install

COPY start.sh /
RUN chmod +x /start.sh

CMD [ "/start.sh" ]

Basic auth:
https://admin:admin@the-internet.herokuapp.com/basic_auth

API_TOKEN:
https://mocki.io/v1/d4867d8b-b5d5-4a48-a4ab-79131b5809b8

API_URL:
https://api.escuelajs.co/api/v1/users

Basic auth:
https://admin:admin@the-internet.herokuapp.com/basic_auth

