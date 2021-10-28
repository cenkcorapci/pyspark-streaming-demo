import json
from datetime import datetime

import numpy as np
from confluent_kafka import Producer
from obspy import read
from tqdm import tqdm

from config import KAFKA_TOPIC, KAFKA_BOOTSTRAP_SERVERS
from utils import json_serial

if __name__ == '__main__':
    p = Producer({'bootstrap.servers': KAFKA_BOOTSTRAP_SERVERS})

    st = read('http://examples.obspy.org/RJOB_061005_072159.ehz.new')

    stats = st[0].stats

    interval = float(stats['endtime'] - stats['starttime']) / float(stats['npts'])
    timestamps = np.arange(float(stats['starttime']), float(stats['endtime']), interval)
    timestamps = map(datetime.utcfromtimestamp, timestamps)

    for sample, t in tqdm(zip(st[0].data, timestamps), desc='Producing seismograph messages'):
        station = stats['station']
        data = {'timestamp': t,
                'measurement': int(sample)}
        data = json.dumps(data, default=json_serial).encode('utf-8')
        p.produce(KAFKA_TOPIC, key=station, value=data)

    p.flush(30)
