"""
Login screen module for user authentication.

This module provides the login interface for user authentication
with phone number and password validation.
"""

from typing import Any
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from utils import AppLogger
from assets import MAIN_ADDPOST


Builder.load_file(f"./assets/kv/{MAIN_ADDPOST}")

class AddPostScreen(MDScreen):

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.logger = AppLogger()
        self.logger.debug("FeedScreen initialized")

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