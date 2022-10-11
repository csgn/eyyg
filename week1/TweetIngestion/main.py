import argparse
import logging
import sys
import requests
import pandas as pd


from sqlalchemy import create_engine
from pprint import pprint

logging.basicConfig(level=logging.DEBUG)


class TweetSession:
    URL = "https://api.twitter.com/2/tweets/search/recent/"

    def __init__(self, token: str) -> None:
        self.session = requests.Session()
        self.session.headers.update({"Authorization": f'Bearer {token}'})

    def get(self, q: str):
        return self.session.get(self.URL, params=q)


def init_engine(*, username, password, host, port, database):
    uri = f'postgresql://{username}:{password}@{host}:{port}/{database}'

    try:
        engine = create_engine(uri)
        engine.connect()
        logging.info(f"PostgreSQL engine is created: {uri}")
    except Exception as e:
        logging.error(f"PostgreSQL engine is not created: connection was refused {uri}")
        return

    return engine

    

def make_request(session, keyword, iteration, max_results):
    q = {
        "query": keyword,
        "max_results": max_results
    }

    for _ in range(iteration):
        next_query = "&".join(list(map(lambda x: f"{x[0]}={x[1]}",
                                       q.items())))

        res = session.get(q=next_query)
        res_data = res.json()
        next_token = res_data['meta']['next_token']

        if next_token:
            q["next_token"] = next_token

        yield res_data["data"]



def main(args) -> int:
    tweet_session = TweetSession(token=args.token)

    db = init_engine(username=args.username,
                       password=args.password,
                       host=args.host,
                       port=args.port,
                       database=args.database)

    if not db:
        return 0

    it = make_request(tweet_session,
                      args.keyword,
                      args.iteration,
                      args.max_results)



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
    parser.add_argument('--token', type=str,
                        help='TwitterAPI Bearer Token', required=True)
    parser.add_argument('--keyword', type=str,
                        help='Keyword to search', required=True)
    parser.add_argument('--max-results', type=int,
                        help='Search result per iteration', default=10)
    parser.add_argument('--iteration', type=int,
                        help='Total request number', default=1)

    args = parser.parse_args()
    sys.exit(main(args))

