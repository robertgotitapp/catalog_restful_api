from app.db import Base
from .base import BaseModel
from sqlalchemy import Column, String


class UserModel(BaseModel):
    __tablename__ = 'users'

    username = Column(String(30))
    password = Column(String(256))
    name = Column(String(40))
    email = Column(String(40))

    def __init__(self, username, password, name, email):
        self.username = username
        self.password = password
        self.name = name
        self.email = email

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()
