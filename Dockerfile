FROM python:3.6
WORKDIR /usr/src/

COPY . .
RUN pip install -r requirements.txt