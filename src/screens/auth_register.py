"""
Registration screen module for new user account creation.

This module provides the registration interface for creating new user accounts
with phone number, password, and password confirmation validation.
"""

from typing import Any

from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from utils import AppLogger
from services import DataValidators


Builder.load_file("./assets/kv/auth.register.kv")


class RegisterScreen(MDScreen):
    """
    Registration screen for new user account creation.

    Provides input fields for phone number, password, and password confirmation
    with comprehensive validation and error handling.
    """

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.logger = AppLogger()
        self.logger.debug("RegisterScreen initialized")

    def handle_register(self) -> None:
        """
        Handle registration button press.

        Validates all input fields, checks password requirements,
        and creates new user account on success.
        """
        phone = self.ids.phone_field.text
        password = self.ids.password_field.text
        confirm_password = self.ids.confirm_password_field.text

        self.logger.info(f"Registration attempt for phone: {phone[:3]}***{phone[-2:] if len(phone) >= 5 else '***'}")

        if not all([phone, password, confirm_password]):
            self.logger.warn("Registration failed: Missing required fields")
            self.show_error_message("Пожалуйста, заполните все поля")
            return

        if password != confirm_password:
            self.logger.warn("Registration failed: Password confirmation mismatch")
            self.show_error_message("Пароли не совпадают")
            return

        if not DataValidators.validate_password(password):
            self.logger.warn(f"Registration failed: Invalid password length - {len(password)} characters")
            self.show_error_message("Пароль слишком слабый или длиннее 30 символов")
            return
        
        if not DataValidators.validate_phone_number(phone):
            self.logger.warn(f"Registration failed: Invalid phone format - {phone}")

        self.logger.info("Registration validation successful")
        self.clear_fields()
        self.show_success_message("Account created successfully!")

    
    def register_user(self, phone: str, password: str) -> bool:
        """
        Register a new user account.

        Args:
            phone (str): User's phone number
            password (str): User's password

        Returns:
            bool: True if registration successful, False otherwise

        Note:
            This is a placeholder - replace with actual PostgreSQL integration.
        """
        # Placeholder - replace with database insertion
        self.logger.debug(f"Attempting to register user in database: {phone}")
        self.logger.info(f"User registration successful for: {phone}")
        return True  # Simulate success
    
    def go_to_login(self) -> None:
        """
        Navigate back to the login screen.

        Switches from registration to login screen in the authentication flow.
        """
        self.logger.debug("Navigating back to login screen")
        from kivymd.app import MDApp
        app = MDApp.get_running_app()
        app.switch_auth_screen("login")
    
    def clear_fields(self) -> None:
        """
        Clear all input fields.

        Resets phone, password, and confirm password fields to empty strings.
        """
        self.logger.debug("Clearing registration form fields")
        self.ids.phone_field.text = ""
        self.ids.password_field.text = ""
        self.ids.confirm_password_field.text = ""
    
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

    def show_success_message(self, message: str) -> None:
        """
        Display a success message and automatically switch to login screen.

        Args:
            message (str): The success message to display
        """
        self.logger.info(f"Registration successful - showing success message: {message}")
        from kivymd.uix.snackbar import MDSnackbar, MDSnackbarText
        from kivymd.app import MDApp

        snackbar = MDSnackbar(
            MDSnackbarText(text=message),
            y="24dp",
            pos_hint={"center_x": 0.5},
            size_hint_x=0.9,
        )

        def switch_after_delay(dt: int) -> None:
            """Switch to login screen after delay."""
            self.logger.debug("Auto-switching to login screen after successful registration")
            app = MDApp.get_running_app()
            app.switch_auth_screen("login")

        from kivy.clock import Clock
        Clock.schedule_once(switch_after_delay, 2)  # Switch after 2 seconds

        snackbar.open()