import os
from dotenv import load_dotenv

dotenv_path = os.getenv("API_DOTENV", os.path.join(os.path.dirname(__file__), ".env"))

load_dotenv(dotenv_path, override=False)  # priorizes env vars (not .env file)

config = {
    'TOPIC': os.getenv('KAFKA_TOPIC', ''),
    'SERVER': os.getenv('KAFKA_SERVER_1'),
    #'SERVER': [os.getenv('KAKFA_SERVER_1'),
    #           os.getenv('KAKFA_SERVER_2'),
    #           os.getenv('KAKFA_SERVER_3')
    #           ],
    'APPLICATION': os.getenv('APPLICATION'),
    'DEBUG_LEVEL': os.getenv('DEBUG_LEVEL'),
    'FILENAME': os.getenv('FILENAME'),
    'FREQUENCY': int(os.getenv('FREQUENCY'))
}