import logging 
import settings 
from dataclasses import dataclass

@dataclass
class FTX_CONN:
    https: str = ""
    wss: str = ""

class FTX: 
    def __init__(self) -> None:
        self.logger = logging.getLogger(settings.LOGGER_NAME)
        
