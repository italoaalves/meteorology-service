FROM python:3.10

ENV LANG pt_BR.UTF-8

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./src /app

CMD [ "python", "./app.py" ]
