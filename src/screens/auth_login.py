"""
Login screen module for user authentication.

This module provides the login interface for user authentication
with phone number and password validation.
"""

from typing import Any

from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from utils import AppLogger

Builder.load_file("./assets/kv/auth.login.kv")


class LoginScreen(MDScreen):
    """
    Login screen for user authentication.

    Provides phone number and password input fields with validation.
    Handles user login and navigation to registration screen.
    """

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.logger = AppLogger()
        self.logger.debug("LoginScreen initialized")

    def handle_login(self) -> None:
        """
        Handle login button press.

        Validates phone number format and password presence,
        then navigates to the main application on success.
        Shows error messages for validation failures.
        """
        phone = self.ids.phone_field.text
        password = self.ids.password_field.text

        self.logger.info(f"Login attempt for phone: {phone[:3]}***{phone[-2:] if len(phone) >= 5 else '***'}")

        if not phone or not password:
            self.logger.warning("Login failed: Empty phone or password fields")
            self.show_error_message("Пожалуйста, заполните все поля")
            return

        
        if len(phone) < 11:
            self.logger.warning(f"Login failed: Invalid phone format - {phone}")
            self.show_error_message("Неверный логин или пароль")
            return

        

        self.ids.phone_field.text = ""
        self.ids.password_field.text = ""

        # TODO: Normal auth
        self.logger.info("Login successful - switching to main app")

        from kivymd.app import MDApp
        app = MDApp.get_running_app()
        app.switch_to_main_app()

        # if self.authenticate_user(phone, password):
        #     self.ids.username_field.text = ""
        #     self.ids.password_field.text = ""

        #     app = self.manager.app
        #     app.after_login_success()
        # else:
        #     self.show_error_dialog("Invalid username or password")

    def go_to_register(self) -> None:
        """
        Navigate to the registration screen.

        Switches from login to register screen in the authentication flow.
        """
        self.logger.debug("Navigating to registration screen")
        from kivymd.app import MDApp
        app = MDApp.get_running_app()
        app.switch_auth_screen("register")

    def show_error_message(self, message: str) -> None:
        """
        Display an error message to the user.

        Args:
            message (str): The error message to display
        """
        self.logger.debug(f"Showing error message: {message}")
        from kivymd.uix.snackbar import MDSnackbar, MDSnackbarText

        snackbar = MDSnackbar(
            MDSnackbarText(text=message),
            y="24dp",
            pos_hint={"center_x": 0.5},
            size_hint_x=0.9,
        )
        snackbar.open()