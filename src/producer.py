import json
import time
from kafka import KafkaProducer

from src.logger import logging
from src.config.settings import config
from src.services.data_reader import Reader


class LogsProducer:
     def __init__(self):
          self.broker = config['SERVER']
          self.topic = config['TOPIC']
          self.freq = config['FREQUENCY']
          self.group_id = ''
          self.producer = self._activate_producer()

     def _activate_producer(self):
          """
          Create a connection with kafka brokers to a specific topic
          to be used by producer functions
          
          :return: Object for connection handling
          """
          try:
               producer = KafkaProducer(bootstrap_servers=self.broker, 
                                        value_serializer=lambda x: json.dumps(x).encode('utf-8')      
                                        )
               logging.debug(f'Producer is ready on {self.topic}')
               return producer
          except Exception as e:
               logging.error(f'Error trying to connect with kafka brokers. Error: {e}')

     def write(self):
        data = Reader()
        data = data.build()

        for point in data:
            try:
                self.producer.send(self.topic, value=point)
                logging.debug(f'Message sent to broker: {point}')
                time.sleep(self.freq)
            except Exception as e:
                logging.error(f'Cant write data into broker. Error: {e}')


if __name__ == '__main__':
    pass