FROM python:3.11-alpine

WORKDIR /consumer

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "consumer.py"]
