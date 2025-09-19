import os
import logging


class AppLogger:
    """Singleton logger class that writes to `latest.log`. Previous `latest.log` gets *removed*."""
    _logger = None
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AppLogger, cls).__new__(cls)
        return cls._instance
    
    def __init__(self, name='app_logger', log_file='latest.log', level=logging.DEBUG):
        # Will initialize once per session
        if self._logger is None:
            self._setup_logger(name, log_file, level)
    
    def _setup_logger(self, name, log_file, level):
        """Internal method for logging setup"""

        if os.path.exists(log_file):
            os.remove(log_file)

        self._logger = logging.getLogger(name)
        self._logger.setLevel(level)

        self._logger.handlers.clear()

        file_handler = logging.FileHandler(log_file, mode='w')
        file_handler.setLevel(level)

        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        file_handler.setFormatter(formatter)
        self._logger.addHandler(file_handler)
    
    @property
    def logger(self):
        """Get the logger instance"""
        return self._logger
    
    def debug(self, message):
        """Log debug message"""
        self._logger.debug(message)
    
    def info(self, message):
        """Log info message"""
        self._logger.info(message)
    
    def warning(self, message):
        """Log warning message"""
        self._logger.warning(message)
    
    def warn(self, message):
        """Log warning message"""
        self._logger.warning(message)
    
    def error(self, message):
        """Log error message"""
        self._logger.error(message)

    def critical(self, message):
        """Log critical message"""
        self._logger.critical(message)