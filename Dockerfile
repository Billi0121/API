FROM python:3.13-slim

RUN mkdir /app

COPY requirements.txt /app

RUN pip3 install -r /app/requirements.txt --no-cache-dir

COPY kittygram/ /app

WORKDIR /app

CMD ["python", "manage.py", "runserver", "0:8000"]