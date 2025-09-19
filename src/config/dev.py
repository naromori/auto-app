from .base import AppConfig


class DevConfig(AppConfig):
    DEV = True
    DEBUG = False
    LOG_LEVEL = "INFO"
    