FROM python:3.8

RUN useradd --create-home userapi
WORKDIR /films_api

RUN pip install -U pipenv
COPY Pipfile .
COPY Pipfile.lock .
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy --system
COPY ../Materials/ITVDN/Flask/lesson8_docerized/flask_dockerize-flask-materials/008_Samples/films_api .
RUN chown -R userapi:userapi ./
USER userapi

EXPOSE 8000
CMD gunicorn --bind 0.0.0.0:$PORT wsgi:app