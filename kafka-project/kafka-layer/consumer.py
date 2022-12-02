import os
import sys
import threading

from typing import Any, Callable, List

from kafka import KafkaConsumer


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
            listener(message)

    threading.Thread(target=poll).start()
    print("thread is running on background")


def kafka_listener(other: Any):
    #print("[PROGRESS] - ", other)
    pass


def main():
    kafka_topic = os.environ['KAFKA_TOPIC']
    kafka_host =  os.environ['KAFKA_HOSTNAME']
    kafka_port = os.environ['KAFKA_PORT']

    kafka_bootstrap_servers = [f'{kafka_host}:{kafka_port}']

    join_kafka(topic=kafka_topic,
               bootstrap_servers=kafka_bootstrap_servers,
               listener=kafka_listener)


if __name__ == '__main__':
    from dotenv import load_dotenv
    load_dotenv()
    
    sys.exit(main())
