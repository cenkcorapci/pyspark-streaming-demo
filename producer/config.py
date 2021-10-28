import os

KAFKA_TOPIC = os.getenv('KAFKA_TOPIC', 'seismograph')
KAFKA_BOOTSTRAP_SERVERS = os.getenv('KAFKA_BOOTSTRAP_SERVERS', 'localhost:9091')
