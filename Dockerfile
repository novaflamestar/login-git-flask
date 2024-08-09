FROM python:3.11.9-bullseye

RUN mkdir /app
COPY app.py /app/app.py
COPY requirements.txt /app/requirements.txt
WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT [ "python", "app.py" ]
