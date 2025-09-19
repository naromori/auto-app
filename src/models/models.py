from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String


class Base(DeclarativeBase):
      pass


class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    phone = Column(String)
    password_hash = Column(String)
    salt = Column(String)


# class Country(Base):
#     __tablename__ = "countries"

#     id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
#     name = Column(String)

# class Manufacturer(Base):
#     __tablename__ = "manufacturers"

#     id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
#     name = Column(String, unique=True)
#     country_id = Column(Integer, ForeignKey('countries.id'), nullable=False)
#     country = relationship("Country", back_populates="manufacturers")

# TODO: Add more models for other entities like Models, Body Types, Generations, etc.
