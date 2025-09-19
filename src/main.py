import kivy
kivy.require('2.3.1')
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager

from utils import AppLogger, DBConnection, EnvManager, EnvRec

from screens import HomeScreen

class AutoApp(MDApp):

    def build(self):

        self.db = DBConnection()
        self.db.connect()

        sm = ScreenManager()
        sm.add_widget(HomeScreen())

        sm.current = "HomeScreen"

        return sm


def main():
    
    logger = AppLogger()
    logger.debug("App started successfully")
    db_name = EnvManager.get("SQLITE_DB_FILENAME")
    if not db_name:
        logger.warn("Cannot find database filename")
        db = EnvRec.find_env(search_target="*.db")
        env = EnvRec.find_env(search_target=".env")

        is_db = db != []
        is_env = env != []

        if not(is_db):
            logger.error("No database found")
        if not(is_env):
            logger.error("No .env file found")
        
        exit(1)

    app = AutoApp()
    logger.debug("App Class initialized successfully")
    app.run()


if __name__ == "__main__":
    main()