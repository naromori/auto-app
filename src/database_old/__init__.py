"""
Module for interacting with SQLite database. Implemented using SQLAlchemy.

Reexports:
get_db_session() -> Session:
    Returns a configured SQLAlchemy session object for the database.
"""

from .connection import get_db_session
from .user_repository import UserRepo

__all__ = ["get_db_session", "UserRepo"]
