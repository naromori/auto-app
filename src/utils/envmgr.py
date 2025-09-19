from dotenv import load_dotenv
from os import getenv, environ
from .logger import AppLogger


class EnvManager:
    """
    Utility class for managing enviroment variables.
    """

    load_dotenv()

    @staticmethod
    def get_env(name: str) -> str | None:
        """
        Get Enviroment Variable by name.
        Args:
           name (str): The name of the environment variable to get

        Returns:
            str | None: The value of the environment variable if it is present
        """
        return getenv(name)

    @staticmethod
    def get_env_required(name: str) -> str:
        """
        Get Enviroment Variable by name. Raise ValueError if it is not set.
        Args:
            name (str): The name of the environment variable to get

        Returns:
            str: The value of the environment variable

        Raises:
            ValueError: If the environment variable is not set

        """
        value = getenv(name)
        if not value:
            logger = AppLogger()
            logger.critical("Missing required environment variable: {name}")
            logger.debug(f"Enviroment Variables Available: {environ}")
            raise ValueError(f"Required Enviromental Variable '{name}' not found")
        return value

    @staticmethod
    def reload_env() -> None:
        """Reload loaded env variables form .env files"""
        load_dotenv(override=True)
