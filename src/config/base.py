class AppConfig:
    DEV = False
    DEBUG = False
    LOG_LEVEL = "WARN"
    PASSWORD_ITERATIONS = 260000
    PASSWORD_SALT_LEN = 16
    MAX_PHOTO_SIZE_MB = 5
    SQLITE_DB_FILENAME = "database.db"
