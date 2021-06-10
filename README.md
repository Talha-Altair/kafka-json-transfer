
# Kafka Json Transfer

A Simple App that instantiates a file data transfer
between a local producer and a local consumer


## Running Tests

Install dependencies:

```bash
$ pip install -r requirements.txt
```

## Download Kafka Server Files

https://kafka.apache.org/quickstart

Change server.properties to localhost advertised listener

## Start Kafka server:

```bash
$ JMX_PORT=8004 bin/kafka-server-start.sh config/server.properties 
```
## Start Kafka Zookeeper:
```bash
$ bin/zookeeper-server-start.sh config/zookeeper.properties
```
## Test message consumer:
```bash
$ bin/kafka-console-consumer.sh --topic quickstart-events --bootstrap-server localhost:9092
```
## Test message producer:
```bash
$ bin/kafka-console-producer.sh --topic quickstart-events --bootstrap-server localhost:9092 
```
## Kafka Manager:

```bash
git clone git@github.com:yahoo/CMAK.git

cd CMAK/target/universal/cmak-3.0.0.5 

$ bin/cmak -Dconfig.file=conf/application.conf -Dhttp.port=8080
```

