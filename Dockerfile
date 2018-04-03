FROM python:3.5

ENV PYTHONUNBUFFERED 1

COPY . /app

RUN pip install -r /app/requirements.txt

WORKDIR /app/mysite

EXPOSE 8000

CMD python manage.py runserver 0.0.0.0:8000
