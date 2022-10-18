FROM python:3.10-slim-buster

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN apt-get update && apt-get install -y default-libmysqlclient-dev
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./backend /app/backend

CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "80"]