from __future__ import annotations
import os
import logging
from kivy.logger import ColonSplittingLogRecord, ColoredLogRecord, UncoloredLogRecord
from typing import Union
from config import get_config


class AppKivyFormatter(logging.Formatter):
    """Custom formatter that adds time/level to Kivy's colon-splitting format.

    Format: [Time] [Level] [Module] message
    """

    def __init__(self, *args, use_color=False, **kwargs):
        super().__init__("[%(asctime)s] [%(levelname)-8s] %(message)s",
                         datefmt="%H:%M:%S", *args, **kwargs)
        self._coloring_cls = (
            ColoredLogRecord if use_color else UncoloredLogRecord)

    def format(self, record):
        return super().format(
            self._coloring_cls(ColonSplittingLogRecord(record)))


class AppLogger:
    """Singleton logger class that writes to `latest.log`. Previous `latest.log` gets *removed*."""

    _logger: logging.Logger | None = None
    _instance: AppLogger | None = None

    def __new__(cls) -> AppLogger:
        if cls._instance is None:
            cls._instance = super(AppLogger, cls).__new__(cls)
        return cls._instance

    def __init__(self, name: str = "app_logger", log_file: str = "latest.log") -> None:
        if self._logger is None:
            config = get_config()
            level = config.LOG_LEVEL

            LEVEL_MAP = {
                "DEBUG": logging.DEBUG,
                "INFO": logging.INFO,
                "WARN": logging.WARNING,
                "ERROR": logging.ERROR,
                "CRITICAL": logging.CRITICAL
            }
            level_fmt = LEVEL_MAP.get(level.upper(), logging.WARN)
            self._setup_logger(name, log_file, level_fmt)

    def _setup_logger(self, name: str, log_file: str, level: logging._Level) -> None:
        """Internal method for logging setup"""

        if os.path.exists(log_file):
            os.remove(log_file)

        self._logger = logging.getLogger(name)
        self._logger.setLevel(level)

        self._logger.handlers.clear()

        file_handler = logging.FileHandler(log_file, mode="w")
        file_handler.setLevel(level)

        formatter = AppKivyFormatter(use_color=False)
        file_handler.setFormatter(formatter)
        self._logger.addHandler(file_handler)

        kivy_logger = logging.getLogger("kivy")
        kivy_logger.addHandler(file_handler)
        kivy_logger.setLevel(level)

        kivymd_logger = logging.getLogger("kivymd")
        kivymd_logger.addHandler(file_handler)
        kivymd_logger.setLevel(level)

    def debug(self, message: object, module: str = "") -> None:
        """Log debug message"""
        if self._logger is not None:
            formatted_message = f"{module}: {message}" if module != "" else message
            self._logger.debug(formatted_message)

    def info(self, message: object, module: str = "") -> None:
        """Log info message"""
        if self._logger is not None:
            formatted_message = f"{module}: {message}" if module != "" else message
            self._logger.info(formatted_message)

    def warning(self, message: object, module: str = "") -> None:
        """Log warning message"""
        if self._logger is not None:
            formatted_message = f"{module}: {message}" if module != "" else message
            self._logger.warning(formatted_message)

    def warn(self, message: object, module: str = "") -> None:
        """Log warning message"""
        if self._logger is not None:
            formatted_message = f"{module}: {message}" if module != "" else message
            self._logger.warning(formatted_message)

    def error(self, message: object, module: str = "") -> None:
        """Log error message"""
        if self._logger is not None:
            formatted_message = f"{module}: {message}" if module != "" else message
            self._logger.error(formatted_message)

    def critical(self, message: object, module: str = "") -> None:
        """Log critical message"""
        if self._logger is not None:
            formatted_message = f"{module}: {message}" if module != "" else message
            self._logger.critical(formatted_message)

    def log(self, level: logging._Level, message: object, module: str = ""):
        """Log with runtime level"""
        if self._logger is not None:
            formatted_message = f"{module}: {message}" if module != "" else message
            self._logger.log(level=level, msg=formatted_message)
