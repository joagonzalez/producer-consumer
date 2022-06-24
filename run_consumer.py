from src.logger import logging
from src.consumer import LogsConsumer
from src.config.settings import config


if __name__ == '__main__':
    logging.info(f'hello to {config["APPLICATION"]} - Consumer')
    consumer = LogsConsumer()
    consumer.read()

