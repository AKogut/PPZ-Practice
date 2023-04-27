FROM python:3.9

ENV PYTHONUNBUFFERED=1
RUN pip install django
WORKDIR ./lab7

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . /lab7/