FROM python:latest

ENV PYTHONUNBUFFERED 1

COPY . /app

RUN pip install ptvsd==3.0.0
RUN pip install -r /app/requirements.txt

WORKDIR /app/project

EXPOSE 8000
EXPOSE 8001

CMD python manage.py runserver 0.0.0.0:8000
