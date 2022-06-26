import logging
from src.config.settings import config

if config['DEBUG_LEVEL'] == 'DEBUG':
    logging.basicConfig(
        format='%(asctime)s:%(levelname)s:%(message)s', 
        level=logging.DEBUG)
elif config['DEBUG_LEVEL'] == 'WARNING':
    logging.basicConfig(
        format='%(asctime)s:%(levelname)s:%(message)s', 
        level=logging.WARNING)
elif config['DEBUG_LEVEL'] == 'ERROR':
    logging.basicConfig(
        format='%(asctime)s:%(levelname)s:%(message)s', 
        level=logging.ERROR)
elif config['DEBUG_LEVEL'] == 'INFO':
    logging.basicConfig(
        format='%(asctime)s:%(levelname)s:%(message)s', 
        level=logging.INFO)