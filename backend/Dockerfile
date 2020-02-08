FROM python:latest

RUN python -m pip install --upgrade pip

COPY requirements.txt requirements.txt
RUN python -m pip install -r requirements.txt

RUN python -m manage.py migrate
RUN python manage.py loaddata web/fixtures/initialdata.json

COPY . .
