import json
from kafka import KafkaConsumer

from src.logger import logging
from src.config.settings import config


class LogsConsumer:
     def __init__(self):
          self.broker = config['SERVER']
          self.topic = config['TOPIC']
          self.group_id = ''
          self.consumer = self._activate_listener()

     def _activate_listener(self):
          """
          Create a connection with kafka brokers to a specific topic
          to be used by consumer functions
          
          :return: Object for connection handling
          """
          try:
               consumer = KafkaConsumer(self.topic,
                                        bootstrap_servers=self.broker,
                                        consumer_timeout_ms=60000,
                                        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
                                        #auto_offset_reset='earliest',
                                        #group_id='consumers',
                                        #enable_auto_commit=True,
                                        #value_deserializer=lambda m: json.loads(m.decode('ascii'))        
                                        )
               logging.debug(f'Consumer is listening on {self.topic}')
               return consumer
          except Exception as e:
               logging.error(f'Error trying to connect with kafka brokers. Error: {e}')

     def read(self):
          for msg in self.consumer:
               try:
                    print(f'Message from topic {self.topic}: {msg}')
               except Exception as e:
                    print('error reading')
     
     def __del__(self):
          try:
               self.consumer.close()
          except Exception as e:
               logging.warning(f'Error closing connection or connection with broker not established...')


if __name__ == '__main__':
     pass