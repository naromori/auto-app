from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, ForeignKey


Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    email = Column(String)
    password_hash = Column(String)
    salt = Column(String)
    
class Country(Base):
    __tablename__ = "countries"

    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column(String)

class Manufacturer(Base):
    __tablename__ = "manufacturers"

    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column(String, unique=True)
    country_id = Column(Integer, ForeignKey('countries.id'), nullable=False)
    country = relationship("Country", back_populates="manufacturers")
