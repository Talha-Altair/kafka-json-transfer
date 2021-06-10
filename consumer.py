from kafka import KafkaConsumer
import json

USERS_JSONPATH = "static_consumer/words.json"

def store_data(json_data):

    with open(USERS_JSONPATH, 'w') as outfile:
        json.dump(json_data, outfile)


if __name__ == '__main__':

    consumer = KafkaConsumer(
        'altair-data-services',
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='smallest',
        enable_auto_commit=True,
        group_id='json-file-transfer',
        )

    print("starting consumer")

    for msg in consumer:

        print(msg)
        
        data = json.loads(msg.value)
        
        store_data(data)

        break

    
