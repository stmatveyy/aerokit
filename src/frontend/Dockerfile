FROM baseImage

WORKDIR /app
RUN pip install pipenv
RUN pipenv install

COPY /app .
RUN pipenv shell

ENTRYPOINT ["streamlit", "run", "src/frontend/app/main.py"]

