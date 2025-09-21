from peewee import Model, AutoField, CharField, BlobField, SqliteDatabase
from utils import AppLogger
from config import get_config
from os.path import dirname, abspath, join
import os
import hashlib

config = get_config()
salt_len = config.PASSWORD_SALT_LEN
iterations = config.PASSWORD_ITERATIONS
app_path = abspath(dirname(__name__))
db = SqliteDatabase(join(app_path, config.SQLITE_DB_FILENAME))


class DBConnection:
    
    def __init__(self):
        self.logger = AppLogger()
        self._db = db
        self.models_used = [UserModel]

    def get_database(self):
        return self._db
    
    def close(self):
        self._db.close()

    def create_tables(self):
        self._db.create_tables(self.models_used)

class BaseModel(Model):
        class Meta:
            database = db

class UserModel(BaseModel):

    class Meta:
        table_name = "users"

    id = AutoField(primary_key=True)
    phone = CharField(max_length=12, unique=True, null=False)
    password_hash = BlobField(null=False)
    salt = BlobField(null=False)

    def set_password(self, password: str):
        self.salt = os.urandom(salt_len)
        self.password_hash = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode(),
            self.salt,
            iterations
        )
    
    def check_password(self, password: str):
        if not self.salt or not self.password_hash:
            return False
        
        test_hash = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode(),
            self.salt,
            iterations
        )

        if test_hash == self.password_hash:
            return True
        
        return False
    
    def __str__(self):
        return self.phone
