from kivy.lang import Builder
from kivy.properties import StringProperty

from kivymd.app import MDApp
from kivymd.uix.navigationbar import MDNavigationItem
from kivymd.uix.widget import Widget
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
from utils import AppLogger, autolog
from config import get_config
from screens import LoginScreen, RegisterScreen, FeedScreen, FavouritesScreen, ChatsScreen, MenuScreen, AddPostScreen
from database import DatabaseManager


class BaseMDNavigationItem(MDNavigationItem):
    """
    Base navigation item for MDNavigationBar.

    Attributes:
        icon (StringProperty): Icon name for the navigation item
        text (StringProperty): Display text for the navigation item
    """
    icon = StringProperty()
    text = StringProperty()

@autolog(on_completion=False)
class AutoApp(MDApp):
    """
    Main application class for the app.

    This app manages authentication flow and main app navigation.

    Attributes:
        logged_in (bool): Current authentication status
        phone_login (str | None): User's phone number on login
        screen_manager (MDScreenManager): Main screen manager for auth flow
        main_screen_manager (MDScreenManager): Screen manager for main app screens
    """

    @autolog(log_timing=True, on_completion=False)
    def __init__(self) -> None:
        """Initialize the app with default settings."""
        super().__init__()
        #! App Important Variables.
        self.ext_cfg = get_config()
        self.logger = AppLogger()
        self.db = DatabaseManager()
        self.user_repo = self.db.user_repo
        
        #! The End...
        # self.config TODO: add proper config to the app.
        self.logged_in = False
        self.phone_login: str | None = None
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.theme_style = "Light"
        # TODO: EVERYTHING FROM TODO TO HERE IS TEMPORARY

        self.base_screen_file = "./assets/kv/app.base.kv"
        self.logger.info(f"AutoApp initialized with {self.theme_cls.primary_palette} theme and {self.theme_cls.theme_style} style", "Main")

    def build(self) -> Widget:
        """
        Build and return the root widget for the application.

        Sets up the initial screen manager with login and register screens.

        Returns:
            Widget: The root screen manager widget
        """
        self.screen_manager: MDScreenManager = MDScreenManager()

        self.screen_manager.add_widget(LoginScreen(name="login"))
        self.screen_manager.add_widget(RegisterScreen(name="register"))
        self.screen_manager.current = "login"

        self.logger.info(f"Initial screen manager built with screens: {", ".join(self.screen_manager.screen_names)}", "Main")
        self.logger.debug(f"Starting with current screen: {self.screen_manager.current_screen}", "Main")

        return self.screen_manager

    def switch_to_main_app(self) -> None:
        """
        Switch from authentication screens to the main application.

        Loads the main UI from base.kv file and sets up navigation screens.
        Sets logged_in status to True.
        """
        self.logger.info("Switching to main application", "Main")
        self.logged_in = True

        main_widget: Widget = Builder.load_file(self.base_screen_file)

        main_screen = MDScreen(name="main")
        main_screen.add_widget(main_widget)
        self.screen_manager.clear_widgets()
        self.screen_manager.add_widget(main_screen)

        screen_manager: MDScreenManager = main_widget.ids.screen_manager
        screen_manager.add_widget(FeedScreen(name="Feed"))
        screen_manager.add_widget(FavouritesScreen(name="Favourites"))
        screen_manager.add_widget(AddPostScreen(name="Post"))
        screen_manager.add_widget(ChatsScreen(name="Chats"))
        screen_manager.add_widget(MenuScreen(name="Menu"))

        self.main_screen_manager = screen_manager
        screen_manager.current = "Feed"

        self.screen_manager.current = "main"
        self.logger.info(f"Successfully switched to main application with screens: {self.screen_manager.screen_names}", "Main")
        self.logger.debug(f"Current screen: {self.screen_manager.current_screen}", "Main")

    def switch_to_auth(self) -> None:
        """
        Switch back to authentication screens from main app.

        Clears user session and resets to login screen.
        """
        self.logger.info("Switching back to authentication screens", "Main")
        self.logged_in = False
        self.phone_login = None
        self.screen_manager.clear_widgets()
        self.logger.debug("Cleared main application widgets and reset user session", "Main")

        # Re-add auth screens
        self.screen_manager.add_widget(LoginScreen(name="login"))
        self.screen_manager.add_widget(RegisterScreen(name="register"))
        self.screen_manager.current = "login"
        self.logger.info(f"Successfully returned to screen {self.screen_manager.current_screen}")

    def on_switch_tabs(self, screen_name: str) -> None:
        """
        Handle tab switching in the main application.

        Args:
            screen_name (str): Name of the screen to switch to
        """
        if self.main_screen_manager.current == screen_name:
            return
        if self.logged_in and hasattr(self, 'main_screen_manager'):
            self.logger.debug(f"Trying to switch tab to: {screen_name}", "Main")
            self.main_screen_manager.current = screen_name
            self.logger.debug(f"Switched to tab: {screen_name}", "Main")
        else:
            self.logger.warning(f"Attempted to switch tabs to {screen_name} but user not logged in or main screen manager not available", "Main")

    def switch_auth_screen(self, screen_name: str) -> None:
        """
        Switch between authentication screens (login/register).

        Args:
            screen_name (str): Name of the auth screen to switch to ("login" or "register")
        """
        if not self.logged_in:
            self.screen_manager.current = screen_name
            self.logger.debug(f"Switched to authentication screen: {screen_name}", "Main")
        else:
            self.logger.warning(f"Attempted to switch to auth screen {screen_name} but user is already logged in", "Main")
    
    def on_stop(self):
        self.db.close()
        return super().on_stop()

    def on_pause(self):
        self.db.close()
        return super().on_pause()

if __name__ == "__main__":
    AutoApp().run()
