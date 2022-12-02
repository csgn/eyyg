import os
import sys
import time
import json
import uuid

from kafka import KafkaProducer
from utils import log_parser


def read_chunk(fp):
    while True:
        other = fp.readline()

        if not other:
            break

        yield other

def main():
    kafka_topic = os.environ['KAFKA_TOPIC']
    kafka_host =  os.environ['KAFKA_HOSTNAME']
    kafka_port = os.environ['KAFKA_PORT']

    kafka_bootstrap_servers = [f'{kafka_host}:{kafka_port}']

    producer = KafkaProducer(bootstrap_servers=kafka_bootstrap_servers,
                             value_serializer=lambda v: json.dumps(v,
                                                                   indent=4,
                                                                   default=str) \
                                                            .encode('utf-8'))

    if not producer:
        print("producer is not created")
        return

    with open('../assets/logfiles.log', 'r') as f:
        for chunk in read_chunk(f):
            time.sleep(0.05)
            parsed = log_parser.parser.parse(chunk)

            body = {
                "host": parsed.remote_host,
                "user": parsed.remote_user,
                "request_time": parsed.request_time.timestamp(),
                "status": parsed.final_status,
                "bytes_sent": parsed.bytes_sent,
                "bytes_out": parsed.bytes_out,
                "request_line": parsed.request_line,
            }

            key = str(uuid.uuid4())
            producer.send(topic=kafka_topic,
                          value=body,
                          key=bytes(key, encoding='utf-8'))

            print("[SENT]: ", key)
            #input(f"[SEND]: {chunk[:10]}")



if __name__ == '__main__':
    from dotenv import load_dotenv
    load_dotenv()

    sys.exit(main())
