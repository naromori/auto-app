from .base import AppConfig


class ProdConfig(AppConfig):
    LOG_LEVEL = "WARN"
    