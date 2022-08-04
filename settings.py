import logging
import os
from dotenv import load_dotenv
load_dotenv()

# Logging 
LOG_LEVEL = logging.DEBUG
CONSOLE_LOG_LEVEL = logging.DEBUG
FILE_LOG_LEVEL = logging.DEBUG
LOGGER_NAME = 'root'

# Mongo
MONGO_URL = os.environ.get("MONGO_URL")