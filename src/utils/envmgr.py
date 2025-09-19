from dotenv import load_dotenv
from os import getenv, environ
from .logger import AppLogger


class EnvManager():
    
    load_dotenv()

    @staticmethod
    def get(name: str) -> str | None:
        return getenv(name)
    
    @staticmethod
    def get_required(name: str) -> str:
        value = getenv(name)
        if not value:
            logger = AppLogger()
            logger.critical("Missing required environment variable: {name}")
            logger.debug(f"Enviroment Variables Available: {environ}")
            raise ValueError(f"Required Enviromental Variable '{name}' not found")
        return value
    
    @staticmethod
    def reload():
        """Reload .env file"""
        load_dotenv(override=True)
