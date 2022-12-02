FROM python:3.11-alpine

WORKDIR /consumer

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN echo KAFKA_TOPIC="eyyg" > .env
RUN echo KAFKA_HOSTNAME="kafka" >> .env
RUN echo KAFKA_PORT="9092" >> .env
RUN echo DB_NAME="postgres" >> .env
RUN echo POSTGRES_USER="postgres" >> .env
RUN echo POSTGRES_PASSWORD="postgres" >> .env
RUN echo POSTGRES_HOST="postgres" >> .env


CMD ["python", "consumer.py"]
