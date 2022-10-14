FROM python:3.10

WORKDIR /app
COPY . .

RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

CMD python main.py \
  -U $POSTGRES_USER \
  -W $POSTGRES_PASSWORD \
  -H $POSTGRES_HOST \
  -p $POSTGRES_PORT \
  -D $POSTGRES_DB \
  --token $TOKEN \
  --keyword $KEYWORD  \
  --max-results $MAX_RESULTS \
  --iteration $ITERATION