import configparser
import os
from typing import Any

class Config:
    def __init__(self, env: str):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
        
        if env not in self.config:
            raise ValueError(f"Environment '{env}' not found in config file")
        
        self.env = env

    def get(self, key: str, default: Any = None) -> Any:
        return self.config[self.env].get(key, default)

    def getboolean(self, key: str, default: bool = False) -> bool:
        return self.config[self.env].getboolean(key, default)


# Load the configuration based on the current environment
current_env = os.getenv('APP_ENV', 'development')  # Default to 'development' if not set
config = Config(current_env)
