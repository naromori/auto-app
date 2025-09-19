# import sqlite3 as sql
# from .envmgr import EnvManager
# from .logger import AppLogger


# class DBConnection():
    
#     def __init__(self):
#         self.conn: sql.Connection | None = None
#         self.cursor: sql.Cursor | None = None
#         self.logger: AppLogger = AppLogger()
    
#     def connect(self):
#         env = EnvManager()
#         try:
#             db_string = env.get_required("SQLITE_DB_FILENAME")
#         except ValueError as e:
#             self.logger.critical(f"Failed to get database filename: {e}")
#             raise e
#         except Exception as e:
#             self.logger.critical(f"Unhandled exception while getting database filename: {e}")

#         self.conn = sql.connect(db_string)
#         self.cursor = self.conn.cursor()
#         self.logger.debug("Database initialized")


from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

class DBConnection():

    def __init__(self, filename: str):
        self.url = f"sqlite:///./{filename}"
        self.engine