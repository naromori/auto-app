from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from utils import EnvManager, FSUtils, AppLogger


def get_database_url() -> str:
    logger = AppLogger()
    db_filename = EnvManager.get_env("SQLITE_DB_FILENAME")

    if db_filename:
        logger.debug(f"Found SQLite database file `{db_filename}` in environment")
        return f"sqlite:///./{db_filename}"

    logger.warn("No database file specified in environment. Recovering...")

    db_search = FSUtils.find_env(".db")
    logger.debug(f"Database search returned: {db_search}")

    match len(db_search):
        case 0:
            logger.error("No database file found. Exiting...")
            raise FileNotFoundError("Database file not found. None in env.")
        case 1:
            logger.info("A single database file found. Will proceed with that.")
            return f"sqlite:///{db_search[0]}"
        case _:
            logger.error(f"Multiple database files found: {', '.join(db_search)}")
            logger.error("Not sure which one to use. Exiting...")
            raise ValueError("Multiple database files found. None in env.")


db_filename: str | None = EnvManager.get_env("SQLITE_DB_FILENAME")
is_prod: bool = True if EnvManager.get_env("PROD") == 1 else False
database_url: str = get_database_url()

engine = create_engine(database_url, echo=is_prod)

SessionLocal = sessionmaker(autoflush=False, bind=engine)


def get_db_session() -> Session:
    """
    Get Database Session
    """
    session = SessionLocal()
    try:
        return session
    finally:
        session.close()
