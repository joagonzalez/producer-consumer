from src.logger import logging
from src.producer import LogsProducer 
from src.config.settings import config


if __name__ == '__main__':
    logging.info(f'hello to {config["APPLICATION"]} - Producer')
    producer = LogsProducer()
    producer.write()
