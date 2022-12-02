import os
import sys
import subprocess
import click
#import pexpect
#import asyncio

#from enum import Enum

KAFKA_BIN = None
KAFKA_CONF = None
KAFKA_HOSTNAME = None
KAFKA_PORT = None


# class ConsoleType(Enum):
#     CONSUMER = "consumer"
#     PRODUCER = "producer"


# async def start_consumer(cmd, after_receive):
#     callback = None
#
#     if after_receive:
#         file, func = after_receive.split(':')
#         file_path = f"{os.getcwd()}/{file}.py"
#
#         import importlib.util
#         spec = importlib.util.spec_from_file_location(file, file_path)
#         f = importlib.util.module_from_spec(spec)
#         spec.loader.exec_module(f)
#         callback = f.run
#
#     with subprocess.Popen(cmd, stdout=subprocess.PIPE) as p:
#         async for line in p.stdout:
#             data = line.decode('utf-8')
#             print("[RECEIVED] " + data)
#             if callback:
#                 await callback(data)
#
#
# def start_producer(cmd, message=None, file=None):
#     p = pexpect.spawn(" ".join(cmd))
#     p.expect('>')
#
#     status = True
#     while status:
#         if file:
#             with open(file, "r") as f:
#                 s = f.read()
#
#             for i in s.split('\n'):
#                 p.sendline(bytes(i, 'utf-8'))
#
#             status = False
#         else:
#             p.sendline(bytes(message or input(">> "), 'utf-8'))
#
#     if p.returncode != 0:
#         raise subprocess.CalledProcessError(p.returncode, p.args)


@click.group()
def cli():
    pass

#
# @cli.add_command
# @click.command()
# @click.option('--type', '-t', '_type', prompt="type", required=True, type=click.Choice(['consumer', 'producer']))
# @click.option('--topic', '-T', prompt="topic", required=True)
# @click.option('--message', required=False)
# @click.option('--file', required=False, type=str)
# @click.option('--after-receive')
# def client(_type, topic, message, file, after_receive):
#     cmd = [
#         KAFKA_BIN + f'/kafka-console-{_type}.sh',
#         '--topic',
#         topic,
#         '--bootstrap-server',
#         KAFKA_HOST + ':' + KAFKA_PORT
#     ]
#
#     if _type == ConsoleType.CONSUMER.value:
#         asyncio.run(start_consumer(cmd, after_receive))
#     elif _type == ConsoleType.PRODUCER.value:
#         print("PRODUCER")
#         start_producer(cmd, message, file)


@cli.add_command
@click.command()
@click.option('--status', type=click.Choice(['start', 'stop']), required=True)
def zookeeper(status):
    cmd = [
        KAFKA_BIN + f'/zookeeper-server-{status}.sh',
        KAFKA_CONF + '/zookeeper.properties'
    ]

    subprocess.run(cmd)


@cli.add_command
@click.command()
@click.option('--status', type=click.Choice(['start', 'stop']), required=True)
def kafka(status):
    cmd = [
        KAFKA_BIN + f'/kafka-server-{status}.sh',
        KAFKA_CONF + '/server.properties'
    ]

    subprocess.run(cmd)


@cli.add_command
@click.command()
@click.option('--name', required=True)
def topic(name):
    cmd = [
        KAFKA_BIN + f'/kafka-topics.sh',
        '--create',
        '--topic',
        name,
        '--bootstrap-server',
        KAFKA_HOSTNAME + ':' + KAFKA_PORT

    ]

    subprocess.run(cmd)


if __name__ == '__main__':
    from dotenv import load_dotenv
    load_dotenv()

    KAFKA_BIN = os.environ.get('KAFKA_BIN')
    KAFKA_CONF = os.environ.get('KAFKA_CONF')
    KAFKA_HOSTNAME = os.environ.get('KAFKA_HOSTNAME')
    KAFKA_PORT = os.environ.get('KAFKA_PORT')

    cli()
