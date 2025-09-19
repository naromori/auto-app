from .base import AppConfig


class DebugConfig(AppConfig):
    DEV = True
    DEBUG = True
    LOG_LEVEL = "DEBUG"