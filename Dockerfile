FROM python:latest

ENV PYTHONUNBUFFERED 1

COPY . /app

RUN pip install -r /app/requirements.txt

WORKDIR /app/project

EXPOSE 8000

CMD python manage.py runserver 0.0.0.0:8000
