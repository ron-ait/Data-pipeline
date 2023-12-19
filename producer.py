from faker import Faker
from kafka import KafkaProducer
import json
import geojson
import time 
import random


producer = KafkaProducer(
    bootstrap_servers='localhost:29092',
    value_serializer= lambda x: json.dumps(x).encode('utf-8')
)

#def generate_random_location(): 
 #   latitude = random.uniform(-90,90)
 #   longitude =  random.uniform(-180,180)
  #  return (latitude, longitude)


fake = Faker()
i =0
while i < 100:
    message= {
        "name": fake.name(),
        "latitude": random.uniform(-90,90), 
        "longitude": random.uniform(-180,180),
        "phone": fake.phone_number()
        }
    kafka_key = 'message_update'.encode('utf-8')


    producer.send(
        topic='new-updates',
        key=kafka_key,
        value=message
    )
    i=i+1

