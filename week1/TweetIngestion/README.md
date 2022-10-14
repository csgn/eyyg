# Tweet Ingestion

[![asciicast](https://asciinema.org/a/s7dqiHvqmIK6NW0SAKhMbn9dl.svg)](https://asciinema.org/a/s7dqiHvqmIK6NW0SAKhMbn9dl)

## Usage
```sh
usage: main.py [-h] [-U USERNAME] [-W PASSWORD] [-H HOST] [-p PORT] -D DATABASE --token TOKEN --keyword KEYWORD
               [--max-results MAX_RESULTS] [--iteration ITERATION]

Tweet Ingestion

options:
  -h, --help            show this help message and exit
  -U USERNAME, --username USERNAME
                        database user name
  -W PASSWORD, --password PASSWORD
                        database password
  -H HOST, --host HOST  database server host
  -p PORT, --port PORT  database server port
  -D DATABASE, --database DATABASE
                        database name
  --token TOKEN         TwitterAPI Bearer Token
  --keyword KEYWORD     Keyword to search
  --max-results MAX_RESULTS
                        Search result per iteration
  --iteration ITERATION
                        Total request number
```

## Example (postgres must be running)
```
$ python main.py -D <DB_NAME> --token <BEARER_TOKEN> --keyword <KEYWORD>
```

## or use Docker (POSTGRES_HOST must be 'db')
```bash
./run.sh -D <POSTGRES_DB> -t <BEARER_TOKEN> -k <KEYWORD> -H db
```
