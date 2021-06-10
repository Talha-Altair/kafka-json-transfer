from kafka import KafkaProducer
import json
import data
import time

USERS_JSONPATH = "static_producer/words.json"

def json_serializer(data):
    return json.dumps(data).encode("utf-8")

# def get_partition(key, all, available):
#     return 0

def get_json():

    json_file = open(USERS_JSONPATH)
    json_data = json.load(json_file)

    return json_data

if __name__ == '__main__':

    producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer = json_serializer,
    )

    data = get_json()

    producer.send("altair-data-services",data)

    time.sleep(3)