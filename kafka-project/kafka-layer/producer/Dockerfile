FROM python:3.11-alpine

WORKDIR /producer

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "producer.py", "logfiles.log"]
