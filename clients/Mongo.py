import settings 
import logging
import certifi
from pymongo import MongoClient, collection


class Mongo():
    def __init__(self) -> None:
        self.logger = logging.getLogger(settings.LOGGER_NAME)
        self._client = MongoClient(settings.MONGO_URL, tlsCAFile=certifi.where()) 

    def __update_state(self) -> None:
        pass 