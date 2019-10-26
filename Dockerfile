FROM python:3.7

RUN pip3 install pip --upgrade \
    && pip3 install pipenv

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /htdocs/www
WORKDIR /htdocs/www

EXPOSE 8000
