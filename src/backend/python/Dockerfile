FROM python:3.12.6

WORKDIR /app
RUN pip install pipenv
COPY ./Pipfile ./Pipfile
RUN pipenv install

COPY /app .



