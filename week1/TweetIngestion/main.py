import argparse
import logging
import sys
import requests

from sqlalchemy import create_engine
from pprint import pprint

EXIT_SUCCESS = 0
EXIT_ERROR = 1
URI = "https://api.twitter.com/2/tweets/search/recent"

logging.basicConfig(level=logging.DEBUG)

def auth(r, bearer_token: str) -> any:
    """
    'https://api.twitter.com/2/tweets/search/recent?query=from:twitterdev' --header 'Authorization: Bearer $BEARER_TOKEN'
    """
    r.headers['Authorization'] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "TweetIngestion"

    return r

def make_request(*args) -> dict | int:
    api_key, secret, bearer_token, params = args
    params_list = params.split("&")
    params_dict = dict([i.split("=") for i in params_list])

    try:
        response = requests.request("GET", URI, 
                                    auth=lambda _: auth(_, bearer_token),
                                    params=params_dict)
        logging.info(f"GET {response.url}")
    except Exception as e:
        logging.error(f"GET {e}")

    return response

def main(args: dict[str, str | int]) -> int:
    username, password, host, port, database, *rest = args.values()
    postgres_uri: str = f'postgresql://{username}:{password}@{host}:{port}/{database}'
                    
    try:
        engine = create_engine(postgres_uri)
        logging.info(f"PostgreSQL engine is created: {postgres_uri}")
    except Exception as e:
        logging.error(f"PostgreSQL engine is not created: {e}")
        return EXIT_ERROR

    response = make_request(*rest)

    if response.status_code != 200:
        return EXIT_ERROR

    # CONVERT THE DATA TO pandas df, then save to PostgreSQL table
    pprint(response.json())

    return EXIT_SUCCESS

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Tweet Ingestion')

    parser.add_argument('-U', '--username', type=str,
                        help='database user name', default="postgres")
    parser.add_argument('-W', '--password', type=str,
                        help='database password', default="postgres")
    parser.add_argument('-H', '--host', type=str,
                        help='database server host', default="localhost")
    parser.add_argument('-p', '--port', type=int,
                        help='database server port', default=5432)
    parser.add_argument('-D', '--database', type=str,
                        help='database name', required=True)
    parser.add_argument('--api_key', type=str,
                        help='TwitterAPI API Key')
    parser.add_argument('--secret', type=str,
                        help='TwitterAPI Secret Key')
    parser.add_argument('--bearer_token', type=str,
                        help='TwitterAPI Bearer Token', required=True)
    parser.add_argument('--params', type=str,
                        help='Params to search', required=True)


    args = parser.parse_args()
    sys.exit(main({"username": args.username,
                    "password": args.password,
                    "host": args.host,
                    "port": args.port,
                    "database": args.database,
                    "api_key": args.api_key,
                    "secret": args.secret,
                    "bearer_token": args.bearer_token,
                    "params": args.params
    }))

