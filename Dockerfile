FROM python:latest

ENV PYTHONUNBUFFERED 1

COPY . /code/
WORKDIR /code/

RUN pip install -r requirements.txt


EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]