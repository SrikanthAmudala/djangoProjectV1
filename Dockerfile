FROM python:3

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY . /code/

RUN pip install -r requirement.txt
EXPOSE 8989
#ENTRYPOINT python manage.py runserver 0.0.0.0:8989