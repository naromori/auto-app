from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager

from utils import AppLogger, DBConnection, EnvManager, EnvRec
from screens import HomeScreen

class AutoApp(MDApp):

    def build(self):

        self.db = DBConnection()

        sm = MDScreenManager()
        sm.add_widget(HomeScreen())
        sm.current = "HomeScreen"

        return sm


def main():
    
    logger = AppLogger()
    logger.info("App instance created successfully")
    env_check()
    logger.info("Enviroment checked successfully")
    app = AutoApp()
    logger.info("App initialized successfully")
    app.run()


def env_check():
    db_name = EnvManager.get("SQLITE_DB_FILENAME")
    logger = AppLogger()
    if not db_name:
        logger.warn("Cannot find database filename")
        db = EnvRec.find_env(search_target="*.db")
        env = EnvRec.find_env(search_target=".env")

        if db != []:
            logger.warn(f"Found database files:{db}")
            is_db = True
        if env != []:
            logger.warn(f"Found .env file {env}")
            is_env = True

        if not(is_db):
            logger.error("No database found")
        if not(is_env):
            logger.error("No .env file found")
        
        exit(1)


if __name__ == "__main__":
    main()