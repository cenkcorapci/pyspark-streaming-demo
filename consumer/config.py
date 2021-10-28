import os

KAFKA_TOPIC = os.getenv('KAFKA_TOPIC', 'seismograph')
KAFKA_BOOTSTRAP_SERVERS = os.getenv('KAFKA_BOOTSTRAP_SERVERS', 'localhost:9091')
ZOOKEEPER_ADDRESS = os.getenv('ZOOKEEPER_ADDRESS', 'localhost:2181')
BATCH_DURATION = os.getenv('BATCH_DURATION',
                           1)  # the time interval (in seconds) at which streaming data will be divided into batches
SPARK_APP_NAME = os.getenv('SPARK_APP_NAME', 'seismograph-consumer')
