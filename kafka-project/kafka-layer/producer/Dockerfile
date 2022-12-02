FROM python:3.11-alpine

WORKDIR /producer

COPY . .

RUN pip install -r requirements.txt

RUN echo KAFKA_TOPIC="eyyg" > .env
RUN echo KAFKA_HOSTNAME="kafka" >> .env
RUN echo KAFKA_PORT="9092" >> .env

CMD ["python", "producer.py"]
