from peewee import SqliteDatabase, Model
from utils import AppLogger
from config import get_config


logger = AppLogger()
config = get_config()
db_path = f"./{config.SQLITE_DB_FILENAME}"


database = SqliteDatabase(
    db_path,
    pragmas={
        'journal_mode': 'wal',
        'cache_size': -1024 * 64,
        'foreign_keys': 1,
        'ignore_check_constraints': 0,
        'synchronous': 0
    }
)


class BaseModel(Model):
    """Base model class that all models should inherit from"""
    class Meta:
        database = database


def connect_db():
    """Connect to the database"""
    logger = AppLogger()
    try:
        database.connect()
        logger.info("Database connected successfully")
    except Exception as e:
        logger.error(f"Failed to connect to database: {e}")
        raise


def close_db():
    """Close database connection"""
    if not database.is_closed():
        database.close()


def create_tables(models):
    """Create tables for the given models"""
    logger = AppLogger()
    try:
        database.create_tables(models, safe=True)
        logger.info(f"Created tables for models: {[m.__name__ for m in models]}")
    except Exception as e:
        logger.error(f"Failed to create tables: {e}")
        raise


# Context manager for database transactions
class DatabaseManager:
    def __enter__(self):
        connect_db()
        return database
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        close_db()


# For compatibility with your existing code structure
def get_db_session():
    """
    Compatibility function - Peewee doesn't use sessions like SQLAlchemy
    Instead, use the database instance directly or the DatabaseManager context manager
    """
    logger = AppLogger()
    logger.warn("get_db_session() called - Peewee doesn't use sessions. Use database instance directly.")
    return database