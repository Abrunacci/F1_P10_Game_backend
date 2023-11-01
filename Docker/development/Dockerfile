FROM python:3.10
LABEL authors="abrunacci"

RUN apt update

ENV PYTHONPATH=/app/src

COPY . /app
WORKDIR /app

RUN pip install --upgrade pip
RUN pip install -r Docker/development/requirements.txt
RUN poetry config virtualenvs.create false
RUN poetry install
EXPOSE 8000
