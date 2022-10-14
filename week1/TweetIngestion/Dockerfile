FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY . .

RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

ENV USERNAME=postgres PASSWORD=postgres HOST=localhost PORT=5432 MAX_RESULTS=100 ITERATION=3 TOKEN=<BEARER_TOKEN>

CMD python main.py -U $USERNAME -W $PASSWORD -H $HOST -p $PORT -D $DATABASE --token $TOKEN --keyword $KEYWORD --max-results $MAX_RESULTS --iteration $ITERATION
