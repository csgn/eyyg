# Tweet Ingestion

## Usage
```sh
usage: main.py [-h] [-U USERNAME] [-W PASSWORD] [-H HOST] [-p PORT] -D
               DATABASE [--api_key API_KEY] [--secret SECRET] --bearer_token
               BEARER_TOKEN --params PARAMS

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
  --api_key API_KEY     TwitterAPI API Key
  --secret SECRET       TwitterAPI Secret Key
  --bearer_token BEARER_TOKEN
                        TwitterAPI Bearer Token
  --params PARAMS       Params to search
```

## Example
```
$ python main.py -D <DB_NAME> --bearer_token <BEARER_TOKEN> --params "query=python&max_results=10"
```

## TODOS
- [x] MAKE REQUEST
- [ ] CONVERT TO PANDAS DATAFRAME
- [ ] STORE TO POSTGRESQL TABLE
- [ ] CREATE DOCKERFILE AND BASHSCRIPT
