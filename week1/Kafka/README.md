```bash
echo KAFKA_BIN=<KAFKA_PATH_BIN> \
	  KAFKA_CONF=<KAFKA_PATH_CONFIG> \
	  KAFKA_HOST=<KAFKA_HOSTNAME> | localhost \
	  KAFKA_PORT=<KAFKA_PORT> | 9092
>> .env
```

```bash
Usage: console.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  client
  kafka
  topic
  zookeeper
```

```bash
Usage: console.py client [OPTIONS]

Options:
  -t, --type [consumer|producer]  [required]
  -T, --topic TEXT                [required]
  --message TEXT
  --file TEXT
  --help                          Show this message and exit.
```

```bash
Usage: console.py kafka [OPTIONS]

Options:
  --status [start|stop]  [required]
  --help                 Show this message and exit.
```

```bash
Usage: console.py zookeeper [OPTIONS]

Options:
  --status [start|stop]  [required]
  --help                 Show this message and exit.
```
