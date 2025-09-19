"""
Screens module for the KivyMD auto app.

This module exports all screen classes used in the application,
including authentication screens and main application screens.
"""

from .auth_login import LoginScreen
from .auth_register import RegisterScreen
from .main_menu import MenuScreen
from .main_feed import FeedScreen
from .main_chats import ChatsScreen
from .main_addpost import AddPostScreen
from .main_favourites import FavouritesScreen

__all__ = ["FeedScreen", "LoginScreen", "RegisterScreen", "FavouritesScreen", "AddPostScreen", "MenuScreen", "ChatsScreen"]
