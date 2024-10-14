FROM python:3.12.6 

WORKDIR /app
RUN pip install pipenv
RUN pipenv install

COPY /app .
RUN pipenv shell

ENTRYPOINT ["uvicorn", "app.main:app", "--reload", "--port 8080"]
