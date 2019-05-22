from .base import BaseModel
from sqlalchemy import Column, String
from werkzeug.security import generate_password_hash


class UserModel(BaseModel):
    __tablename__ = 'users'

    username = Column(String(30))
    password = Column(String(256), unique=True)
    name = Column(String(40))
    email = Column(String(40), unique=True)

    def __init__(self, username, password, name, email):
        self.username = username
        self.password = generate_password_hash(password, method='sha256')
        self.name = name
        self.email = email

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).one_or_none()

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).one_or_none()
