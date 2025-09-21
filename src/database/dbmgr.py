from .connection import DBConnection
from .user_repository import UserRepository
from utils import AppLogger, autolog


class DatabaseManager:

    @autolog()
    def __init__(self):
        self._logger = AppLogger()
        self._logger.debug("Preparing database connection.", "DB Manager")
        self._db = DBConnection()
        self._logger.debug("Creating tables.", "DB Manager")
        self._db.create_tables()
        self._logger.debug("Initializing User Repository.", "DB Manager")
        self.user_repo = UserRepository(self._db.get_database())

    @autolog(on_completion=False)
    def close(self):
        self._db.close()