"""
Login screen module for user authentication.

This module provides the login interface for user authentication
with phone number and password validation.
"""

from typing import Any

from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.lang import Builder
from utils import AppLogger, DataValidator
from database import UserRepository

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

    def get_app(self) -> MDApp:
        return MDApp.get_running_app()

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

        if not DataValidator.validate_phone_number(phone):
            self.logger.warning("Login failed: Phone validation failed")
            self.show_error_message("Неверный формат номера")
            return

        app = self.get_app()
        user_repo: UserRepository = app.user_repo

        if user_repo.auth(phone=phone, password=password):
            self.logger.info("Login successful - switching to main app")
            self.ids.phone_field.text = ""
            self.ids.password_field.text = ""
            app.switch_to_main_app()
            return
        
        self.logger.info("Login unsuccessfull")
        self.show_error_message("Неправильный логин или пароль")        


    def go_to_register(self) -> None:
        """
        Navigate to the registration screen.

        Switches from login to register screen in the authentication flow.
        """
        self.logger.debug("Navigating to registration screen")

        app = self.get_app()
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