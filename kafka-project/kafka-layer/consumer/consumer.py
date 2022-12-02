import os
import sys
import threading
import json

from datetime import datetime
from typing import Any, Callable, List

from kafka import KafkaConsumer
from psycopg2 import connect


def join_kafka(*, 
               topic: str,
               bootstrap_servers: List[str],
               listener: Callable):
    def poll():
        consumer = KafkaConsumer(topic,
                                 bootstrap_servers=bootstrap_servers)

        print("Consumer is being started for polling...")
        try:
            consumer.poll(timeout_ms=5000)
            print("Consumer is polling now from: ", topic)
        except Exception as e:
            raise Exception("Polling process is failed")

        for message in consumer:
            print("[RECEIVED] - ", str(message.key, 'utf-8'))
            try:
                listener(message)
            except:
                return

    threading.Thread(target=poll).start()
    print("thread is running on background")


def kafka_listener(other: Any):
    try:
        conn = connect(
            dbname=os.environ['DB_NAME'],
            user=os.environ['POSTGRES_USER'],
            host=os.environ['POSTGRES_HOST'],
            password=os.environ['POSTGRES_PASSWORD']
        )
        cursor = conn.cursor()
    except Exception as e:
        print("ERROR", e)
        return

    data = str(other.value, encoding='utf-8')
    data = json.loads(data)

    #_id = str(other.key, encoding='utf-8')
    _host = data['host']
    _user = data['user']
    _request_time = datetime.fromtimestamp(data['request_time'])
    _status = data['status']
    _bytes_sent = data['bytes_sent']
    _bytes_out = data['bytes_out']
    print(_request_time)

    (_request_method,
     _request_endpoint,
     _request_http_version) = data['request_line'].split(' ')

    try:
        cursor.execute(f"""
            INSERT INTO serverlog
               (request_host,
                request_user,
                request_time,
                request_status,
                request_bytes_sent,
                request_bytes_out,
                request_method,
                request_endpoint,
                request_http_version)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, 
            (
            _host,
            _user,
            _request_time,
            _status,
            _bytes_sent,
            _bytes_out,
            _request_method,
            _request_endpoint,
            _request_http_version
            ))
        conn.commit()
        cursor.close()
        conn.close()
        #_ = cursor.fetchone()[0]
        print("INSERTED")
    except Exception as e:
        print("ERROR", e)



def main():
    kafka_topic = os.environ.get('KAFKA_TOPIC', 'eyyg')
    kafka_host =  os.environ.get('KAFKA_HOSTNAME', 'localhost')
    kafka_port = os.environ.get('KAFKA_PORT', 9092)

    kafka_bootstrap_servers = [f'{kafka_host}:{kafka_port}']

    print(kafka_topic, kafka_bootstrap_servers)

    join_kafka(topic=kafka_topic,
               bootstrap_servers=kafka_bootstrap_servers,
               listener=kafka_listener)


if __name__ == '__main__':
    from dotenv import load_dotenv
    load_dotenv()
    
    sys.exit(main())
