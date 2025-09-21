from .connection import UserModel
from utils import AppLogger
from peewee import SqliteDatabase
from utils import DataValidator


class UserRepository:

    def __init__(self, db_connection):
        self.db: SqliteDatabase = db_connection
        self.logger = AppLogger()


    def create_user(self, phone: str, password: str):

        phone_valid = DataValidator.clean_phone_number(phone)

        new_user = UserModel(phone=phone_valid)
        new_user.set_password(password)
        new_user.save()

        self.db.close()
    
    def auth(self, phone, password: str) -> bool:

        phone_valid = DataValidator.clean_phone_number(phone)

        user: UserModel = UserModel.get_or_none(UserModel.phone == phone_valid)
        if not user:
            return False
        if user.check_password(password):
            return True
        
        return False
