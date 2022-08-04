import logging
import settings 
import requests
from requests.exceptions import RequestException
from typing import Dict, Optional

class Https:
    def __init__(self, base_url: str) -> None:
        self.logger = logging.getLogger(settings.LOGGER_NAME)
        self.base_url = base_url
    
    def get(
        self, 
        endpoint: str, 
        params: Optional[Dict] = None, 
        headers: Optional[Dict] = None,
    ) -> requests.Response:
        url = self.base_url + endpoint
        try:
            response = requests.get(url, params=params, headers=headers)
            return response

        except RequestException as e:
            self.logger.error(f"HTTP request exception occured: {e}")
            raise SystemExit()
        
        except Exception as e:
           self.logger.error(f"Other error with http request occured: {e}") 

    def set_default_header(self, header = Dict) -> None:
        self.default_header = header
