FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN mkdir /django_project

COPY ./app /django_project/
COPY requirements.txt /django_project/

RUN pip install -r /django_project/requirements.txt

WORKDIR /django_project

# RUN python manage.py migrate
    # && python manage.py createsuperuser \
    #     --noinput \
    #     --username ${DJANGO_SUPERUSER_USERNAME} \
    #     --email ${DJANGO_SUPERUSER_EMAIL}\