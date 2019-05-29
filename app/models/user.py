from .base import BaseModel
from sqlalchemy import Column, String
from werkzeug.security import generate_password_hash


class UserModel(BaseModel):
    __tablename__ = 'users'

    username = Column(String(30), unique=True)
    password = Column(String(256))
    name = Column(String(40))
    email = Column(String(40), unique=True)

    def __init__(self, username, password, name, email):
        """
        User constructor
        :param username: username of account
        :param password: password of account
        :param name: name of user
        :param email: email of account
        """
        self.username = username
        self.password = generate_password_hash(password, method='sha256')
        self.name = name
        self.email = email

    @classmethod
    def find_by_username(cls, username):
        """
        Find user by username
        :param username: username being provided
        :return: user with the provided username
        """
        return cls.query.filter_by(username=username).one_or_none()

    @classmethod
    def find_by_email(cls, email):
        """
        Find user by email
        :param email: email being provided
        :return: user with the provided email
        """
        return cls.query.filter_by(email=email).one_or_none()
